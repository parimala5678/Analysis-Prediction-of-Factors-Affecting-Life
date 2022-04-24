import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import json
import pathlib
from dash.exceptions import PreventUpdate
from plotly.graph_objects import Layout
from plotly.validator_cache import ValidatorCache

colors = {'Andaman and Nicobar Islands': ['rgb(0, 37, 77)', 'rgb(0, 51, 102)', 'rgb(0, 86, 179)', 'rgb(0, 111, 230)',
                                          'rgb(51, 150, 255)'],
          'Andhra Pradesh': ['rgb(153, 77, 0)', 'rgb(179, 89, 0)', 'rgb(255, 153, 51)', 'rgb(255, 179, 102)',
                             'rgb(255, 204, 153)'],
          'Arunanchal Pradesh': ['rgb(0, 77, 0)', 'rgb(0, 102, 0)', 'rgb(0, 179, 0)', 'rgb(0, 230, 0)',
                                 'rgb(204, 255, 204)'],
          'Assam': ['rgb(51, 51, 0)', 'rgb(77, 77, 0)', 'rgb(153, 153, 0)', 'rgb(230, 230, 0)',
                    'rgb(255, 255, 51)'],
          'Bihar': ['rgb(38, 77, 0)', 'rgb(51, 102, 0)', 'rgb(77, 153, 0)', 'rgb(115, 230, 0)',
                    'rgb(153, 255, 51)'],
          'Chandigarh': ['rgb(77, 51, 25)', 'rgb(116, 77, 37)', 'rgb(155, 102, 49)', 'rgb(194, 128, 61)',
                         'rgb(206, 153, 100)'],
          'Chhattisgarh': ['rgb(179, 0, 0)', 'rgb(255, 0, 0)', 'rgb(255, 51, 51)', 'rgb(255, 77, 77)',
                           'rgb(255, 153, 153)'],
          'Daman & Diu': ['rgb(0, 51, 17)', 'rgb(0, 102, 34)', 'rgb(0, 153, 51)', 'rgb(0, 204, 68)',
                          'rgb(102, 255, 153)'],
          'NCT of Delhi': ['rgb(51, 77, 77)', 'rgb(71, 107, 107)', 'rgb(92, 138, 138)', 'rgb(133, 173, 173)',
                           'rgb(179, 204, 204)'],
          'Goa': ['rgb(102, 0, 77)', 'rgb(153, 0, 115)', 'rgb(230, 0, 172)', 'rgb(255, 77, 210)',
                  'rgb(255, 179, 236)'],
          'Gujarat': ['rgb(51, 51, 204))', 'rgb(71, 71, 209)', 'rgb(112, 112, 219)', 'rgb(153, 153, 230)',
                      'rgb(193, 193, 240)'],
          'Haryana': ['rgb(0, 128, 96)', 'rgb(0, 179, 134)', 'rgb(0, 230, 172)', 'rgb(51, 255, 204)',
                      'rgb(179, 255, 236)'],
          'Himachal Pradesh': ['rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(204, 0, 68)', 'rgb(255, 0, 85)',
                               'rgb(255, 51, 119)'],
          'Jammu & Kashmir': ['rgb(57, 0, 77)', 'rgb(94, 0, 128)', 'rgb(131, 0, 179)', 'rgb(168, 0, 230)',
                              'rgb(207, 77, 255)'],
          'Jharkhand': ['rgb(71, 0, 179)', 'rgb(92, 0, 230)', 'rgb(117, 26, 255)', 'rgb(148, 77, 255)',
                        'rgb(194, 153, 255)'],
          'Karnataka': ['rgb(128, 128, 0)', 'rgb(179, 179, 0)', 'rgb(204, 204, 0)', 'rgb(255, 255, 0)',
                        'rgb(255, 255, 102)'],
          'Kerala': ['rgb(0, 102, 68)', 'rgb(0, 153, 102)', 'rgb(0, 204, 136)', 'rgb(26, 255, 178)',
                     'rgb(153, 255, 221)'],
          'Lakshadweep': ['rgb(230, 57, 0)', 'rgb(255, 64, 0)', 'rgb(255, 83, 26)', 'rgb(255, 102, 51)',
                          'rgb(255, 140, 102)'],
          'Madhya Pradesh': ['rgb(153, 153, 102)', 'rgb(173, 173, 133)', 'rgb(184, 184, 148)', 'rgb(194, 194, 163)',
                             'rgb(214, 214, 194)'],
          'Maharashtra': ['rgb(153, 0, 255)', 'rgb(163, 26, 255)', 'rgb(173, 51, 255)', 'rgb(194, 102, 255)',
                          'rgb(214, 153, 255)'],
          'Manipur': ['rgb(255, 0, 255)', 'rgb(255, 51, 255)', 'rgb(255, 102, 255)', 'rgb(255, 153, 255)',
                      'rgb(255, 230, 255)'],
          'Meghalaya': ['rgb(0, 204, 102)', 'rgb(0, 255, 132)', 'rgb(51, 255, 156)', 'rgb(102, 255, 181)',
                        'rgb(179, 255, 218)'],
          'Mizoram': ['rgb(255, 153, 0)', 'rgb(255, 173, 51)', 'rgb(255, 194, 102)', 'rgb(255, 214, 153)',
                      'rgb(255, 235, 204)'],
          'Nagaland': ['rgb(51, 204, 255)', 'rgb(77, 210, 255)', 'rgb(153, 230, 255)', 'rgb(204, 242, 255)',
                       'rgb(204, 242, 255)'],
          'Orissa': ['rgb(136, 136, 68)', 'rgb(170, 170, 85)', 'rgb(187, 187, 119)', 'rgb(204, 204, 153)',
                     'rgb(229, 229, 204)'],
          'Puducherry': ['rgb(0, 179, 134)', 'rgb(0, 230, 172)', 'rgb(26, 255, 198)', 'rgb(51, 255, 204)',
                         'rgb(153, 255, 230)'],
          'Punjab': ['rgb(0, 60, 179)', 'rgb(0, 77, 230)', 'rgb(26, 102, 255)', 'rgb(77, 136, 255)',
                     'rgb(179, 204, 255)'],
          'Rajasthan': ['rgb(0, 128, 0)', 'rgb(0, 204, 0)', 'rgb(0, 255, 0)', 'rgb(77, 255, 77)',
                        'rgb(153, 255, 153)'],
          'Sikkim': ['rgb(153, 153, 102)', 'rgb(163, 163, 117)', 'rgb(184, 184, 148)', 'rgb(204, 204, 179)',
                     'rgb(224, 224, 209)'],
          'Tamil Nadu': ['rgb(204, 102, 255)', 'rgb(221, 153, 255)', 'rgb(230, 179, 255)', 'rgb(238, 204, 255)',
                         'rgb(247, 230, 255)'],
          'Telangana': ['rgb(102, 0, 102)', 'rgb(153, 0, 153)', 'rgb(204, 0, 204)', 'rgb(255, 0, 255)',
                        'rgb(255, 128, 255)'],
          'Tripura': ['rgb(255, 255, 0)', 'rgb(255, 255, 51)', 'rgb(255, 255, 102)', 'rgb(255, 255, 128)',
                      'rgb(255, 255, 179)'],
          'Uttar Pradesh': ['rgb(0, 204, 204)', 'rgb(0, 255, 255)', 'rgb(51, 255, 255)', 'rgb(102, 255, 255)',
                            'rgb(179, 255, 255)'],
          'Uttarakhand': ['rgb(51, 153, 102)', 'rgb(64, 191, 128)', 'rgb(102, 204, 153)', 'rgb(140, 217, 179)',
                          'rgb(198, 236, 217)'],
          'West Bengal': ['rgb(51, 153, 51)', 'rgb(64, 191, 64)', 'rgb(121, 210, 121)', 'rgb(159, 223, 159)',
                          'rgb(198, 236, 198)']}

