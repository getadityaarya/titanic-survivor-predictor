from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("titanic_model.pkl")

# Encoding mappings
sex_map = {"male": 1, "female": 0}
embarked_map = {"C": 0, "Q": 1, "S": 2}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    pclass = int(data["Pclass"])
    sex = sex_map[data["Sex"]]
    age = float(data["Age"])
    sibsp = int(data["SibSp"])
    parch = int(data["Parch"])
    fare = float(data["Fare"])
    embarked = embarked_map[data["Embarked"]]

    features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].tolist()

    return jsonify({"survived": int(prediction), "probability": probability})

if __name__ == "__main__":
    app.run(debug=True)
