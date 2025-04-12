import plotly.express as px
import pandas as pd

df = pd.read_csv('AB_NYC_2019_cleaned.csv')



fig = px.scatter(df, x="latitude", y="longitude", color="neighbourhood_group", size="price",
                 hover_name="neighbourhood",  title="Airbnb Listings in NYC", template="plotly_dark")
fig.update_layout(
    xaxis=dict(showgrid=False),  # Disable gridlines for x-axis
    yaxis=dict(showgrid=False) ,  # Disable gridlines for y-axis
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot background
)


fig2 = px.pie(df, names='neighbourhood_group', title='Neighbourhood Group Distribution', hole=0.3, template="plotly_dark")
fig2.update_traces(textposition='inside', textinfo='percent+label')
fig2.update_layout(showlegend=False, # Hide legend
                   paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
                    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot background
                )  

fig3 = px.pie(df, names='room_type', title='Room Type Distribution', hole=0.3, template="plotly_dark")
fig3.update_traces(textposition='inside', textinfo='percent+label')
fig3.update_layout(showlegend=False, # Hide legend
                   paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
                 plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot background
            )  


fig4 = px.histogram(df, x="neighbourhood_group", y = "price", color="neighbourhood_group", title='Neighbourhood Distribution', template="plotly_dark")