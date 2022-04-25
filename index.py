import dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from apps import children, first_page, total_coverage, others, alcohol_deaths, speed_deaths, suicides_scatter
import pathlib
import json
import plotly.express as px
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
server = app.server
token = 'pk.eyJ1IjoicGFyaW1hbGE1Njc4IiwiYSI6ImNsMDN1dnAzMzA3bGYzYm9nNTB6OXlrdnkifQ.ezumHt1etwfcMkRHuTe6FQ'
states_india = json.load(open("india_states.geojson", 'r'))
state_id_map = {}
for feature in states_india["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../Capstone/datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("children_dataset.csv"))
df2 = pd.read_csv(DATA_PATH.joinpath("Death_rate.csv"))
df3 = pd.read_csv(DATA_PATH.joinpath("alcohol_and_speed_deaths.csv"))
df4 = pd.read_csv(DATA_PATH.joinpath("suicides_dataset.csv"))
df['id'] = df["states"].apply(lambda x: state_id_map[x])
all_states = df.states.unique()

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("MAIN PAGE", href="/first_page"),
                ],
                nav=True,
                in_navbar=True,
                label="HOME",
                style={'font-weight': 'bold', 'color': 'white', "font-size": "20px"}
            ),
        ),
        dbc.NavItem(
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("STATS", href="/children"),
                ],
                nav=True,
                in_navbar=True,
                label="Children Statistics",
                style={'font-weight': 'bold', 'color': 'white', "font-size": "20px"}
            ),
        ),
        dbc.NavItem(
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Miscellaneous Factors", href="/others"),
                ],
                nav=True,
                in_navbar=True,
                label="Others Statistics",
                style={'font-weight': 'bold', 'color': 'white', "font-size": "20px"}
            ),
        ),
        dbc.NavItem(
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Coverage Info", href="/total_coverage"),
                ],
                nav=True,
                in_navbar=True,
                label="Vaccination Statistics",
                style={'font-weight': 'bold', 'color': 'white', "font-size": "20px"}
            ),
        ),
        dbc.NavItem(
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Accidents due to consumption of alcohol", href="/alcohol_deaths"),
                    dbc.DropdownMenuItem("Accidents due to over-speed", href="/speed_deaths"),
                    dbc.DropdownMenuItem("Suicides", href="/suicides_scatter"),
                ],
                nav=True,
                in_navbar=True,
                label="Accidental Deaths Statistics",
                style={'font-weight': 'bold', 'color': 'white', "font-size": "20px"}
            ),
        )
    ],
    brand="NavBar",
    color="dark",
    dark=True,
    className="mb-2",
)

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', children=[])
])


############################## FIRST PAGE ################################
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


