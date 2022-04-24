import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import Input, Output
from dash import html
import pandas as pd
import plotly.express as px
import json
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df3 = pd.read_csv(DATA_PATH.joinpath("alcohol_and_speed_deaths.csv"))
states_india = json.load(open("C:\\Users\\DELL\\Downloads\\india_states.geojson", 'r'))
state_id_map = {}
for feature in states_india["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

df3['id'] = df3["states"].apply(lambda x: state_id_map[x])

all_states = df3.states.unique()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

cardTwo = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("SPEED DEATHS", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "Did you know that, in a cause-wise split, maximum number of road crashes and deaths were caused by over-speeding, which accounted for 67.3 per cent or 1,01,699 deaths, 71 per cent of crashes and 72.4 per cent of injuries",
                    className="card-text", style={"color": "rgb(250,250,250)"}
                ),
                dbc.CardLink("Click to learn more", href="https://injuryfacts.nsc.org/motor-vehicle/motor-vehicle-safety-issues/speeding/"),
                html.Hr(className="my-2"),
                dcc.Dropdown(id='state-picker', options=[{'label': state, "value": state} for state in
                                                         df3.states.unique()],
                             value='Andaman & Nicobar Island', clearable=False, style={"color": "#000000"}),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id='my-bar4', style={'padding': '12px', 'width': '60vw'})
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
                dbc.Col(html.Div(cardTwo),
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
            "All the data is taken from an open-source website called data.gov.in",
            color="dark"),
    ]
)

# layout

app.layout = html.Div(
    [row, foot_alert]
)

