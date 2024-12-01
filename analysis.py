import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
from dash import Dash,dcc,html,Input,Output
data = pd.read_csv('supply_chain_data.csv')
app = Dash(__name__)
server=app.server
sales_data=data.groupby('Product type')['Number of products sold'].sum().reset_index()
total_revenue=data.groupby('Shipping carriers')['Revenue generated'].sum().reset_index()
defect_rate=data.groupby('Product type')['Defect rates'].mean().reset_index()
app.layout=html.Div(
    style={'backgroundColor': '#000000', 'color': '#E50914', 'padding': '20px', 'font-family': 'Arial'},
    children=[html.H1("Problem Statement 1: the price of the product and revenue genereted by them",style={'text-align': 'center', 'color': '#E50914'}),
              dcc.Graph(figure=px.scatter(data,x='Price',y='Revenue generated',color='Product type',hover_data=['Number of products sold'],trendline='ols')),
              
              html.H2(" Problem statement 2:Analyze the sales by product type", style={'text-align': 'center', 'color': '#E50914'}),
              dcc.Graph(figure=px.pie(sales_data,values='Number of products sold',names='Product type',hover_data=['Number of products sold'],title='sales by product type')),
              
              html.H2("Problem statement 3:Find out the total revenue genereted from shipping carreiers", style={'text-align': 'center', 'color': '#E50914'}),
              dcc.Graph(figure=px.bar(total_revenue,x='Shipping carriers',y='Revenue generated',title="total revenue by shipping carriers")),
              
              html.H2("problem statement 4:Analyze the revenue generated by each Sku",style={'text-align': 'center', 'color': '#E50914'}),
              dcc.Graph(figure=px.line(data,x='SKU',y='Revenue generated',title='revenue generated by sku')),
              
              html.H2("problem statement 5:Analyze the order quantity of each Sku",style={'text-align': 'center', 'color': '#E50914'}),
              dcc.Graph(figure=px.bar(data,x='Shipping carriers',y='Shipping costs',title='shipping costs by carrier')),
              
              html.H2("problem statement 6:Find out the cost distribution by transportation mode",style={'text-align': 'center', 'color': '#E50914'}),
              dcc.Graph(figure=px.pie(data,values='Costs',names='Transportation modes',title='Cost distribution by transportation modes')),
              
              html.H2("problem statement 7:Analyzing the defect rate of the product during shipping",style={'text-align': 'center', 'color': '#E50914'}),
              dcc.Graph( figure=px.bar(defect_rate,x='Product type',y='Defect rates',title='Average defect rates by product type'))

              ]
    

)


if __name__ == '__main__':
    app.run_server(debug=True)