states_india = json.load(open("C:\\Users\\DELL\\Downloads\\india_states.geojson", 'r'))
state_id_map = {}
for feature in states_india["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("children_dataset.csv"))
df['id'] = df["states"].apply(lambda x: state_id_map[x])

all_states = df.states.unique()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

# cards
cardOne = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H4("TT IMMUNIZATION", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "Did you know that the majority of reported tetanus cases are birth-associated among newborn babies"
                    " and mothers who have not been sufficiently vaccinated with TTCV.", className="card-text",
                    style={"color": "rgb(250,250,250)"}
                ),
                html.Hr(className="my-2"),
                html.Div(
                    [
                        dbc.Button("ABOUT BAR CHART", id="open-offcanvas1", n_clicks=0),
                        dbc.Offcanvas(
                            html.P(
                                "Bar graphs are the pictorial representation of data (generally grouped), in the form of vertical or "
                                "horizontal rectangular bars, where the length of bars are proportional to the measure of data.The "
                                "bars drawn are of uniform width, and the variable quantity is represented on one of the axes. The bar chart in this dashboard"
                                "represent the BCG & TT immunization coverage percentage from the year 2015 to 2019.",
                                className="card-text", style={"font-family": "Consolas"}),
                            id="offcanvas1",
                            title="BAR CHART",
                            is_open=False,
                        ),
                    ]
                ),
                html.Hr(className="my-2"),
                dbc.CardLink("Click to learn more about Tetanus Toxoid", href="https://en.wikipedia.org/wiki/Tetanus_vaccine#:~:text=Tetanus%20vaccine%2C%20also%20known%20as,are%20recommended%20to%20maintain%20immunity."),
                html.Hr(className="my-2"),
                dcc.Dropdown(id='state-picker', options=[{'label': state, "value": state} for state in
                                                         df.states.unique()],
                             value='Andaman & Nicobar Island', clearable=False, style={"color": "#000000"}),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id='my-bar1', style={'padding': '12px', 'width': '60vw'})
                ),
            ]
        )
    ],
    style={"width": "60rem", "position": "center"}, color="dark",
)
cardTwo = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("BCG IMMUNIZATION", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "BCG vaccine has a documented protective effect against meningitis and disseminated TB in children",
                    className="card-text", style={"color": "rgb(250,250,250)"}
                ),
                dbc.CardLink("Click to learn more about BCG Vaccine", href="https://en.wikipedia.org/wiki/BCG_vaccine"),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id='my-bar2', style={'padding': '12px', 'width': '60vw'})
                ),
            ]
        )
    ],
    style={"width": "60rem", "position": "center"}, color="dark",
)

