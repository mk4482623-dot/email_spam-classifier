import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english'):
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('modell.pkl', 'rb'))

st.title("SMS Spam Classifier")
st.markdown("Check whether a message is Spam or Not Spam")

st.sidebar.title("About")
st.sidebar.write("Model: Machine Learning")
st.sidebar.write("Vectorizer: TF-IDF")
st.sidebar.write("Built with Streamlit")

input_sms = st.text_area("Enter your message here:")

if st.button('Predict'):

    if input_sms.strip() == "":
        st.warning("Please enter a message")
    else:
        transform_sms = transform_text(input_sms)
        vec_input = tfidf.transform([transform_sms])
        result = model.predict(vec_input)[0]
        prob = model.predict_proba(vec_input)[0][1]

        if result == 1:
            st.error(f"Spam (Confidence: {prob*100:.2f}%)")
        else:
            st.success(f"Not Spam (Confidence: {(1 - prob)*100:.2f}%)")

st.markdown("### Try Examples")
col1, col2 = st.columns(2)
with col1:
    if st.button("Spam Example"):
        st.write("Try: WIN a FREE iPhone now!!! Click here")
        st.write("Try: You could be entitled up to £3,160 in compensation from mis-sold PPI on a credit card or loan. Please reply PPI for info or STOP to opt out")

with col2:
    if st.button("Normal Example"):
        st.write("Try: Hey, are we meeting today?")
        st.write("Try: hey! i am free today , should we go for a movie date")