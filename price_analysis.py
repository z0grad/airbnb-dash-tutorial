import plotly.express as px
import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import graphs


df = pd.read_csv('AB_NYC_2019_cleaned.csv')


price_analysis_content = dbc.Container([
    

dbc.Row([
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H3("Avg Price", className="card-title text-center"),
                html.H3(f"{df.price.mean():.2f}", className="card-text text-center")
            ]),
            className="shadow-sm rounded-3"
        ), width=4
    ),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H3("Min Price", className="card-title text-center"),
                html.H3(f"{df.price.min():.2f}", className="card-text text-center")
            ]),
            className="shadow-sm rounded-3"
        ), width=4
    ),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H3("Max Price", className="card-title text-center"),
                html.H3(f"{df.price.max():.2f}", className="card-text text-center")
            ]),
            className="shadow-sm rounded-3"
        ), width=4
    ),
], className="mb-4"),


dcc.Graph(figure=graphs.fig4 ),
], fluid=True)

