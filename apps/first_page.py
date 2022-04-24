import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

cardOne = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="https://image.shutterstock.com/image-vector/cartoon-man-different-ages-life-260nw"
                            "-1112124896.jpg",
                        className="img-fluid rounded-start"
                    ),
                    className="col-md-4", style={'width': '25rem'},
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H1("LIFE EXPECTANCY ANALYSIS DASHBOARD", className="card-title",
                                    style={"color": "rgb(250,250,250)", "font-family": "Arial Black"}),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"width": "80rem", 'align': 'center'}, color="dark",
)

collapse = html.Div(
    [
        dbc.Button(
            "CLICK TO KNOW ABOUT DASHBOARD", outline=True, color="info",
            style={"font-size": '25px', "font-family": "sacramento"},
            id="collapse-button",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(
                [
                    html.P(
                        "➤	     𝘞𝘦 𝘢𝘳𝘦 𝘭𝘪𝘷𝘪𝘯𝘨 𝘪𝘯 𝘢𝘯 𝘶𝘯𝘱𝘳𝘦𝘤𝘦𝘥𝘦𝘯𝘵𝘦𝘥 𝘦𝘱𝘰𝘤𝘩 𝘪𝘯 𝘸𝘩𝘪𝘤𝘩 "
                        "𝘩𝘶𝘮𝘢𝘯𝘴 𝘢𝘳𝘦 𝘦𝘪𝘵𝘩𝘦𝘳 𝘭𝘪𝘷𝘪𝘯𝘨 𝘭𝘰𝘯𝘨𝘦𝘳 𝘭𝘪𝘷𝘦𝘴 𝘰𝘳 𝘥𝘺𝘪𝘯𝘨 "
                        "𝘺𝘰𝘶𝘯𝘨𝘦𝘳 𝘭𝘪𝘷𝘦𝘴. 𝘏𝘶𝘮𝘢𝘯 𝘣𝘦𝘩𝘢𝘷𝘪𝘰𝘶𝘳 𝘢𝘯𝘥 𝘢𝘤𝘵𝘪𝘷𝘪𝘵𝘪𝘦𝘴 𝘢𝘳𝘦 "
                        "𝘴𝘰 𝘷𝘢𝘳𝘪𝘦𝘥 𝘵𝘩𝘢𝘵 𝘪𝘵 𝘪𝘴 𝘱𝘳𝘢𝘤𝘵𝘪𝘤𝘢𝘭𝘭𝘺 𝘩𝘢𝘳𝘥 𝘵𝘰 𝘮𝘦𝘢𝘴𝘶𝘳𝘦, "
                        "𝘤𝘢𝘵𝘦𝘨𝘰𝘳𝘪𝘴𝘦, 𝘢𝘯𝘥 𝘱𝘳𝘦𝘥𝘪𝘤𝘵 𝘭𝘪𝘧𝘦𝘴𝘱𝘢𝘯. 𝘛𝘩𝘦 𝘥𝘢𝘴𝘩𝘣𝘰𝘢𝘳𝘥 "
                        "𝘧𝘰𝘳 𝘭𝘪𝘧𝘦 𝘦𝘹𝘱𝘦𝘤𝘵𝘢𝘯𝘤𝘺 𝘢𝘯𝘢𝘭𝘺𝘴𝘪𝘴 𝘴𝘦𝘦𝘬𝘴 𝘵𝘰 𝘱𝘳𝘰𝘷𝘪𝘥𝘦 𝘵𝘩𝘦 "
                        "𝘦𝘴𝘴𝘦𝘯𝘵𝘪𝘢𝘭 𝘢𝘴𝘱𝘦𝘤𝘵𝘴 𝘢𝘯𝘥 𝘷𝘢𝘳𝘪𝘢𝘣𝘭𝘦𝘴 𝘵𝘩𝘢𝘵 𝘤𝘰𝘯𝘵𝘳𝘪𝘣𝘶𝘵𝘦 "
                        "𝘵𝘰 𝘭𝘪𝘧𝘦 𝘦𝘹𝘱𝘦𝘤𝘵𝘢𝘯𝘤𝘺. 𝘐𝘵 𝘪𝘴 𝘤𝘳𝘪𝘵𝘪𝘤𝘢𝘭 𝘵𝘰 𝘶𝘯𝘥𝘦𝘳𝘴𝘵𝘢𝘯𝘥 𝘢 "
                        "𝘴𝘵𝘢𝘵𝘦'𝘴 𝘰𝘳 𝘤𝘰𝘶𝘯𝘵𝘳𝘺'𝘴 𝘭𝘪𝘧𝘦 𝘦𝘹𝘱𝘦𝘤𝘵𝘢𝘯𝘤𝘺 𝘦𝘴𝘵𝘪𝘮𝘢𝘵𝘦𝘴 "
                        "𝘣𝘦𝘤𝘢𝘶𝘴𝘦 𝘵𝘩𝘦𝘺 𝘩𝘢𝘷𝘦 𝘵𝘩𝘦 𝘢𝘣𝘪𝘭𝘪𝘵𝘺 𝘵𝘰 𝘣𝘦𝘯𝘦𝘧𝘪𝘵 "
                        "𝘪𝘯𝘥𝘪𝘷𝘪𝘥𝘶𝘢𝘭𝘴, 𝘩𝘦𝘢𝘭𝘵𝘩-𝘤𝘢𝘳𝘦 𝘱𝘳𝘰𝘧𝘦𝘴𝘴𝘪𝘰𝘯𝘢𝘭𝘴, "
                        "𝘢𝘯𝘥 𝘨𝘰𝘷𝘦𝘳𝘯𝘮𝘦𝘯𝘵𝘴.",
                        className="card-text", style={"font-family": "Consolas", "font-size": '20px'}),
                    dbc.CardImg(
                        src='https://brifly-media.s3.ap-south-1.amazonaws.com/s3fs-public/article/2020-10/life-expectancy.png',
                        className='align-self-center',
                        style={"height": "20vw", "width": "25rem"}
                    ),
                    html.P(
                        "➤ 𝘐𝘵 𝘪𝘴 𝘤𝘰𝘮𝘮𝘰𝘯𝘭𝘺 𝘳𝘦𝘤𝘰𝘨𝘯𝘪𝘴𝘦𝘥 𝘵𝘩𝘢𝘵 𝘢 𝘱𝘦𝘳𝘴𝘰𝘯'𝘴 𝘭𝘪𝘧𝘦 "
                        "𝘴𝘱𝘢𝘯 𝘪𝘴 𝘪𝘯𝘧𝘭𝘶𝘦𝘯𝘤𝘦𝘥 𝘣𝘺 𝘢 𝘯𝘶𝘮𝘣𝘦𝘳 𝘰𝘧 𝘧𝘢𝘤𝘵𝘰𝘳𝘴, "
                        "𝘪𝘯𝘤𝘭𝘶𝘥𝘪𝘯𝘨 𝘨𝘦𝘰𝘨𝘳𝘢𝘱𝘩𝘪𝘤𝘢𝘭 𝘷𝘢𝘳𝘪𝘢𝘯𝘤𝘦𝘴, 𝘦𝘤𝘰𝘯𝘰𝘮𝘪𝘤 "
                        "𝘴𝘪𝘵𝘶𝘢𝘵𝘪𝘰𝘯𝘴, 𝘨𝘦𝘯𝘥𝘦𝘳 𝘥𝘪𝘴𝘱𝘢𝘳𝘪𝘵𝘪𝘦𝘴, 𝘮𝘦𝘯𝘵𝘢𝘭 𝘥𝘪𝘴𝘦𝘢𝘴𝘦𝘴, "
                        "𝘱𝘩𝘺𝘴𝘪𝘤𝘢𝘭 𝘪𝘭𝘭𝘯𝘦𝘴𝘴𝘦𝘴, 𝘦𝘥𝘶𝘤𝘢𝘵𝘪𝘰𝘯, 𝘺𝘦𝘢𝘳 𝘰𝘧 𝘣𝘪𝘳𝘵𝘩, "
                        "𝘢𝘯𝘥 𝘰𝘵𝘩𝘦𝘳 𝘥𝘦𝘮𝘰𝘨𝘳𝘢𝘱𝘩𝘪𝘤 𝘤𝘩𝘢𝘳𝘢𝘤𝘵𝘦𝘳𝘪𝘴𝘵𝘪𝘤𝘴. 𝘈𝘴 𝘢 "
                        "𝘳𝘦𝘴𝘶𝘭𝘵, 𝘐 𝘦𝘷𝘢𝘭𝘶𝘢𝘵𝘦𝘥 𝘢 𝘸𝘪𝘥𝘦 𝘷𝘢𝘳𝘪𝘦𝘵𝘺 𝘰𝘧 𝘦𝘭𝘦𝘮𝘦𝘯𝘵𝘴 "
                        "𝘵𝘩𝘢𝘵 𝘪𝘯𝘧𝘭𝘶𝘦𝘯𝘤𝘦 𝘢𝘯 𝘪𝘯𝘥𝘪𝘷𝘪𝘥𝘶𝘢𝘭'𝘴 𝘭𝘪𝘧𝘦𝘴𝘱𝘢𝘯. 𝘛𝘩𝘪𝘴 "
                        "𝘥𝘢𝘴𝘩𝘣𝘰𝘢𝘳𝘥 𝘯𝘰𝘵 𝘰𝘯𝘭𝘺 𝘰𝘧𝘧𝘦𝘳𝘴 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯 𝘳𝘦𝘨𝘢𝘳𝘥𝘪𝘯𝘨 "
                        "𝘯𝘢𝘵𝘶𝘳𝘢𝘭 𝘧𝘢𝘵𝘢𝘭𝘪𝘵𝘪𝘦𝘴 𝘪𝘯 𝘢 𝘴𝘵𝘢𝘵𝘦, 𝘣𝘶𝘵 𝘪𝘵 𝘢𝘭𝘴𝘰 "
                        "𝘪𝘯𝘤𝘭𝘶𝘥𝘦𝘴 𝘢𝘯𝘢𝘭𝘺𝘴𝘦𝘴 𝘰𝘧 𝘢𝘤𝘤𝘪𝘥𝘦𝘯𝘵𝘢𝘭 𝘥𝘦𝘢𝘵𝘩𝘴 𝘵𝘩𝘢𝘵 "
                        "𝘰𝘤𝘤𝘶𝘳𝘳𝘦𝘥 𝘰𝘷𝘦𝘳 𝘢 𝘴𝘱𝘦𝘤𝘪𝘧𝘪𝘤 𝘵𝘪𝘮𝘦 𝘱𝘦𝘳𝘪𝘰𝘥.",
                        style={"font-family": "Consolas", "font-size": '20px'}
                    ),
                    dbc.Row(
                        [
                            dbc.Col(dbc.CardImg(
                                src='https://thumbs.gfycat.com/UniqueSizzlingFinwhale-max-1mb.gif',
                                style={"height": "13vw", "width": "20rem"}
                            )),
                            dbc.Col(
                                dbc.CardBody(
                                    [
                                        html.H1("WHY ACCIDENTAL DEATHS....?", className="card-title",
                                                style={"color": "rgb(250,250,250)", "font-family": "Rouge Script"}),
                                    ]
                                ),
                                className="col-md-8",
                            ),
                            html.P(
                                "➤                𝘛𝘩𝘪𝘴 𝘥𝘢𝘴𝘩𝘣𝘰𝘢𝘳𝘥 𝘪𝘯𝘤𝘭𝘶𝘥𝘦𝘴 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯 "
                                "𝘳𝘦𝘨𝘢𝘳𝘥𝘪𝘯𝘨 𝘧𝘪𝘳𝘦 𝘪𝘯𝘤𝘪𝘥𝘦𝘯𝘵𝘴 (𝘵𝘰𝘨𝘦𝘵𝘩𝘦𝘳 𝘸𝘪𝘵𝘩 𝘵𝘩𝘦 "
                                "𝘭𝘰𝘤𝘢𝘵𝘪𝘰𝘯 𝘰𝘧 𝘵𝘩𝘦 𝘰𝘤𝘤𝘶𝘳𝘳𝘦𝘯𝘤𝘦), 𝘳𝘰𝘢𝘥 𝘢𝘤𝘤𝘪𝘥𝘦𝘯𝘵𝘴 "
                                "𝘤𝘢𝘶𝘴𝘦𝘥 𝘣𝘺 𝘢𝘭𝘤𝘰𝘩𝘰𝘭 𝘶𝘴𝘦, 𝘢𝘯𝘥 𝘴𝘱𝘦𝘦𝘥𝘪𝘯𝘨 𝘢𝘴 𝘱𝘢𝘳𝘵 "
                                "𝘰𝘧 𝘵𝘩𝘦 𝘢𝘤𝘤𝘪𝘥𝘦𝘯𝘵𝘢𝘭 𝘥𝘦𝘢𝘵𝘩𝘴. 𝘐 𝘢𝘭𝘴𝘰 𝘦𝘷𝘢𝘭𝘶𝘢𝘵𝘦𝘥 "
                                "𝘵𝘩𝘦 𝘴𝘶𝘪𝘤𝘪𝘥𝘦𝘴 𝘥𝘢𝘵𝘢𝘴𝘦𝘵, 𝘪𝘯 𝘰𝘳𝘥𝘦𝘳 𝘵𝘰 𝘢𝘴𝘴𝘪𝘴𝘵 "
                                "𝘶𝘴𝘦𝘳𝘴 𝘪𝘯 𝘱𝘳𝘰𝘷𝘪𝘥𝘪𝘯𝘨 𝘨𝘳𝘦𝘢𝘵𝘦𝘳 𝘪𝘯𝘴𝘪𝘨𝘩𝘵𝘴 𝘪𝘯𝘵𝘰 "
                                "𝘵𝘩𝘦 𝘤𝘢𝘶𝘴𝘦𝘴 (𝘵𝘩𝘦 𝘥𝘢𝘵𝘢 𝘤𝘰𝘯𝘵𝘢𝘪𝘯𝘴 𝘵𝘩𝘦 𝘳𝘦𝘢𝘴𝘰𝘯 𝘧𝘰𝘳 "
                                "𝘴𝘶𝘪𝘤𝘪𝘥𝘦) 𝘧𝘰𝘳 𝘴𝘶𝘪𝘤𝘪𝘥𝘦𝘴 𝘪𝘯 𝘐𝘯𝘥𝘪𝘢. 𝘛𝘩𝘪𝘴 𝘪𝘴 "
                                "𝘴𝘪𝘨𝘯𝘪𝘧𝘪𝘤𝘢𝘯𝘵 𝘴𝘪𝘯𝘤𝘦 𝘢𝘤𝘤𝘪𝘥𝘦𝘯𝘵𝘴 𝘢𝘳𝘦 "
                                "𝘶𝘯𝘱𝘳𝘦𝘥𝘪𝘤𝘵𝘢𝘣𝘭𝘦 𝘢𝘯𝘥 𝘤𝘢𝘯 𝘭𝘦𝘢𝘷𝘦 𝘧𝘢𝘮𝘪𝘭𝘺 𝘮𝘦𝘮𝘣𝘦𝘳𝘴 "
                                "𝘪𝘯 𝘢 𝘥𝘪𝘭𝘦𝘮𝘮𝘢 𝘸𝘩𝘦𝘯 𝘢 𝘥𝘦𝘢𝘵𝘩 𝘤𝘰𝘮𝘦𝘴 "
                                "𝘶𝘯𝘦𝘹𝘱𝘦𝘤𝘵𝘦𝘥𝘭𝘺. 𝘚𝘰, 𝘪𝘯 𝘰𝘳𝘥𝘦𝘳 𝘵𝘰 𝘣𝘦𝘵𝘵𝘦𝘳 "
                                "𝘶𝘯𝘥𝘦𝘳𝘴𝘵𝘢𝘯𝘥 𝘵𝘩𝘦 𝘵𝘳𝘦𝘯𝘥𝘴 𝘰𝘧 𝘴𝘶𝘤𝘩 𝘶𝘯𝘦𝘹𝘱𝘦𝘤𝘵𝘦𝘥 "
                                "𝘪𝘯𝘤𝘪𝘥𝘦𝘯𝘵𝘴 𝘢𝘯𝘥 𝘱𝘳𝘰𝘷𝘪𝘥𝘦 𝘣𝘦𝘵𝘵𝘦𝘳 𝘪𝘯𝘴𝘪𝘨𝘩𝘵𝘴 𝘵𝘰 "
                                "𝘵𝘩𝘦 𝘨𝘰𝘷𝘦𝘳𝘯𝘮𝘦𝘯𝘵 𝘢𝘯𝘥 𝘤𝘪𝘵𝘪𝘻𝘦𝘯𝘴, 𝘵𝘩𝘪𝘴 𝘢𝘯𝘢𝘭𝘺𝘴𝘪𝘴 "
                                "𝘸𝘪𝘭𝘭 𝘢𝘭𝘴𝘰 𝘢𝘴𝘴𝘪𝘴𝘵 𝘪𝘯 𝘳𝘦𝘤𝘰𝘮𝘮𝘦𝘯𝘥𝘪𝘯𝘨 𝘵𝘰 "
                                "𝘥𝘪𝘧𝘧𝘦𝘳𝘦𝘯𝘵 𝘴𝘵𝘢𝘵𝘦𝘴 𝘸𝘩𝘪𝘤𝘩 𝘢𝘴𝘱𝘦𝘤𝘵𝘴 𝘰𝘧 "
                                "𝘢𝘤𝘤𝘪𝘥𝘦𝘯𝘵𝘢𝘭 𝘥𝘦𝘢𝘵𝘩𝘴 𝘴𝘩𝘰𝘶𝘭𝘥 𝘣𝘦 𝘱𝘳𝘪𝘰𝘳𝘪𝘵𝘪𝘴𝘦𝘥 𝘪𝘯 "
                                "𝘰𝘳𝘥𝘦𝘳 𝘵𝘰 𝘪𝘮𝘱𝘳𝘰𝘷𝘦 𝘵𝘩𝘦 𝘭𝘪𝘧𝘦 𝘦𝘹𝘱𝘦𝘤𝘵𝘢𝘯𝘤𝘺 𝘰𝘧 𝘪𝘵𝘴 "
                                "𝘱𝘦𝘰𝘱𝘭𝘦. 𝘈𝘴 𝘢 𝘳𝘦𝘴𝘶𝘭𝘵, 𝘐 𝘤𝘰𝘯𝘴𝘪𝘥𝘦𝘳𝘦𝘥 𝘵𝘩𝘦𝘮.",
                                style={"font-family": "Consolas", "font-size": '20px'})
                        ],
                    )
                ],
            ),
            id="collapse",
            is_open=False,
        ),
    ],
    className="d-grid gap-2 mb-4",
)
heading = html.H1("Glimpse About the Dashboard ⬇",
                  style={"color": "rgb(250,250,250)", "font-family": "Segoe Print", "font-size": "40px",
                         "text-decoration": "underline"}, className="text-center")