cardThree = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Vaccination Percentage Coverage in various states of INDIA over the years.",
                        className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "INDIA", className="card-text", style={"color": "rgb(250,250,250)"}
                ),
                html.Hr(className="my-2"),
                html.Div(
                    [
                        dbc.Button("ABOUT CHART", id="open-offcanvas2", n_clicks=0),
                        dbc.Offcanvas(
                            html.P(
                                "A line chart is a form of graphical representation of data in the form of points that are joined "
                                "continuously with the help of a line. Line charts are the simplest form of representing quantitative "
                                "data between two variables that are shown with the help of a line that can either be straight or "
                                "curved.The line chart here represents the vaccine percentage coverage of states of India from the year 2015 to 2019",
                                className="card-text", style={"font-family": "Consolas"}),
                            id="offcanvas2",
                            title="LINE CHART",
                            is_open=False,
                        ),
                    ]
                ),
                html.Hr(className="my-2"),
                dbc.CardLink("Click to learn more about vaccinations in India", href="https://en.wikipedia.org/wiki/Vaccination_in_India"),
                html.Hr(className="my-2"),
                dcc.Checklist(id="checklist", options=[{"label": x, "value": x}
                                                       for x in all_states],
                              value=all_states[36:], style={"color": "rgb(250,250,250)"},
                              labelStyle={'display': 'inline-block'}
                              ),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id="line-chart", style={'padding': '12px', 'width': '60vw'})
                ),
            ]
        )
    ],
    style={"width": "60rem", "position": "center"}, color="dark",
)

cardFour = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("INFANT MORTALITY", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "India is neither among the countries with the highest nor among those with the lowest infant "
                    "mortality rate",
                    className="card-text", style={"color": "rgb(250,250,250)"}
                ),
                html.Hr(className="my-2"),
                html.Div(
                    [
                        dbc.Button("ABOUT MAP", id="open-offcanvas3", n_clicks=0),
                        dbc.Offcanvas(
                            html.P(
                                "Choropleth Maps display divided geographical areas or regions that are coloured or shaded "
                                "in relation to a data variable.This provides a way to visualise values over a geographical area, "
                                "which can show patterns across the displayed location.The data variable uses colour "
                                "progression to represent itself in each region of the map. Here the map uses the infant mortality data"
                                "of various states from the year 2010 to 2019.",
                                className="card-text", style={"font-family": "Consolas"}),
                            id="offcanvas3",
                            title="CHOROPLETH MAP",
                            is_open=False,
                        ),
                    ]
                ),
                html.Hr(className="my-2"),
                dbc.CardLink("Click to learn more about Infant Mortality Rate (IMR)", href="https://en.wikipedia.org/wiki/Infant_mortality"),
                html.Hr(className="my-2"),
                dcc.Input(id='input_state', type='number', inputMode='numeric', value=2010,
                          max=2019, min=2010, step=1, required=True),
                html.Button(id='submit_button', n_clicks=0, children='Submit'),
                html.Div(id='output_state'),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id='my-choropleth', style={'padding': '12px', 'width': '60vw'})
                ),
            ]
        )
    ],
    style={"width": "60rem", "position": "center"}, color="dark"
)

sp = html.Br()
# rows
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
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardTwo)),

            ],
            style={'margin': 'auto', 'width': '68vw'}
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardThree)),

            ],
            style={'margin': 'auto', 'width': '68vw'}
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardFour)),

            ],
            style={'margin': 'auto', 'width': '68vw'}
        ),
    ], style={'backgroundColor': 'rgb(3, 16, 33)'}
)

#####################################################################################
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
