# Dash app libraries
import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import base64

# Making table quickly
import pandas as pd

# Listing manually all the apps created

derivatives = ["European option", 
               "European option",
               "Arithmetic Asian option",
               "Arithmetic Asian option",
               "Exchange option"]

models      = ["Black-Scholes-Merton",
               "Cox-Ross Rubinstein",
               "Cox-Ross Rubinstein" ,
               "Monte-Carlo simulation", 
               "Black-Scholes-Merton"]

URLs        = [html.A(html.P("eu-option-bsm"),href="https://eu-option-bsm.onrender.com", target="_blank"), 
               html.A(html.P('eu-option-crr'),href="https://eu-option-crr.onrender.com", target="_blank"), 
               html.A(html.P("asian-option-crr"),href='https://asian-option-crr.onrender.com', target="_blank"),
               html.A(html.P("asian-option-mc"),href='https://mc-asian-app.onrender.com', target="_blank"),  
               html.A(html.P("exchange-option-bsm"),href='https://exchange-option-bsm.onrender.com', target="_blank")]

authors     = ["Michel Vanderhulst",
               "Michel Vanderhulst",
               "Michel Vanderhulst",
               "Valentin Paquay",
               "Michel Vanderhulst"]

# Would be a nice addition, idk how to do it. I imagine getting from github the last commit date from each app?                
lastupdated = ["2021/01/04","2021/02/11","2021/02/11","2021/02/14"]

# Building the table fromm all apps info
dictionary={"Derivative":derivatives,"Model":models,"URL":URLs,"Author":authors}
df=pd.DataFrame(dictionary)

# making Dash table out of pandas table
table=dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

# Creating the app body
def body():
  return html.Div(children=[
            html.Div(id='left-column', children=[
                dcc.Tabs(
                    id='tabs', value='About this App',
                    children=[
                        dcc.Tab(
                            label='About this App',
                            value='About this App',
                            children=html.Div(children=[
                              html.Br(),
                                html.H4('What is this app?', style={"text-align":"center"}),
                                html.P(
                                    """
                                    This app lists a series of web applications for pricing derivatives. 
                                    """
                                      ),
                                html.P(
                                    """
                                    The applications developed by Michel Vanderhulst use visuals to illustrate investment strategies that replicate the derivatives prices, i.e. proving they are arbitrage-free.  
                                    """
                                      ),
                                html.P(
                                    """
                                    The application by Valentin Paquay illustrates the use of the Monte-Carlo method to calculate the price of a derivative, as well as the use of methods to improve accuracy.  
                                    """
                                      ),      
                                html.Br(),
                                html.P(
                                  """
                                  Note: the apps are turned off by default. Upon startup, it can take between 10 to 30 seconds to load. It will then run at full speed.
                                  """),
                                html.Br(),
                                html.Div(table)])
                                 ),
                        dcc.Tab(
                          label="Origin",
                          value="Origin",
                          children=[html.Div(children=[
                            html.Br(),
                            html.H4("Origin of apps", style={"text-align":"center"}),
                            html.P([
                              """
                              The 4 first web applications were done by Michel Vanderhulst in 2020/2021 for his Master's Thesis under the supervision of Prof. Frédéric Vrins.
                              Their goal is these application to be maintained and further enriched with other derivatives' replication strategies. 
                              """]),
                            html.P("""
                              The application using Monte-Carlo simulation was carried out by Valentin Paquay in 2022/2023, also for his Master's thesis under the supervision of Prof. Frédéric Vrins. 
                                The objective was to work on Monte-Carlo simulation and methods derived from it. 
                            """
                            ),
                            html.Br(),
                            html.P(["The source code of the 4 first apps can be found at ", html.A("github.com/MichelVanderhulst",href="https://github.com/MichelVanderhulst?tab=repositories", target="_blank"),"."]),
                            html.P(["The source code of the last app can be found at ", html.A("github.com/Vapaquay",href="https://github.com/Vapaquay?tab=repositories", target="_blank"), "."])
                            ])]),
                      #
                      #
                  
    ],),], style={"display":"flex", 'margin':"20px", 'transform':'translateX(+30%)', "width":"60%"}), 
  ])


