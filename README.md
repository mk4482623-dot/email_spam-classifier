# 📩 SMS Spam Classifier

A Machine Learning web application that classifies messages as **Spam** or **Not Spam** using Natural Language Processing and Streamlit.

---

## 🚀 Demo

Type a message and instantly check whether it is spam along with a confidence score.

---

## 🧠 Features

* Text preprocessing using NLTK (tokenization, stopword removal, stemming)
* TF-IDF Vectorization
* Machine Learning model for classification
* Confidence score display
* Interactive UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* NLTK
* NumPy
* Pandas

---

## 📂 Project Structure

```
sms-spam-classifier/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── images/
│   ├── wordcloud.png
│   └── model_comparison.png
└── .gitignore
```

---

## 📊 Model Details

* Vectorizer: TF-IDF
* Algorithm: Naive Bayes
* Input: Raw text message
* Output: Spam / Not Spam with probability

---

## 🏆 Model Comparison

Multiple models were trained and evaluated:

* Naive Bayes
* Logistic Regression
* Support Vector Machine (SVM)

Naive Bayes performed best in terms of **accuracy and precision**, making it the final selected model.

### 📈 Performance Comparison Table

![Model Comparison](images/model_comparison.png)

---

## ☁️ Word Cloud Visualization

Word clouds were generated during Exploratory Data Analysis (EDA) to visualize the most frequent words in spam and non-spam messages.

![Word Cloud](images/wordcloud.png)

---

## 🟢 Live Demo

👉 https://emailspam-classifier-nun.streamlit.app/

---


## 🤝 Contributing

Feel free to fork this repository and improve the project.

---
