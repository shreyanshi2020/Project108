import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as ps

data = ps.read_csv("data.csv")
fig = ff.create_distplot([data["Avg Rating"].tolist()],["Rating"],show_hist= False)
fig.show()