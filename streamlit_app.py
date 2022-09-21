from datetime import date, datetime
import streamlit as st
import yfinance as yf
import plotly.express as px

# print title
st.title("Streamlit Web App")

# print plain text
st.write("A Streamlit App that visualizes **High** stock price data when stocks and a date range are selected.")
st.write("Author: Kenneth Dei-Amoah")

# a list of stock names
stock_names = ['AAPL', 'NFLX', 'MSFT', 'TWTR', 'GOOGL']

# select a stock to check
target_stock = st.multiselect('Choose at least TWO stocks to visualize. Default stocks: AAPL, NFLX', [
                              'AAPL', 'NFLX', 'MSFT', 'TWTR', 'GOOGL'], default=['AAPL', 'NFLX'])

# start date of the stock infomation, default is the first day of year 2021
start_date = st.date_input('Start Date', datetime(2021, 1, 1))

# end date of the stock infomation, default is date of today
end_date = st.date_input("End Date")

# get today's date
today = date.today()
if st.button('Submit'):
    # check valid date
    if start_date > today or end_date > today:
        st.write("## **Please select a valid date period.**")
    else:
        # download the stock data based on stock name, start/end date
        data = yf.download(target_stock, start_date, end_date)
        # show a progress bar
        with st.spinner(text='In progress'):

            fig = px.line(data['High'], x=data.index, y=list(data['High'].columns), title=(
                f"High Stock Price: {start_date} to {end_date}"), labels={"value": "Stock Price ($)", "variable": "Stock"})

            st.write(fig)
