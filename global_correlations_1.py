import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
from fredapi import Fred
py.sign_in('srjain', 'AWR06Gn6LYQ4HHrspVXW')

fred = Fred(api_key='a0718ea00e6784c5f8b452741622a98c')


stocklist = ['FXF','FXB','FXE','FXA','SPY','EWJ','EWG','IWV','IYY','FEZ','ONEQ',\
             'GLD','SLV','OIL','UNL','JJC','WEAT','CORN','TLT','IEF']   
column_name = ['USD/JPY','GBP/USD','EUR/USD','AUD/USD','S&P','NIKKEI',\
               'DAX','RUSSELL','DOW','EURO_50','NASDAQ','GOLD','SILVER',\
               'OIL','GAS','COPPER','WEAT','CORN','20yr_Bond','7_10_yr_Bond']
df = pd.DataFrame()
start = datetime(2011,9,19)
end = datetime(2016,12,16)
for i,j in enumerate(stocklist): 
    p = wb.DataReader(j,'yahoo',start,end)
    return_df = p['Adj Close']
    col_name = column_name[i]
    return_df_build = pd.DataFrame(return_df.values,index=return_df.index,\
                                   columns=[col_name])
    print(return_df_build.head())
    if df.empty:
        df = return_df_build
    else:
        df = pd.concat([df,return_df_build], axis=1)


   
etf = df
etf_ret = df.pct_change(1)
corr1 = etf_ret.rolling(window=12).corr(etf_ret['S&P'])
spy_aud = pd.concat([etf['S&P'],corr1['AUD/USD']], axis=1)

spy_aud['X'] = spy_aud.index
spy_aud.reset_index()

trace1 = go.Scatter(
    x=spy_aud['X'],
    y=spy_aud['S&P'],
    name='SPY Data'
) 

trace2 = go.Scatter(
    x=spy_aud['X'],
    y=spy_aud['AUD/USD'],
    name='AUD/USD & SPY Correlation',
    yaxis='y2'
) 
data = [trace1, trace2]
layout = go.Layout(
    title='AUD/USD Correlation',
    yaxis=dict(
        title='SPY Cumulative Return'
    ),
    yaxis2=dict(
        title='Correlation',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='multiple-axes-double', sharing='public')

T_10Y = pd.DataFrame(fred.get_series('DGS10',observation_start='9/19/2011'))

trace3 = go.Scatter(
    x=spy_aud['X'],
    y=spy_aud['S&P'],
    name='SPY Data'
) 

trace4 = go.Scatter(
    x=spy_aud['X'],
    y=T_10Y[0],
    name='Treasury 10 Year Yield',
    yaxis='y2'
) 

data1 = [trace3, trace4]
layout1 = go.Layout(
    title='SPY Cumulative',
    yaxis=dict(
        title='SPY Cumulative Return'
    ),
    yaxis2=dict(
        title='Treasury & S&P',
        titlefont=dict(
            color='rgb(0, 98, 63)'
        ),
        tickfont=dict(
            color='rgb(134, 197, 225)'
        ),
        overlaying='y',
        side='right'
    )
)

fig1 = go.Figure(data=data1, layout=layout1)
plot_url1 = py.plot(fig1, filename='10 Year Treasury', sharing='public')
# Treasury SPY Correlation
corr2 = etf_ret.rolling(window=12).corr(T_10Y[0])

trace5 = go.Scatter(
    x=spy_aud['X'],
    y=corr2['S&P'],
    name='Correlation 10 Y Treasury & S&P'
) 

trace6 = go.Scatter(
    x=spy_aud['X'],
    y=T_10Y[0],
    name='Treasury 10 Year Yield',
    yaxis='y2'
) 

data2 = [trace5, trace6]
layout2 = go.Layout(
    title='Correlation 10 Y Treasury & S&P',
    yaxis=dict(
        title='Correlation'
    ),
    yaxis2=dict(
        title='Treasury 10 Year Yield',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)

fig2 = go.Figure(data=data2, layout=layout2)
plot_url2 = py.plot(fig2, filename='Correlation 10 Year Treasury & SPY',\
                    sharing='public')
