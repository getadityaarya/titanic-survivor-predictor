# 🚢 Titanic Survival Prediction

This project predicts the survival chances of passengers on the Titanic using a Decision Tree Classifier. It includes a simple web application built using Flask and HTML/CSS for user input and real-time prediction.

---

## 📊 Problem Statement

The goal is to build a classification model that predicts whether a passenger would survive based on features like class, age, sex, fare, and more.

---

## 📁 Project Structure

```
titanic-survival-prediction/
├── app/                    # Flask web app
│   ├── app.py
│   └── templates/
│       └── index.html
├── data/
│   └── t2.csv              # Titanic dataset
├── notebooks/
│   └── titanic_model.ipynb # Training & EDA
├── titanic_model.pkl       # Trained model
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy, Scikit-learn
- Decision Tree Classifier
- Flask (for web app)
- HTML/CSS + JavaScript (for frontend)

---

## 🔍 Features

- Cleaned and preprocessed Titanic dataset
- Feature selection and encoding
- Trained a Decision Tree Classifier
- Built a prediction web app using Flask
- Encoded user input and returned survival prediction with probability

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/getadityaarya/titanic-survivor-predictor.git
cd titanic-survival-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model (optional)
Open `notebooks/titanic_model.ipynb`, run all cells, and export the model using:
```python
joblib.dump(clf, 'titanic_model.pkl')
```

### 4. Run the app
```bash
python app/app.py
```

Open your browser at `http://127.0.0.1:5000`

---

## 🧪 Example

You can input:
- Age: `25`
- Sex: `female`
- Pclass: `1`
- Fare: `100`

It will predict: **"Survived"** with 85% confidence 🎉

---

## 📌 Future Improvements

- Add visualizations with SHAP for model interpretability
- Deploy on Render or Railway
- Improve frontend with Bootstrap or Tailwind

---

## 📂 Dataset

This dataset is a part of the [Kaggle Titanic Challenge](https://www.kaggle.com/competitions/titanic/data).

---

## 👨‍💻 Author

Aditya Arya  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)
