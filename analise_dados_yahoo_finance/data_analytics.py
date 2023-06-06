#pip install html5lib
#!pip install webdriver-manager
#!pip install python-bcb
#!pip install pandas-datareader
#!pip install mplfinance
#!pip install selenium
#!pip install FPDF
#!pip install mplcyberpunk
#!pip install python-dotenv
#!pip install pywin32

import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
from datetime import datetime
from datetime import timedelta
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import mplcyberpunk
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import requests
from fpdf import FPDF
from matplotlib.dates import date2num
import warnings
warnings.filterwarnings('ignore')

#!pip install fix_yahoo_finance
import io, os, sys, setuptools, tokenize
import yfinance 
import fix_yahoo_finance as yf
from fix_yahoo_finance import __version__

indices = ['^BVSP', '^GSPC']

hoje = datetime.now()
um_ano_atras = hoje - timedelta(days = 366)

# data = yf.download('BVSP',start="2021-01-01", end="2022-01-01")
# dados_mercado = pdr.get_data_yahoo('BVSP',start="2021-01-01", end="2022-01-01")

pd.get_data_yahoo

diplay(data)
print("deu ruim")

indices = ['^BVSP', '^GSPC']
bla = [0,1]
mystocks = []
for t in bla:
    try:
        mystocks[t]=wb.DataReader(t,data_source='yahoo',start='2015-1-1')['Adj Close']
    except:
        continue
display(mystocks)

import fix_yahoo_finance as yf
!pip install fix_yahoo_finance --upgrade --no-cache-dir

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "SPY IWM TLT",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "mtd",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True
    )

data

from pandas_datareader import data as pdr

import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
