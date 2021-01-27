import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Stock Price
""")

tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '1d', start = '2020-1-1', end = '2020-12-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
