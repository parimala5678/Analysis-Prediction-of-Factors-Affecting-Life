import dash
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import folium
from folium import plugins
import pathlib


world = folium.Map(
    zoom_start=2,
    location=[20.5937, 78.9629])

world.save('world_empty.html')
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

immu_states = pd.read_csv(DATA_PATH.joinpath("immunization_status.csv"))

state = immu_states.iloc[3]
folium.Marker(
    location=[state['latitude'], state['longitude']],
).add_to(world)

world.save('world_some_states.html')
world_all_states_colored = folium.Map(
    zoom_start=2,
    location=[20.5937, 78.9629]
)

all_subgroups = folium.FeatureGroup(name='all details')
world_all_states_colored.add_child(all_subgroups)

# subgroup 1
total_vaccine = plugins.FeatureGroupSubGroup(all_subgroups, 'Total coverage')
world_all_states_colored.add_child(total_vaccine)

# subgroup 2
bcg_vaccine = plugins.FeatureGroupSubGroup(all_subgroups, 'Bcg vaccine')
world_all_states_colored.add_child(bcg_vaccine)

# subgroup 3
measles_vaccine = plugins.FeatureGroupSubGroup(all_subgroups, 'Measles vaccine')
world_all_states_colored.add_child(measles_vaccine)


def select_marker_color(row):
    if row['total_status'] == 'fully_covered':
        return 'red'
    elif row['total_status'] == 'partially_covered':
        return 'pink'
    return 'blue'


immu_states['colors'] = immu_states.apply(select_marker_color, axis=1)

world_all_states_colored_1 = folium.Map(
    zoom_start=2,
    location=[20.5937, 78.9629]
)

for _, state in immu_states.iterrows():
    folium.Marker(
        location=[state['latitude'], state['longitude']],
        popup=state['states'],
        tooltip=state['vaccination'],
        hover=state['states'],
        icon=folium.Icon(color=state['colors'], prefix='fa', icon='circle')
    ).add_to(total_vaccine)
folium.TileLayer('stamentoner').add_to(world_all_states_colored)
folium.TileLayer('openstreetmap').add_to(world_all_states_colored)
folium.TileLayer('stamenwatercolor').add_to(world_all_states_colored)
folium.TileLayer('cartodbdark_matter').add_to(world_all_states_colored)
folium.LayerControl().add_to(world_all_states_colored)


def select_marker_color(row1):
    if row1['BCG_status'] == 'fully_covered':
        return 'black'
    elif row1['BCG_status'] == 'partially_covered':
        return 'gray'
    return 'darkpurple'


immu_states['colors'] = immu_states.apply(select_marker_color, axis=1)

world_all_states_colored_2 = folium.Map(
    zoom_start=2,
    location=[20.5937, 78.9629]
)

for _, state in immu_states.iterrows():
    folium.Marker(
        location=[state['latitude'], state['longitude']],
        popup=state['states'],
        tooltip=state['vaccination'],
        hover=state['states'],
        icon=folium.Icon(color=state['colors'], prefix='fa', icon='circle')
    ).add_to(bcg_vaccine)


def select_marker_color(row2):
    if row2['Measles_status'] == 'fully_covered':
        return 'orange'
    elif row2['Measles_status'] == 'partially_covered':
        return 'cadetblue'
    return 'lightgreen'


immu_states['colors'] = immu_states.apply(select_marker_color, axis=1)

world_all_states_colored_3 = folium.Map(
    zoom_start=2,
    location=[20.5937, 78.9629]
)

for _, state in immu_states.iterrows():
    folium.Marker(
        location=[state['latitude'], state['longitude']],
        popup=state['states'],
        tooltip=state['vaccination'],
        hover=state['states'],
        icon=folium.Icon(color=state['colors'], prefix='fa', icon='circle')
    ).add_to(measles_vaccine)
world_all_states_colored.save('world_all_states_colored_updated.html')

app = dash.Dash(external_stylesheets=[dbc.themes.VAPOR])

cardOne = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("TOTAL VACCINATION COVERAGE ", className="card-title",
                        style={"color": "rgb(250,250,250)"}),
                html.P(
                    "Did you know that Immunization currently prevents 2-3 million deaths every year from diseases "
                    "like diphtheria, tetanus, pertussis, influenza and measles. We now have vaccines to prevent more "
                    "than 20 life-threatening diseases, helping people of all ages live longer, healthier lives",
                    className="card-text",
                    style={"color": "rgb(250,250,250)"}
                ),
                html.Hr(className="my-2"),
                html.Div(
                    [
                        dbc.Button("ABOUT FOLIUM MAP", id="open-offcanvas4", n_clicks=0),
                        dbc.Offcanvas(
                            html.P(
                                "Folium makes it easy to visualize data that’s been manipulated in Python on an "
                                "interactive leaflet map.It enables both the binding of data to a map for choropleth "
                                "visualizations as well as passing rich vector/raster/HTML visualizations as markers on "
                                "the map. The library has a number of built-in tilesets "
                                "from OpenStreetMap, Mapbox, and Stamen API keys.The folium map that is shown in the dashboard has tooltips for "
                                "different types of vaccinations as shown in the legend. But there are also colors "
                                "associated with the tooltips of the map. These colors represent various conditions "
                                "given as per the coverage percentage. If the vaccination coverage is higher than 95% "
                                "it is marked as fully covered. If the vaccination coverage is between 50% and 95% "
                                "it is marked as PARTIALLY COVERED. If the vaccination coverage is lower than 50% it is"
                                "marked as POORLY COVERED." 
                                "With respect to the Total Vaccination Data,Red represents Fully Covered status,Pink "
                                "Partially Covered status and "
                                " blue represents Poorly covered status. With respect to the Measles"
                                "vaccination Data Orange represents Fully Covered status, Cadet Blue represents "
                                "Partially Covered status and Light Green represents Poorly covered status."
                                "With respect to the BCG vaccination Data black represents Fully Covered status, Gray "
                                "represents Partially Covered status",
                                className="card-text", style={"font-family": "Consolas"}),
                            id="offcanvas4",
                            title="FOLIUM MAP",
                            is_open=False,
                        ),
                    ]
                ),
                html.Hr(className="my-2"),
                html.Div(
                    children=[
                        html.Iframe(src='/assets/world_all_states_colored_updated.html',
                                    style={"height": "1000px", "width": "100%"})
                    ]
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

app.layout = html.Div(
    [row])
