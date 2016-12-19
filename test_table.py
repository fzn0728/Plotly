# Get this figure: fig = py.get_figure("https://plot.ly/~jfdarre/1359/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~jfdarre/1359/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="TOTAL LOAN AMOUNT ISSUED THOUGH LC<BR>(HOVER FOR BREAKDOWN) (19)", fileopt="extend")
# Get z data of first trace: z1 = py.get_figure("https://plot.ly/~jfdarre/1359/").get_data()[0]["z"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('fzn0728', 'yoXOLw8dqTWiwYZvsv9O')
trace1 = {
  "z": [28.7, 118.3, 65.6, 207.1, 500, 203.9, 143.8, 26.3, 500, 308, 51.7, 0.1, 0.1, 386, 143.1, 84, 88.2, 113, 235.6, 233.2, 0, 231, 163.7, 147.3, 35, 26.1, 260.7, 0.1, 45.3, 374.9, 52.8, 125.6, 500, 301.6, 85.6, 111, 328.1, 39.8, 113.7, 18.2, 132.9, 500, 68, 300.5, 17.9, 214.4, 118.7, 49.4, 24], 
  "colorbar": {"title": "Amount Issued <br>in millions USD"}, 
  "colorscale": [
    ["0", "rgb(201, 218, 248)"], [1, "rgb(61, 133, 198)"]], 
  "locationmode": "USA-states", 
  "locations": ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"], 
  "marker": {"line": {
      "color": "rgb(70,130,180)", 
      "width": 1
    }}, 
  "text": ["Alaska <br> Total amount issued: 28.7 <br> Number of issued loans: 1,726 <br> Default rates: 4.17", "Alabama <br> Total amount issued: 118.3 <br> Number of issued loans: 8,113 <br> Default rates: 5.87", "Arkansas <br> Total amount issued: 65.6 <br> Number of issued loans: 4,733 <br> Default rates: 5.09", "Arizona <br> Total amount issued: 207.1 <br> Number of issued loans: 14,753 <br> Default rates: 5.1", "California <br> Total amount issued: 1,385.7 <br> Number of issued loans: 96,310 <br> Default rates: 5.9", "Colorado <br> Total amount issued: 203.9 <br> Number of issued loans: 13,713 <br> Default rates: 4.24", "Connecticut <br> Total amount issued: 143.8 <br> Number of issued loans: 9,746 <br> Default rates: 4.81", "Delaware <br> Total amount issued: 26.3 <br> Number of issued loans: 1,815 <br> Default rates: 4.79", "Florida <br> Total amount issued: 606.8 <br> Number of issued loans: 44,014 <br> Default rates: 6.09", "Georgia <br> Total amount issued: 308 <br> Number of issued loans: 20,887 <br> Default rates: 4.89", "Hawaii <br> Total amount issued: 51.7 <br> Number of issued loans: 3,444 <br> Default rates: 6.01", "Iowa <br> Total amount issued: 0.1 <br> Number of issued loans: 10 <br> Default rates: 20", "Idaho <br> Total amount issued: 0.1 <br> Number of issued loans: 12 <br> Default rates: 8.33", "Illinois <br> Total amount issued: 386 <br> Number of issued loans: 25,729 <br> Default rates: 4.79", "Indiana <br> Total amount issued: 143.1 <br> Number of issued loans: 9,699 <br> Default rates: 3.96", "Kansas <br> Total amount issued: 84 <br> Number of issued loans: 5,806 <br> Default rates: 4.63", "Kentucky <br> Total amount issued: 88.2 <br> Number of issued loans: 6,184 <br> Default rates: 5.4", "Louisiana <br> Total amount issued: 113 <br> Number of issued loans: 7,709 <br> Default rates: 5.31", "Massachusetts <br> Total amount issued: 235.6 <br> Number of issued loans: 15,058 <br> Default rates: 5.17", "Maryland <br> Total amount issued: 233.2 <br> Number of issued loans: 15,230 <br> Default rates: 5.32", "Maine <br> Total amount issued: 0 <br> Number of issued loans: 4 <br> Default rates: 0", "Michigan <br> Total amount issued: 231 <br> Number of issued loans: 16,429 <br> Default rates: 5.13", "Minnesota <br> Total amount issued: 163.7 <br> Number of issued loans: 11,589 <br> Default rates: 4.88", "Missouri <br> Total amount issued: 147.3 <br> Number of issued loans: 10,340 <br> Default rates: 5.59", "Mississippi <br> Total amount issued: 35 <br> Number of issued loans: 2,309 <br> Default rates: 2.08", "Montana <br> Total amount issued: 26.1 <br> Number of issued loans: 1,921 <br> Default rates: 3.9", "North Carolina <br> Total amount issued: 260.7 <br> Number of issued loans: 18,043 <br> Default rates: 5.26", "Nebraska <br> Total amount issued: 0.1 <br> Number of issued loans: 11 <br> Default rates: 54.55", "New Hampshire <br> Total amount issued: 45.3 <br> Number of issued loans: 3,105 <br> Default rates: 4.19", "New Jersey <br> Total amount issued: 374.9 <br> Number of issued loans: 24,510 <br> Default rates: 5.81", "New Mexico <br> Total amount issued: 52.8 <br> Number of issued loans: 3,586 <br> Default rates: 5.41", "Nevada <br> Total amount issued: 125.6 <br> Number of issued loans: 9,114 <br> Default rates: 6.68", "New York <br> Total amount issued: 780.4 <br> Number of issued loans: 54,322 <br> Default rates: 5.62", "Ohio <br> Total amount issued: 301.6 <br> Number of issued loans: 21,322 <br> Default rates: 4.96", "Oklahoma <br> Total amount issued: 85.6 <br> Number of issued loans: 5,830 <br> Default rates: 5.2", "Oregon <br> Total amount issued: 111 <br> Number of issued loans: 8,219 <br> Default rates: 5.02", "Pennsylvania <br> Total amount issued: 328.1 <br> Number of issued loans: 22,971 <br> Default rates: 5.06", "Rhode Island <br> Total amount issued: 39.8 <br> Number of issued loans: 2,855 <br> Default rates: 5.39", "South Carolina <br> Total amount issued: 113.7 <br> Number of issued loans: 7,751 <br> Default rates: 4.36", "South Dakota <br> Total amount issued: 18.2 <br> Number of issued loans: 1,340 <br> Default rates: 4.78", "Tennessee <br> Total amount issued: 132.9 <br> Number of issued loans: 8,894 <br> Default rates: 4.25", "Texas <br> Total amount issued: 785.3 <br> Number of issued loans: 50,969 <br> Default rates: 4.31", "Utah <br> Total amount issued: 68 <br> Number of issued loans: 4,713 <br> Default rates: 5.69", "Virginia <br> Total amount issued: 300.5 <br> Number of issued loans: 19,456 <br> Default rates: 5.24", "Vermont <br> Total amount issued: 17.9 <br> Number of issued loans: 1,293 <br> Default rates: 4.1", "Washington <br> Total amount issued: 214.4 <br> Number of issued loans: 14,645 <br> Default rates: 5.37", "Wisconsin <br> Total amount issued: 118.7 <br> Number of issued loans: 8,365 <br> Default rates: 4.79", "West Virginia <br> Total amount issued: 49.4 <br> Number of issued loans: 3,401 <br> Default rates: 3.32", "Wyoming <br> Total amount issued: 24 <br> Number of issued loans: 1,558 <br> Default rates: 3.02"], 
  "type": "choropleth"
}
data = Data([trace1])
layout = {
  "geo": {
    "lakecolor": "rgb(255,255,255)", 
    "projection": {"type": "albers usa"}, 
    "scope": "usa", 
    "showlakes": False
  }, 
  "title": "TOTAL LOAN AMOUNT ISSUED THOUGH LC<BR>(HOVER FOR BREAKDOWN)"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)