import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import Input, Output
from dash import html
import pandas as pd
import json
import pathlib

states_india = json.load(open("C:\\Users\\DELL\\Downloads\\india_states.geojson", 'r'))
state_id_map = {}
for feature in states_india["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df3 = pd.read_csv(DATA_PATH.joinpath("alcohol_and_speed_deaths.csv"))
df3['id'] = df3["states"].apply(lambda x: state_id_map[x])

all_states = df3.states.unique()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

cardOne = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("ALCOHOL DEATHS", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "Fifteen years later and despite a set of strict laws and regulations, drunk driving is one of the major reasons behind road accidents in India. According to the Ministry of Road Transport & Highways, in 2019 there were 12,256 road accidents related to drunk driving.", className="card-text",
                    style={"color": "rgb(250,250,250)"}
                ),
                dbc.CardLink("Click to learn more", href="https://pib.gov.in/Pressreleaseshare.aspx?PRID=1577134"),
                html.Hr(className="my-2"),
                dcc.Dropdown(id='state-picker', options=[{'label': state, "value": state} for state in
                                                         df3.states.unique()],
                             value='Andaman & Nicobar Island', clearable=False, style={"color": "#000000"}),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id='my-bar3', style={'padding': '12px', 'width': '60vw'})
                ),
            ]
        )
    ],
    style={"width": "60rem", "position": "center"}, color="dark",
)
row = html.Div(
    [
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardOne),
                        width={"size": 6, "offset": 1},
                        )

            ],
            style={'margin': 'auto', 'width': '81vw'},
        ),
], style={'backgroundColor': 'rgb(3, 16, 33)'}
)

foot_alert = html.Div(
    [
        dbc.Alert(
            "Here I have considered Only the year 2015 to 2019 because of the limitation of the data available on the "
            "internet.",
            color="dark"),
    ]
)

# layout

app.layout = html.Div(
    [row, foot_alert]
)
