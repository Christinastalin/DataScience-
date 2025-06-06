import streamlit as st
import pickle as pickle
import string
import nltk
from nltk import PorterStemmer
from nltk.corpus import stopwords
nltk.data.path.append('C:/Users/chris/PycharmProjects/sms-spam-classification/.venv/Lib/site-packages/nltk')

nltk.download('stopwords')
nltk.download('punkt_tab')
ps= PorterStemmer()
def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)

  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)



tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('Email/SMS Spam Classification')

input_text = st.text_input('Enter your message')
if st.button('Predict'):
    #Preprocessing the input text
    transformed_text= transform_text(input_text)

    #Vectorize
    vector_input = tfidf.transform([transformed_text])

    #Predict
    result = model.predict(vector_input)

    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')