##### OFF CANVAS ###
@app.callback(
    Output("offcanvas1", "is_open"),
    [Input("open-offcanvas1", "n_clicks")],
    [State("offcanvas1", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@app.callback(
    Output("offcanvas2", "is_open"),
    [Input("open-offcanvas2", "n_clicks")],
    [State("offcanvas2", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@app.callback(
    Output("offcanvas3", "is_open"),
    [Input("open-offcanvas3", "n_clicks")],
    [State("offcanvas3", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


# call back for folium map off-canvas
@app.callback(
    Output("offcanvas4", "is_open"),
    [Input("open-offcanvas4", "n_clicks")],
    [State("offcanvas4", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


# call back for children page graphs
@app.callback([Output("my-bar1", "figure"), Output("my-bar2", "figure")],
              [Input("state-picker", "value")]
              )
def update_bar_chart(state):
    colors1 = {
        'Andaman & Nicobar Island': ['rgb(0, 37, 77)', 'rgb(0, 51, 102)', 'rgb(0, 86, 179)', 'rgb(0, 111, 230)',
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
    mask = df["states"] == state
    fig = px.bar(df[mask], x='year', y='tt_immunization',
                 color='states', height=900, width=900)
    fig.update_traces(marker_color=colors1[state], marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)
    fig1 = px.bar(df[mask], x='year', y='bcg_immunization',
                  color='states', height=900, width=900)
    fig1.update_traces(marker_color=colors1[state], marker_line_color='rgb(8,48,107)',
                       marker_line_width=1.5, opacity=0.6)
    return fig, fig1


@app.callback(
    Output("line-chart", "figure"),
    [Input("checklist", "value")])
def update_line_chart(states):
    mask = df.states.isin(states)
    fig2 = px.line(df[mask],
                   x="year", y="Percentage_Coverage", color='states', markers=True)
    return fig2


######################### CHILDREN PAGE###################################
@app.callback(
    [Output('output_state', 'children'),
     Output(component_id='my-choropleth', component_property='figure')],
    [Input(component_id='submit_button', component_property='n_clicks')],
    [State(component_id='input_state', component_property='value')]
)
def update_chart(num_clicks, val_selected):
    if val_selected is None:
        raise PreventUpdate
    else:
        df1 = df.query('year=={}'.format(val_selected))
        fig3 = px.choropleth(df1, color='infant_mortality_rate', geojson=states_india, locations="id",
                             hover_data=['states'],
                             featureidkey="properties.state_code", projection="mercator",
                             title='infant mortality by state')
        fig3.update_geos(fitbounds="locations", visible=False)
        fig3.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return ('The input value was "{}" and the button has been \
                clicked {} times'.format(val_selected, num_clicks), fig3)


################################## OTHERS PAGE ###############################################################
@app.callback(Output("my-bar", "figure"),
              [Input("state-picker", "value")]
              )
def update_bar_chart(state):
    mask1 = df2["states"] == state
    fig = px.bar(df2[mask1], x='year', y='value', barmode='group', color='type', title="Grouped bar chart for "
                                                                                       "comparison "
                                                                                       "between Birth & Death Rate.")
    return fig


############# ALCOHOL DEATHS #############
@app.callback(Output("my-bar3", "figure"),
              [Input("state-picker", "value")]
              )
def update_bar_chart(state):
    colors = {
        'Andaman & Nicobar Island': ['rgb(0, 37, 77)', 'rgb(0, 37, 77)', 'rgb(0, 37, 77)', 'rgb(0, 37, 77)',
                                     'rgb(0, 37, 77)', 'rgb(0, 37, 77)', 'rgb(0, 37, 77)', 'rgb(0, 37, 77)',
                                     'rgb(0, 37, 77)', 'rgb(0, 37, 77)'],
        'Andhra Pradesh': ['rgb(153, 77, 0)', 'rgb(153, 77, 0)', 'rgb(153, 77, 0)', 'rgb(153, 77, 0)',
                           'rgb(153, 77, 0)', 'rgb(153, 77, 0)', 'rgb(153, 77, 0)', 'rgb(153, 77, 0)',
                           'rgb(153, 77, 0)', 'rgb(153, 77, 0)'],
        'Arunanchal Pradesh': ['rgb(0, 77, 0)', 'rgb(0, 77, 0)', 'rgb(0, 77, 0)', 'rgb(0, 77, 0)',
                               'rgb(0, 77, 0)',
                               'rgb(0, 77, 0)', 'rgb(0, 77, 0)', 'rgb(0, 77, 0)', 'rgb(0, 77, 0)',
                               'rgb(0, 77, 0)'],
        'Assam': ['rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)',
                  'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)'],
        'Bihar': ['rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)',
                  'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)'],
        'Chandigarh': ['rgb(77, 51, 25)', 'rgb(77, 51, 25)', 'rgb(77, 51, 25)', 'rgb(77, 51, 25)',
                       'rgb(77, 51, 25)',
                       'rgb(77, 51, 25)', 'rgb(77, 51, 25)', 'rgb(77, 51, 25)', 'rgb(77, 51, 25)',
                       'rgb(77, 51, 25)'],
        'Chhattisgarh': ['rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)',
                         'rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)',
                         'rgb(179, 0, 0)'],
        'Daman & Diu': ['rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)',
                        'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)'],
        'NCT of Delhi': ['rgb(51, 77, 77)', 'rgb(51, 77, 77)', 'rgb(51, 77, 77)', 'rgb(51, 77, 77)',
                         'rgb(51, 77, 77)', 'rgb(51, 77, 77)', 'rgb(51, 77, 77)', 'rgb(51, 77, 77)',
                         'rgb(51, 77, 77)', 'rgb(51, 77, 77)'],
        'Goa': ['rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)',
                'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)'],
        'Gujarat': ['rgb(51, 51, 204)', 'rgb(51, 51, 204)', 'rgb(51, 51, 204)', 'rgb(51, 51, 204)',
                    'rgb(51, 51, 204)', 'rgb(51, 51, 204)', 'rgb(51, 51, 204)', 'rgb(51, 51, 204)',
                    'rgb(51, 51, 204)', 'rgb(51, 51, 204)'],
        'Haryana': ['rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)',
                    'rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)',
                    'rgb(0, 128, 96)'],
        'Himachal Pradesh': ['rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(102, 0, 34)',
                             'rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(102, 0, 34)',
                             'rgb(102, 0, 34)', 'rgb(102, 0, 34)'],
        'Jammu & Kashmir': ['rgb(57, 0, 77)', 'rgb(57, 0, 77)', 'rgb(57, 0, 77)', 'rgb(57, 0, 77)',
                            'rgb(57, 0, 77)',
                            'rgb(57, 0, 77)', 'rgb(57, 0, 77)', 'rgb(57, 0, 77)', 'rgb(57, 0, 77)',
                            'rgb(57, 0, 77)'],
        'Jharkhand': ['rgb(71, 0, 179)', 'rgb(71, 0, 179)', 'rgb(71, 0, 179)', 'rgb(71, 0, 179)',
                      'rgb(71, 0, 179)',
                      'rgb(71, 0, 179)', 'rgb(71, 0, 179)', 'rgb(71, 0, 179)', 'rgb(71, 0, 179)',
                      'rgb(71, 0, 179)'],
        'Karnataka': ['rgb(128, 128, 0)', 'rgb(128, 128, 0)', 'rgb(128, 128, 0)', 'rgb(128, 128, 0)',
                      'rgb(128, 128, 0)', 'rgb(128, 128, 0)', 'rgb(128, 128, 0)', 'rgb(128, 128, 0)',
                      'rgb(128, 128, 0)', 'rgb(128, 128, 0)'],
        'Kerala': ['rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)',
                   'rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)',
                   'rgb(0, 102, 68)', ],
        'Lakshadweep': ['rgb(230, 57, 0)', 'rgb(230, 57, 0)', 'rgb(230, 57, 0)', 'rgb(230, 57, 0)',
                        'rgb(230, 57, 0)',
                        'rgb(230, 57, 0)', 'rgb(230, 57, 0)', 'rgb(230, 57, 0)', 'rgb(230, 57, 0)',
                        'rgb(230, 57, 0)', ],
        'Madhya Pradesh': ['rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)',
                           'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)',
                           'rgb(153, 153, 102)', ],
        'Maharashtra': ['rgb(153, 0, 255)', 'rgb(153, 0, 255)', 'rgb(153, 0, 255)', 'rgb(153, 0, 255)',
                        'rgb(153, 0, 255)', 'rgb(153, 0, 255)', 'rgb(153, 0, 255)', 'rgb(153, 0, 255)',
                        'rgb(153, 0, 255)', 'rgb(153, 0, 255)', ],
        'Manipur': ['rgb(255, 0, 255)', 'rgb(255, 0, 255)', 'rgb(255, 0, 255)', 'rgb(255, 0, 255)',
                    'rgb(255, 0, 255)', 'rgb(255, 0, 255)', 'rgb(255, 0, 255)', 'rgb(255, 0, 255)',
                    'rgb(255, 0, 255)', 'rgb(255, 0, 255)', ],
        'Meghalaya': ['rgb(0, 204, 102)', 'rgb(0, 204, 102)', 'rgb(0, 204, 102)', 'rgb(0, 204, 102)',
                      'rgb(0, 204, 102)', 'rgb(0, 204, 102)', 'rgb(0, 204, 102)', 'rgb(0, 204, 102)',
                      'rgb(0, 204, 102)', 'rgb(0, 204, 102)', ],
        'Mizoram': ['rgb(255, 153, 0)', 'rgb(255, 153, 0)', 'rgb(255, 153, 0)', 'rgb(255, 153, 0)',
                    'rgb(255, 153, 0)', 'rgb(255, 153, 0)', 'rgb(255, 153, 0)', 'rgb(255, 153, 0)',
                    'rgb(255, 153, 0)', 'rgb(255, 153, 0)', ],
        'Nagaland': ['rgb(51, 204, 255)', 'rgb(51, 204, 255)', 'rgb(51, 204, 255)', 'rgb(51, 204, 255)',
                     'rgb(51, 204, 255)', 'rgb(51, 204, 255)', 'rgb(51, 204, 255)', 'rgb(51, 204, 255)',
                     'rgb(51, 204, 255)', 'rgb(51, 204, 255)', ],
        'Orissa': ['rgb(136, 136, 68)', 'rgb(136, 136, 68)', 'rgb(136, 136, 68)', 'rgb(136, 136, 68)',
                   'rgb(136, 136, 68)', 'rgb(136, 136, 68)', 'rgb(136, 136, 68)', 'rgb(136, 136, 68)',
                   'rgb(136, 136, 68)', 'rgb(136, 136, 68)', ],
        'Puducherry': ['rgb(0, 179, 134)', 'rgb(0, 179, 134)', 'rgb(0, 179, 134)', 'rgb(0, 179, 134)',
                       'rgb(0, 179, 134)', 'rgb(0, 179, 134)', 'rgb(0, 179, 134)', 'rgb(0, 179, 134)',
                       'rgb(0, 179, 134)', 'rgb(0, 179, 134)'],
        'Punjab': ['rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)',
                   'rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)',
                   'rgb(0, 60, 179)', ],
        'Rajasthan': ['rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)',
                      'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', ],
        'Sikkim': ['rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)',
                   'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)',
                   'rgb(153, 153, 102)', 'rgb(153, 153, 102)', ],
        'Tamil Nadu': ['rgb(204, 102, 255)', 'rgb(204, 102, 255)', 'rgb(204, 102, 255)', 'rgb(204, 102, 255)',
                       'rgb(204, 102, 255)', 'rgb(204, 102, 255)', 'rgb(204, 102, 255)', 'rgb(204, 102, 255)',
                       'rgb(204, 102, 255)', 'rgb(204, 102, 255)', ],
        'Telangana': ['rgb(102, 0, 102)', 'rgb(102, 0, 102)', 'rgb(102, 0, 102)', 'rgb(102, 0, 102)',
                      'rgb(102, 0, 102)', 'rgb(102, 0, 102)', 'rgb(102, 0, 102)', 'rgb(102, 0, 102)',
                      'rgb(102, 0, 102)', 'rgb(102, 0, 102)', ],
        'Tripura': ['rgb(255, 255, 0)', 'rgb(255, 255, 0)', 'rgb(255, 255, 0)', 'rgb(255, 255, 0)',
                    'rgb(255, 255, 0)', 'rgb(255, 255, 0)', 'rgb(255, 255, 0)', 'rgb(255, 255, 0)',
                    'rgb(255, 255, 0)', 'rgb(255, 255, 0)', ],
        'Uttar Pradesh': ['rgb(0, 204, 204)', 'rgb(0, 204, 204)', 'rgb(0, 204, 204)', 'rgb(0, 204, 204)',
                          'rgb(0, 204, 204)', 'rgb(0, 204, 204)', 'rgb(0, 204, 204)', 'rgb(0, 204, 204)',
                          'rgb(0, 204, 204)', 'rgb(0, 204, 204)', ],
        'Uttarakhand': ['rgb(51, 153, 102)', 'rgb(51, 153, 102)', 'rgb(51, 153, 102)', 'rgb(51, 153, 102)',
                        'rgb(51, 153, 102)', 'rgb(51, 153, 102)', 'rgb(51, 153, 102)', 'rgb(51, 153, 102)',
                        'rgb(51, 153, 102)', 'rgb(51, 153, 102)', ],
        'West Bengal': ['rgb(51, 153, 51)', 'rgb(51, 153, 51)', 'rgb(51, 153, 51)', 'rgb(51, 153, 51)',
                        'rgb(51, 153, 51)', 'rgb(51, 153, 51)', 'rgb(51, 153, 51)', 'rgb(51, 153, 51)',
                        'rgb(51, 153, 51)', 'rgb(51, 153, 51)', ]}
    mask = df3["states"] == state
    fig3 = px.bar(df3[mask], x='year', y='alcohol_deaths',
                  color='states', height=900, width=900)
    fig3.update_traces(marker_color=colors[state], marker_line_color='rgb(8,48,107)',
                       marker_line_width=1.5, opacity=0.6)
    return fig3


###################### speed deaths ##############################
@app.callback(Output("my-bar4", "figure"),
              [Input("state-picker", "value")]
              )
def update_bar_chart(state):
    colors = {'Andaman & Nicobar Island': ['rgb(0, 37, 77)', 'rgb(0, 37, 77)', 'rgb(0, 37, 77)', 'rgb(0, 37, 77)',
                                           'rgb(0, 37, 77)', 'rgb(0, 37, 77)', 'rgb(0, 37, 77)', 'rgb(0, 37, 77)',
                                           'rgb(0, 37, 77)', 'rgb(0, 37, 77)'],
              'Andhra Pradesh': ['rgb(153, 77, 0)', 'rgb(153, 77, 0)', 'rgb(153, 77, 0)', 'rgb(153, 77, 0)',
                                 'rgb(153, 77, 0)', 'rgb(153, 77, 0)', 'rgb(153, 77, 0)', 'rgb(153, 77, 0)',
                                 'rgb(153, 77, 0)', 'rgb(153, 77, 0)'],
              'Arunanchal Pradesh': ['rgb(0, 77, 0)', 'rgb(0, 77, 0)', 'rgb(0, 77, 0)', 'rgb(0, 77, 0)',
                                     'rgb(0, 77, 0)',
                                     'rgb(0, 77, 0)', 'rgb(0, 77, 0)', 'rgb(0, 77, 0)', 'rgb(0, 77, 0)',
                                     'rgb(0, 77, 0)'],
              'Assam': ['rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)',
                        'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)', 'rgb(51, 51, 0)'],
              'Bihar': ['rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)',
                        'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)', 'rgb(38, 77, 0)'],
              'Chandigarh': ['rgb(77, 51, 25)', 'rgb(77, 51, 25)', 'rgb(77, 51, 25)', 'rgb(77, 51, 25)',
                             'rgb(77, 51, 25)',
                             'rgb(77, 51, 25)', 'rgb(77, 51, 25)', 'rgb(77, 51, 25)', 'rgb(77, 51, 25)',
                             'rgb(77, 51, 25)'],
              'Chhattisgarh': ['rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)',
                               'rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)', 'rgb(179, 0, 0)',
                               'rgb(179, 0, 0)'],
              'Daman & Diu': ['rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)',
                              'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)', 'rgb(0, 51, 17)'],
              'NCT of Delhi': ['rgb(51, 77, 77)', 'rgb(51, 77, 77)', 'rgb(51, 77, 77)', 'rgb(51, 77, 77)',
                               'rgb(51, 77, 77)', 'rgb(51, 77, 77)', 'rgb(51, 77, 77)', 'rgb(51, 77, 77)',
                               'rgb(51, 77, 77)', 'rgb(51, 77, 77)'],
              'Goa': ['rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)',
                      'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)', 'rgb(102, 0, 77)'],
              'Gujarat': ['rgb(51, 51, 204)', 'rgb(51, 51, 204)', 'rgb(51, 51, 204)', 'rgb(51, 51, 204)',
                          'rgb(51, 51, 204)', 'rgb(51, 51, 204)', 'rgb(51, 51, 204)', 'rgb(51, 51, 204)',
                          'rgb(51, 51, 204)', 'rgb(51, 51, 204)'],
              'Haryana': ['rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)',
                          'rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)', 'rgb(0, 128, 96)',
                          'rgb(0, 128, 96)'],
              'Himachal Pradesh': ['rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(102, 0, 34)',
                                   'rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(102, 0, 34)', 'rgb(102, 0, 34)',
                                   'rgb(102, 0, 34)', 'rgb(102, 0, 34)'],
              'Jammu & Kashmir': ['rgb(57, 0, 77)', 'rgb(57, 0, 77)', 'rgb(57, 0, 77)', 'rgb(57, 0, 77)',
                                  'rgb(57, 0, 77)',
                                  'rgb(57, 0, 77)', 'rgb(57, 0, 77)', 'rgb(57, 0, 77)', 'rgb(57, 0, 77)',
                                  'rgb(57, 0, 77)'],
              'Jharkhand': ['rgb(71, 0, 179)', 'rgb(71, 0, 179)', 'rgb(71, 0, 179)', 'rgb(71, 0, 179)',
                            'rgb(71, 0, 179)',
                            'rgb(71, 0, 179)', 'rgb(71, 0, 179)', 'rgb(71, 0, 179)', 'rgb(71, 0, 179)',
                            'rgb(71, 0, 179)'],
              'Karnataka': ['rgb(128, 128, 0)', 'rgb(128, 128, 0)', 'rgb(128, 128, 0)', 'rgb(128, 128, 0)',
                            'rgb(128, 128, 0)', 'rgb(128, 128, 0)', 'rgb(128, 128, 0)', 'rgb(128, 128, 0)',
                            'rgb(128, 128, 0)', 'rgb(128, 128, 0)'],
              'Kerala': ['rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)',
                         'rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)', 'rgb(0, 102, 68)',
                         'rgb(0, 102, 68)', ],
              'Lakshadweep': ['rgb(230, 57, 0)', 'rgb(230, 57, 0)', 'rgb(230, 57, 0)', 'rgb(230, 57, 0)',
                              'rgb(230, 57, 0)',
                              'rgb(230, 57, 0)', 'rgb(230, 57, 0)', 'rgb(230, 57, 0)', 'rgb(230, 57, 0)',
                              'rgb(230, 57, 0)', ],
              'Madhya Pradesh': ['rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)',
                                 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)',
                                 'rgb(153, 153, 102)', ],
              'Maharashtra': ['rgb(153, 0, 255)', 'rgb(153, 0, 255)', 'rgb(153, 0, 255)', 'rgb(153, 0, 255)',
                              'rgb(153, 0, 255)', 'rgb(153, 0, 255)', 'rgb(153, 0, 255)', 'rgb(153, 0, 255)',
                              'rgb(153, 0, 255)', 'rgb(153, 0, 255)', ],
              'Manipur': ['rgb(255, 0, 255)', 'rgb(255, 0, 255)', 'rgb(255, 0, 255)', 'rgb(255, 0, 255)',
                          'rgb(255, 0, 255)', 'rgb(255, 0, 255)', 'rgb(255, 0, 255)', 'rgb(255, 0, 255)',
                          'rgb(255, 0, 255)', 'rgb(255, 0, 255)', ],
              'Meghalaya': ['rgb(0, 204, 102)', 'rgb(0, 204, 102)', 'rgb(0, 204, 102)', 'rgb(0, 204, 102)',
                            'rgb(0, 204, 102)', 'rgb(0, 204, 102)', 'rgb(0, 204, 102)', 'rgb(0, 204, 102)',
                            'rgb(0, 204, 102)', 'rgb(0, 204, 102)', ],
              'Mizoram': ['rgb(255, 153, 0)', 'rgb(255, 153, 0)', 'rgb(255, 153, 0)', 'rgb(255, 153, 0)',
                          'rgb(255, 153, 0)', 'rgb(255, 153, 0)', 'rgb(255, 153, 0)', 'rgb(255, 153, 0)',
                          'rgb(255, 153, 0)', 'rgb(255, 153, 0)', ],
              'Nagaland': ['rgb(51, 204, 255)', 'rgb(51, 204, 255)', 'rgb(51, 204, 255)', 'rgb(51, 204, 255)',
                           'rgb(51, 204, 255)', 'rgb(51, 204, 255)', 'rgb(51, 204, 255)', 'rgb(51, 204, 255)',
                           'rgb(51, 204, 255)', 'rgb(51, 204, 255)', ],
              'Orissa': ['rgb(136, 136, 68)', 'rgb(136, 136, 68)', 'rgb(136, 136, 68)', 'rgb(136, 136, 68)',
                         'rgb(136, 136, 68)', 'rgb(136, 136, 68)', 'rgb(136, 136, 68)', 'rgb(136, 136, 68)',
                         'rgb(136, 136, 68)', 'rgb(136, 136, 68)', ],
              'Puducherry': ['rgb(0, 179, 134)', 'rgb(0, 179, 134)', 'rgb(0, 179, 134)', 'rgb(0, 179, 134)',
                             'rgb(0, 179, 134)', 'rgb(0, 179, 134)', 'rgb(0, 179, 134)', 'rgb(0, 179, 134)',
                             'rgb(0, 179, 134)', 'rgb(0, 179, 134)'],
              'Punjab': ['rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)',
                         'rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)', 'rgb(0, 60, 179)',
                         'rgb(0, 60, 179)', ],
              'Rajasthan': ['rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)',
                            'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', 'rgb(0, 128, 0)', ],
              'Sikkim': ['rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)',
                         'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)', 'rgb(153, 153, 102)',
                         'rgb(153, 153, 102)', 'rgb(153, 153, 102)', ],
              'Tamil Nadu': ['rgb(204, 102, 255)', 'rgb(204, 102, 255)', 'rgb(204, 102, 255)', 'rgb(204, 102, 255)',
                             'rgb(204, 102, 255)', 'rgb(204, 102, 255)', 'rgb(204, 102, 255)', 'rgb(204, 102, 255)',
                             'rgb(204, 102, 255)', 'rgb(204, 102, 255)', ],
              'Telangana': ['rgb(102, 0, 102)', 'rgb(102, 0, 102)', 'rgb(102, 0, 102)', 'rgb(102, 0, 102)',
                            'rgb(102, 0, 102)', 'rgb(102, 0, 102)', 'rgb(102, 0, 102)', 'rgb(102, 0, 102)',
                            'rgb(102, 0, 102)', 'rgb(102, 0, 102)', ],
              'Tripura': ['rgb(255, 255, 0)', 'rgb(255, 255, 0)', 'rgb(255, 255, 0)', 'rgb(255, 255, 0)',
                          'rgb(255, 255, 0)', 'rgb(255, 255, 0)', 'rgb(255, 255, 0)', 'rgb(255, 255, 0)',
                          'rgb(255, 255, 0)', 'rgb(255, 255, 0)', ],
              'Uttar Pradesh': ['rgb(0, 204, 204)', 'rgb(0, 204, 204)', 'rgb(0, 204, 204)', 'rgb(0, 204, 204)',
                                'rgb(0, 204, 204)', 'rgb(0, 204, 204)', 'rgb(0, 204, 204)', 'rgb(0, 204, 204)',
                                'rgb(0, 204, 204)', 'rgb(0, 204, 204)', ],
              'Uttarakhand': ['rgb(51, 153, 102)', 'rgb(51, 153, 102)', 'rgb(51, 153, 102)', 'rgb(51, 153, 102)',
                              'rgb(51, 153, 102)', 'rgb(51, 153, 102)', 'rgb(51, 153, 102)', 'rgb(51, 153, 102)',
                              'rgb(51, 153, 102)', 'rgb(51, 153, 102)', ],
              'West Bengal': ['rgb(51, 153, 51)', 'rgb(51, 153, 51)', 'rgb(51, 153, 51)', 'rgb(51, 153, 51)',
                              'rgb(51, 153, 51)', 'rgb(51, 153, 51)', 'rgb(51, 153, 51)', 'rgb(51, 153, 51)',
                              'rgb(51, 153, 51)', 'rgb(51, 153, 51)', ]}
    mask = df3["states"] == state
    fig4 = px.bar(df3[mask], x='year', y='speed_deaths',
                  color='states', height=900, width=900)
    fig4.update_traces(marker_color=colors[state], marker_line_color='rgb(8,48,107)',
                       marker_line_width=1.5, opacity=0.6)
    return fig4


@app.callback(
    [Output('output_state1', 'children'),
     Output(component_id='my-choropleth1', component_property='figure')],
    [Input(component_id='cause-picker1', component_property='value'),
     Input(component_id='submit_button1', component_property='n_clicks')],
    [State(component_id='input_state1', component_property='value')]
)
def update_chart(cause, num_clicks, val_selected):
    mask1 = df4["causes"] == cause
    if val_selected is None:
        raise PreventUpdate
    else:
        df7 = df4.query('year=={}'.format(val_selected))
        fig6 = px.scatter_mapbox(df7[mask1], color='total',
                                 lat="latitude",
                                 lon="longitude",
                                 color_continuous_scale=px.colors.sequential.Peach,
                                 size='total',
                                 center={"lat": 20.5937, "lon": 78.9629},
                                 zoom=4,
                                 opacity=1,
                                 title='Suicides by state')
        fig6.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
        fig6.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return ('The input value was "{}" and the button has been \
                clicked {} times'.format(val_selected, num_clicks), fig6)

############################ INDEX PAGE ################################################
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/children':
        return children.app.layout
    elif pathname == '/total_coverage':
        return total_coverage.app.layout
    elif pathname == '/others':
        return others.app.layout
    elif pathname == '/alcohol_deaths':
        return alcohol_deaths.app.layout
    elif pathname == '/speed_deaths':
        return speed_deaths.app.layout
    elif pathname == '/suicides_scatter':
        return suicides_scatter.app.layout
    else:
        return first_page.app.layout


if __name__ == '__main__':
    app.run_server(debug=True)