carousel = dbc.Col([
    dbc.Carousel(
        items=[
            {"key": "1",
             "src": "https://apexcharts.com/media/vue-chart-updation.gif",
             "caption": "My cat captions", "img_style": {"max-height": "400px", "width": "4"}},
            {"key": "2",
             "src": "https://gifimage.net/wp-content/uploads/2018/11/gif-graph-4.gif",
             "header": "My cat header", "img_style": {"max-height": "700px", "width": "4"}},
            {"key": "3",
             "src": "https://miro.medium.com/max/1400/1*yKI8QPzYKNWuHvn5Demndw.gif",
             "img_style": {"max-height": "400px", "width": "4"}},
            {"key": "4",
             "src": "https://cdn.analyticsvidhya.com/wp-content/uploads/2020/04/ft-v4.gif",
             "img_style": {"max-height": "400px", "width": "4"}},
            {"key": "5",
             "src": "https://datatricks.co.uk/wp-content/uploads/2020/07/scatter-chart-d3-animated.gif",
             "img_style": {"max-height": "400px", "width": "4"}},

        ],
        controls=True,
        indicators=True,
        interval=2000,
        ride="carousel",
    ),
],
    width=6)

row = html.Div(
    [

        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardOne),
                        width="auto"
                        )

            ],
            justify='center'
            # style={'margin': 'auto'},
        ),
    ], style={'backgroundColor': 'rgb(3, 16, 33)'}
)

row2 = html.Div(
    [

        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(carousel),
                        width="10"
                        )

            ],
            justify='center'
            # style={},
        ),
    ], style={'backgroundColor': 'rgb(3, 16, 33)','margin': 'auto',"offset":"1rem"}
)

app.layout = html.Div(
    [row, collapse, heading, row2]
)
