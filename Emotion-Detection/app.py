import streamlit as st
import pickle

st.title('Emotion Classification Using NLP')
model=pickle.load(open('./model/emotion_logistic_regression.pkl','rb'))
emotions = ["anger 😠","disgust 🤮", "fear 😨😱", "joy 😂", "neutral 😐", "sadness 😔", "shame 😳", "surprise 😮"]
def predict_emotion(text):
    result=model.predict([text])
    return result[0]
text= st.text_input('Enter a Sentence')

clk=st.button("Submit")
if clk:
    res=predict_emotion(text)
    if res=='anger':
        st.success(emotions[0])
    elif res=='disgust':
        st.success(emotions[1])
    elif res=='fear':
        st.success(emotions[2]) 
    elif res=='joy':
        st.success(emotions[3]) 
    elif res=='neutral':
        st.success(emotions[4])  
    elif res=='sadness':
        st.success(emotions[5]) 
    elif res=='shame':
        st.success(emotions[6]) 
    elif res=='surprise':
        st.success(emotions[7])                            
    
    