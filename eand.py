import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

sheet_id = "1r9LAQ4yKhl7IudzmTHdYAeWZN1qGYUgs"
data = pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?fromat=xlsx")
price = pd.read_excel(data, "price", header=0, index_col="Date")

st.title("Emirates Telecommunications Group Company PJSC (ETISALAT.AB)")
financial = pd.read_excel(data, "financials", header=0)

price_performance, revenue, net_income = st.tabs(["Price Performance-Last 5Yr", "Revenue Performance", "Net Income Growth"])

with price_performance:
    st.header("Price Movements")
    fig, ax1 = plt.subplots()
    ax1.plot(price['EAND'], label='EAND', color='red')
    ax1.plot(price['ADX Indexd'], label='ADX Indexd', color='blue')
    ax1.plot(price['DFM Indexd'], label='DFM Indexd', color='black')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Price')
    ax1.legend(loc='upper left')
    ax1.axhline(y=19, color='green', linestyle='--', label='Target Price')
    ax1.text(x=price.index[50], y=19, s='Target Price', color='green', verticalalignment='bottom',horizontalalignment='center')
    ax2 = ax1.twinx()
    ax2.bar(price.index, price['Volume'], label = "Volume", alpha=0.3, color='gray')
    ax2.set_ylabel('Volume')
    ax2.set_ylim(0, 30000)
    plt.title('EAND Price Performance for Last 5 Years')
    st.pyplot(fig)

with revenue:
    st.header("Historical and Estimated")
    fig, ax = plt.subplots()
    bar_width = 0.7
    index = range(len(financial['Year']))
    colors = ['blue'] * (len(financial['Revenue']) - 5) + ['red'] * 5
    bar1 = ax.bar(index, financial['Revenue'], bar_width, label='Revenue', color=colors)
    ax.set_xlabel('Year')
    ax.set_ylabel("AED'Mn")
    ax.set_title('Revenue by Year')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(financial['Year'])
    ax.set_ylim(45000, max(financial['Revenue']) + 5000)
    ax.legend()
    st.pyplot(fig)
    
with net_income:
    st.header("Historical and Estimated")
    fig, ax = plt.subplots()
    bar_width = 0.7
    index = range(len(financial['Year']))
    colors = ['blue'] * (len(financial['Net Income']) - 5) + ['red'] * 5
    bar1 = ax.bar(index, financial['Net Income'], bar_width, label='Net Income', color=colors)
    ax.set_xlabel('Year')
    ax.set_ylabel("AED'Mn")
    ax.set_title('Net Income by Year')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(financial['Year'])
    ax.set_ylim(8000, max(financial['Net Income']) + 1000)
    ax.legend()
    st.pyplot(fig)
    