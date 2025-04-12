import plotly.express as px
import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import graphs


df = pd.read_csv('AB_NYC_2019_cleaned.csv')


overview_content = dbc.Container([
    

dbc.Row([
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H3("Total Listings", className="card-title text-center"),
                html.H3(f"{df.shape[0]:,}", className="card-text text-center")
            ]),
            className="shadow-sm rounded-3"
        ), width=4
    ),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H3("Neighbourhood Groups", className="card-title text-center"),
                html.H3(f"{df.neighbourhood_group.nunique()}", className="card-text text-center")
            ]),
            className="shadow-sm rounded-3"
        ), width=4
    ),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H3("Total Neighbourhoods", className="card-title text-center"),
                html.H3(f"{df.neighbourhood.nunique()}", className="card-text text-center")
            ]),
            className="shadow-sm rounded-3"
        ), width=4
    ),
], className="mb-4"),


dcc.Graph(figure=graphs.fig ),

dbc.Row([
    dbc.Col(dcc.Graph(figure=graphs.fig2 ), width=6),
    dbc.Col(dcc.Graph(figure=graphs.fig3 ), width=6)
], align='center', className='mt-4')

], fluid=True)
