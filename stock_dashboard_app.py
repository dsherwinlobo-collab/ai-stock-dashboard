import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
st.title("AI Stock Analysis Dashboard")
ticker = st.text_input("Enter Stock Symbol", "AAPL")
if st.button("Analyze Stock"):
    data = yf.download(ticker, period="1y")
    data["MA20"] = data["Close"].rolling(window=20).mean()
    data["MA50"] = data["Close"].rolling(window=50).mean()
    data["Day"] = range(len(data))
    x = data[["Day"]]
    y = data["Close"]
    model = LinearRegression()
    model.fit(x, y)
    next_day = [[len(data)]]
    prediction = model.predict(next_day)
    st.write("Predicted next price:", prediction[0])
    fig, ax = plt.subplots()
    data[["Close","MA20","MA50"]].plot(ax=ax)
    st.pyplot(fig)