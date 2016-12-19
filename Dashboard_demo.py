# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:23:18 2016

@author: ZFang
"""

import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import pandas as pd



py.sign_in('fzn0728', 'yoXOLw8dqTWiwYZvsv9O')
df_HFRX = pd.read_csv('C:/Users/ZFang/Desktop/TeamCo/Plotly/HFRX.csv',encoding = 'iso-8859-1')
df_Equity_Index = pd.read_csv('C:/Users/ZFang/Desktop/TeamCo/Plotly/Equity_Index.csv',encoding = 'iso-8859-1')
df_Bond_Yield = pd.read_csv('C:/Users/ZFang/Desktop/TeamCo/Plotly/Bond_Yield.csv',encoding = 'iso-8859-1')
df_FX_Rate = pd.read_csv('C:/Users/ZFang/Desktop/TeamCo/Plotly/FX_Rate.csv',encoding = 'iso-8859-1')




table_HFRX = FF.create_table(df_HFRX)
table_Equity_Index = FF.create_table(df_Equity_Index)
table_Bond_Yield = FF.create_table(df_Bond_Yield)
table_FX_Rate = FF.create_table(df_FX_Rate)




py.plot(table_HFRX, filename='table_HFRX')
py.plot(table_Equity_Index, filename='df_Equity_Index')
py.plot(table_Bond_Yield, filename='df_Bond_Yield')
py.plot(table_Bond_Yield, filename='df_FX_Rate')



