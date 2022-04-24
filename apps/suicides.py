mapbox_access_token = 'pk.eyJ1IjoicGFyaW1hbGE1Njc4IiwiYSI6ImNsMDN1dnAzMzA3bGYzYm9nNTB6OXlrdnkifQ.ezumHt1etwfcMkRHuTe6FQ'
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

df = pd.read_csv('E:/CAPSTONE/ACCIDENTAL_DEATHS/suicides_dataset.csv')
blackbold = {'color': 'black', 'font-weight': 'bold'}
app = dash.Dash(__name__)

cardOne = dbc.Card(
    [
        dbc.CardBody(
            [
                html.Li("Bankruptcy or Indebtedness", className='circle',
                        style={'background': '#FFFFFF', 'color': 'black',
                               'list-style': 'none', 'text-indent': '17px'}),
                html.Li("Extra Marital Affairs", className='circle', style={'background': '#FF0000', 'color': 'black',
                                                                            'list-style': 'none',
                                                                            'text-indent': '17px'}),
                html.Li("Impotency", className='circle', style={'background': '#00FF00', 'color': 'black',
                                                                'list-style': 'none',
                                                                'text-indent': '17px'}),
                html.Li("AIDS", className='circle', style={'background': '#FFFF00', 'color': 'black',
                                                           'list-style': 'none',
                                                           'text-indent': '17px'}),
                html.Li("Cancer", className='circle', style={'background': '#00FFFF', 'color': 'black',
                                                             'list-style': 'none',
                                                             'text-indent': '17px'}),
                html.Li("Paralysis", className='circle', style={'background': '#FF00FF', 'color': 'black',
                                                                'list-style': 'none',
                                                                'text-indent': '17px'}),
                html.Li("Mental Illness", className='circle', style={'background': '#C0C0C0', 'color': 'black',
                                                                     'list-style': 'none',
                                                                     'text-indent': '17px'}),
                html.Li("Other Prolonged Illness", className='circle', style={'background': '#FFA500', 'color': 'black',
                                                                              'list-style': 'none',
                                                                              'text-indent': '17px'}),
                html.Li("Dowry Related Issues", className='circle', style={'background': '#FFD700', 'color': 'black',
                                                                           'list-style': 'none',
                                                                           'text-indent': '17px'}),
                html.Li("Divorce", className='circle', style={'background': '#F0E68C', 'color': 'black',
                                                              'list-style': 'none',
                                                              'text-indent': '17px'}),
                html.Li("Drug Abuse", className='circle', style={'background': '#808000', 'color': 'black',
                                                                 'list-style': 'none',
                                                                 'text-indent': '17px'}),
                html.Li("Failure in Examination", className='circle', style={'background': '#7CFC00', 'color': 'black',
                                                                             'list-style': 'none',
                                                                             'text-indent': '17px'}),
                html.Li("Fall in Social Reputation ", className='circle',
                        style={'background': '#ADFF2F', 'color': 'black',
                               'list-style': 'none',
                               'text-indent': '17px'}),
                html.Li("Family Problems", className='circle', style={'background': '#20B2AA', 'color': 'black',
                                                                      'list-style': 'none',
                                                                      'text-indent': '17px'}),
                html.Li("Family Problems", className='circle', style={'background': '#191970', 'color': 'black',
                                                                      'list-style': 'none',
                                                                      'text-indent': '17px'}),
                html.Li("Physical Abuse", className='circle', style={'background': '#6495ED', 'color': 'black',
                                                                     'list-style': 'none',
                                                                     'text-indent': '17px'}),
                html.Li("Poverty", className='circle', style={'background': '#9400D3', 'color': 'black',
                                                              'list-style': 'none',
                                                              'text-indent': '17px'}),
                html.Li("Professional or Career problem", className='circle',
                        style={'background': '#DDA0DD', 'color': 'black',
                               'list-style': 'none',
                               'text-indent': '17px'}),

                html.Li("Unemployment", className='circle', style={'background': '#FFE4C4', 'color': 'black',
                                                                   'list-style': 'none',
                                                                   'text-indent': '17px'}),
                html.Li("Causes Not Known", className='circle', style={'background': '#D2691E', 'color': 'black',
                                                                       'list-style': 'none',
                                                                       'text-indent': '17px'}),
            ], style={'border-bottom': 'solid 3px', 'border-color': '#FFE4B5', 'padding-top': '6px'}
        ),
        html.Hr(className="my-2"),
        html.Label(children=['CAUSES: '], style=blackbold),
        dcc.Checklist(id='cause_name',
                      options=[{'label': str(b), 'value': b} for b in sorted(df['cause'].unique())],
                      value=[b for b in sorted(df['cause'].unique())],
                      ),
        html.Hr(className="my-2"),
        html.Label(children=['YEAR: '], style=blackbold),
        dcc.RadioItems(id='year_type',
                       options=[
                           {'label': '2015', "value": 2015},
                           {'label': '2016', "value": 2016},
                           {'label': '2017', "value": 2017},
                           {'label': '2018', "value": 2018},
                           {'label': '2019', "value": 2019},
                       ],
                       value=2015
                       ),
        html.Hr(className="my-2"),
        html.Div([
            dcc.Graph(id='graph', config={'displayModeBar': False, 'scrollZoom': True},
                      style={'background': '#00FC87', 'padding-bottom': '2px', 'padding-left': '2px', 'height': '100vh'}
                      )
        ], className='nine columns'
        ),

    ], className='row'
)

app.layout = html.Div(
    [cardOne]
)

@app.callback(
    Output('graph', 'figure'),
    [Input('cause_name', 'value'),
     Input('year_type', 'value')]
)
def update_figure(chosen_cause, chosen_year):
    df_sub = df[(df['cause'].isin(chosen_cause))]

    # Create figure
    locations = [go.Scattermapbox(
        lon=df_sub['longitude'],
        lat=df_sub['latitude'],
        mode='markers',
        marker={'color': df_sub['color']},
        unselected={'marker': {'opacity': 1}},
        selected={'marker': {'opacity': 0.5, 'size': 25}},
    )]

    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision='foo',  # preserves state of figure/map after callback activated
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            title=dict(text="Where to Recycle My Stuff?", font=dict(size=50, color='green')),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=25,
                style='light',
                center=dict(
                    lat=20.5937,
                    lon=78.9629
                ),
                pitch=40,
            ),
        )
    }


if __name__ == '__main__':
    app.run_server(debug=False)
