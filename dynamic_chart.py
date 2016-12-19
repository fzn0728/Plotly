# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:28:24 2016

@author: ZFang
"""
import plotly
import numpy as np 
import plotly.plotly as py  
import plotly.tools as tls   
import plotly.graph_objs as go
import time
import datetime


token_1 = 'i0fvy0wj52'   # I'm getting my stream tokens from the end to ensure I'm not reusing tokens
token_2 = 'yh3pqfpedh'   
print(token_1)
print(token_2)

stream_id1 = dict(token=token_1, maxpoints=60)
stream_id2 = dict(token=token_2, maxpoints=60)


trace1 = go.Scatter(x=[], y=[], stream=stream_id1, name='trace1')
trace2 = go.Scatter(x=[], y=[], stream=stream_id2, yaxis='y2', name='trace2', marker=dict(color='rgb(148, 103, 189)'))

data = [trace1, trace2]
layout = go.Layout(
    title='Streaming Two Traces',
    yaxis=dict(
        title='y for trace1'
    ),
    yaxis2=dict(
        title='y for trace2',
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
plot_url = py.plot(fig, filename='multple-trace-axes-streaming')


s_1 = py.Stream(stream_id=token_1)
s_2 = py.Stream(stream_id=token_2)


s_1.open()
s_2.open()



k=10
i=0

while True:
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    delta = np.random.randint(4,10) 
    y = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0] 
    s_1.write(dict(x=x,y=y))
    s_2.write(dict(x=x,y=(-delta*y)))
    time.sleep(0.8)
    i += 1
s_1.close()
s_2.close()

tls.embed('streaming-demos','124')