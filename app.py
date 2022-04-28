# Importing dependencies
import pandas as pd
import dash 
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Starting Dash
app = dash.Dash(__name__)

# Using the Seaborn dataset library, I chose data on the Titantic
import seaborn as sns
# print(sns.get_dataset_names())

# Load the dataset
df = sns.load_dataset('titanic')
df

# Dropping Nan values in the DataFrame
df = df.dropna()

# Using Plotly Express
import plotly.express as px

# This figure shows the genders and ages of passengers, and whether they're alive or not
fig = px.scatter(df, x="age", y="sex", color="alive", size="age")
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()

#Create the layout and start the app
app.layout = html.Div(children=[
    html.H1(children='First Dash using Titanic Data'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
