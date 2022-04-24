import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import json
import folium


states_india = json.load(open("C:\\Users\\DELL\\Downloads\\india_states.geojson", 'r'))
state_id_map = {}
for feature in states_india["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]
df = pd.read_csv('E:/CAPSTONE/ACCIDENTAL_DEATHS/suicides_dataset.csv')
df['id'] = df["states"].apply(lambda x: state_id_map[x])

print(df.head(5))
all_states = df.states.unique()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=4, tiles='openstreetmap')

cardOne = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("SUICIDES ALONG WITH CAUSES", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "Suicide rates in India have been rising over the past five decades.Suicides during 2019 increased by 3.4% in comparison to 2018.India's contribution to global suicide deaths increased from 25.3% in 1990 to 36.6% in 2016 among women, and from 18.7% to 24.3% among men",
                    className="card-text", style={"color": "rgb(250,250,250)"}
                ),
                dbc.CardLink("Click to learn more", href="https://en.wikipedia.org/wiki/Suicide_in_India"),
                html.Hr(className="my-2"),
                dbc.CardLink("Click this link to check out Non-Profit Organisations that are committed to combating Mental Health Issues.", href="https://www.giveindia.org/blog/6-ngos-tackling-mental-health-issues-head-on/"),
                html.Hr(className="my-2"),
                dcc.Dropdown(id='cause-picker1', options=[{'label': cause, "value": cause} for cause in
                                                         df.causes.unique()],
                             value='Bankruptcy or Indebtedness', clearable=False, style={"color": "#000000"}),
                html.Hr(className="my-2"),
                dcc.Input(id='input_state1', type='number', inputMode='numeric', value=2015,
                          max=2019, min=2015, step=1, required=True),
                html.Button(id='submit_button1', n_clicks=0, children='Submit'),
                html.Div(id='output_state1'),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id='my-choropleth1', style={'padding': '12px', 'width': '60vw'})
                ),
            ]
        )
    ],
    style={"width": "60rem", "position": "center"}, color="dark"
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

app.layout = html.Div(
    [row]
)




