#  Spam Email Detection System

This project is an end-to-end **Natural Language Processing (NLP)** application that classifies text messages as **Spam** or **Not Spam** using Machine Learning.

The system provides real-time prediction through a **FastAPI backend** and an interactive **Streamlit frontend**.

---

##  Project Overview

Spam messages are a common problem in communication platforms.  
This project builds an intelligent classifier capable of automatically identifying unwanted promotional or fraudulent messages.

The model learns patterns from message text and predicts whether a message should be considered spam.

---

##  Model Approach

The following NLP pipeline is used:

- Text preprocessing
- TF-IDF Vectorization
- Logistic Regression Classifier
- Class imbalance handling using `class_weight="balanced"`
- N-gram feature extraction

---

##  Model Performance

Model evaluation results:

-  Accuracy: **~97–98%**
-  Spam Recall: **~91%**
-  Cross-Validation F1 Score: **~0.92**

Cross-validation confirms that the model generalizes well and does not suffer from data leakage.

---

## Tech Stack

- Python
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- FastAPI
- Streamlit
- Joblib

---

## Project Structure

Spam-Email-Detection-System/ 
│ 
├── backend/ 
│   ├── main.py              # FastAPI backend 
│   ├── spam_model.pkl       # Trained ML model 
│   └── requirements.txt 
│ 
├── frontend/ 
│   ├── app.py               # Streamlit interface 
│   └── requirements.txt 
│   └── README.md
---

## Running the Project

---

### 1.Run FastAPI Backend

```bash  Open a new terminal

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

API Documentation:http://127.0.0.1:8000/docs


### 2. Run Streamlit Frontend
Open a new terminal

cd frontend
pip install -r requirements.txt
streamlit run app.py

Application runs at : http://localhost:8501



User Message
      ↓
Streamlit Interface
      ↓
FastAPI API Request
      ↓
Machine Learning Model
      ↓
Spam / Not Spam Prediction