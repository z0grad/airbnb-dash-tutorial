
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import overview, price_analysis


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server
df = pd.read_csv('AB_NYC_2019_cleaned.csv')



app.layout = dbc.Container([    html.H1(children='Airbnb Listings in NYC', className='text-center mt-4'),
                                html.Hr(),

                                dbc.Tabs(
                                            [
                                                dbc.Tab(overview.overview_content, label="Overview"),
                                                dbc.Tab(price_analysis.price_analysis_content, label="Price Analysis"),
                                                dbc.Tab("This tab's content is never seen", label="Tab 3", disabled=True),
                                            ]
                                        )
                                ], fluid=True)

if __name__ == '__main__':
    app.run(port=8080)
