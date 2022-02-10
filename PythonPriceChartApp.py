import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Python Price Chart App
 
 Showing the **closing price** and ***volume*** of S&P and BTC

""")

tickerSymbol = 'SPY'

# ticker2Symbol = 'BTC'


ticker.Data = yf.Ticker(tickerSymbol)

# ticker2.Data = yf.Ticker(ticker2Symbol)


tickerDf = tickerData.history(period='5d', start='2010-5-31', end='2020-5-31')

# ticker2Df = ticker2Data.history(period='5d', start='2010-5-31', end='2020-5-31')



st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.line_chart(ticker2Df.Close)
st.line_chart(ticker2Df.Volume)
