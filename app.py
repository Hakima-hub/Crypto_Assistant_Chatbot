import streamlit as st
from Scripts.data_loader import get_live_price
from Scripts.model_predict import predict_trend
from Scripts.chatbot import chatbot_response
from tensorflow import keras

st.set_page_config(page_title="Crypto Chatbot", layout="wide")
st.title("💬 Crypto Trading Assistant")

# Live Price Section
st.subheader("Live Price")
symbol = st.text_input("Enter Crypto Pair", "BTCUSDT")
if st.button("Get Live Price"):
    price = get_live_price(symbol)
    st.success(f"Current {symbol} price: {price} USD")

# Prediction Section
st.subheader("Market Prediction")
features_input = st.text_input("Enter Features (comma-separated)", "45000,1.2,0.8")
if st.button("Predict Trend"):
    try:
        features = [float(x) for x in features_input.split(",")]
        prediction = predict_trend(features)
        st.info(f"Predicted Market Trend: {prediction}")
    except:
        st.error("Error in prediction. Check feature format.")

# Chatbot Section
st.subheader("Ask the Chatbot")
user_question = st.text_input("Ask about crypto (e.g., 'What is RSI?')")
if st.button("Get Answer"):
    st.write(chatbot_response(user_question))
