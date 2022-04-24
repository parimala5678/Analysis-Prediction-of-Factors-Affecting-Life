import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import plotly.express as px
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df2 = pd.read_csv(DATA_PATH.joinpath("Death_rate.csv"))
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

figure = px.scatter(df2, x="GDP", y="Life Expectancy", animation_frame="year", animation_group="states",
                    color="states", hover_name="states",
                    log_x=True, size_max=55, range_x=[3000, 29773382], range_y=[50, 99])

cardOne = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Death rate versus Birth rate", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                dbc.CardLink("click to learn more", href="https://en.wikipedia.org/wiki/Demographics_of_India"),
                html.Hr(className="my-2"),
                dcc.Dropdown(id='state-picker', options=[{'label': state, "value": state} for state in
                                                         df2.states.unique()],
                             value='Andaman and Nicobar Islands', clearable=False, style={"color": "#000000"}),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id='my-bar', style={'padding': '10px', 'width': '70vw'})
                ),
            ]
        )
    ],
    style={"width": "65rem", "position": "center"}, color="dark",
)

cardTwo = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Animated Graph between GDP & Life Expectancy", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "The economy of India is a middle income developing market economy. It is the world's sixth-largest"
                    " economy by nominal GDP and the third-largest by purchasing power parity.", className="card-text",
                    style={"color": "rgb(250,250,250)"}
                ),
                html.Div(
                    dcc.Graph(figure=figure, style={'padding': '10px', 'width': '70vw'})
                ),
            ]
        )
    ],
    style={"width": "65rem", "position": "center"}, color="dark",
)

row = html.Div(
    [

        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardOne)),
            ],
            style={'margin': 'auto', 'width': '100vw'},
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardTwo)),
            ],
            style={'margin': 'auto', 'width': '100vw'},
        ),
    ],
    style={'backgroundColor': 'rgb(3, 16, 33)'}
)
foot_alert = html.Div(
    [
        dbc.Alert("Here I considered years only from 2015 to 2019 as "
                  "because of the limitation of the data availability.", color="dark"),
    ]
)

app.layout = html.Div(
    [row, foot_alert]
)
