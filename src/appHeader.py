# Dash app libraries
import dash
from dash import html
import dash_bootstrap_components as dbc
import base64
import os

# Author parameters
bg_color="#506784",
font_color="#F3F6FA"
author = "Michel Vanderhulst"
emailAuthor = "michelvanderhulst@hotmail.com"
supervisor = "Prof. Frédéric Vrins"
emailSupervisor = "frederic.vrins@uclouvain.be"
logo1path = os.path.join(os.path.dirname(__file__), 'pictures', 'Logo_LSM.png')
logo1URL  = "https://uclouvain.be/en/faculties/lsm"
logo2path = "./pictures/1280px-NovaSBE_Logo.svg.png"
logo2URL  = "https://www2.novasbe.unl.pt/en/"

# Creating the app header
def header():
    return html.Div(
                id='app-page-header',
                children=[
                    html.Div(children=[
                                         html.A(id='lsm-logo', 
                                               children=[html.Img(style={'height':'6%', 'width':'6%'}, src='data:image/png;base64,{}'.format(base64.b64encode(open(f"{logo1path}", 'rb').read()).decode()))],
                                               href=f"{logo1URL}",
                                               target="_blank", #open link in new tab
                                               style={"margin-left":"10px"}
                                               ),

                                       html.Div(children=[html.H5("Derivatives replication strategies central hub"),
                                                          ],
                                                 style={"display":"inline-block", "font-family":'sans-serif', "transform":"translateY(+22%)", "margin-left":"40px"}),

                                       html.Div(children=[dbc.Button("About", id="popover-target", outline=True, style={"color":"white", 'border': 'solid 1px white'}),
                                                          dbc.Popover(children=[dbc.PopoverHeader("About"),
                                                                                dbc.PopoverBody(["Michel Vanderhulst",                             
                                                                                             f"\n michelvanderhulst@hotmail.com",
                                                                                              f"\n Valentin Paquay",
                                                                                              f"\n valentin.paquay1@gmail.com",
                                                                                               html.Hr(), 
                                                                                             f"This app was built for our Master's Thesis, under the supervision of {supervisor} ({emailSupervisor})."]),
                                                                                ],
                                                                       id="popover",
                                                                       is_open=False,
                                                                       target="popover-target"),
                                                          ],
                                                 style={"display":"inline-block", "font-family":"sans-serif", "transform":"translateY(+15%)", "marginLeft":"5%", "margin-right":"10px"}
                                                 ),

                                     # html.A(id="nova-logo",
                                     #        children=[html.Img(style={"height":"9%","width":"9%"}, src="data:image/png;base64,{}".format(base64.b64encode(open(f"{logo2path}","rb").read()).decode()))],
                                     #        href=f"{logo2URL}",
                                     #        target="_blank",                   
                                     #        style={}
                                     #        )                                       
                                      ]
                             )#,style={"display":"inline-block"}),  
                         ],
                style={
                    'background': bg_color,
                    'color': font_color,
                    "padding-bottom": "10px",
                    "padding-top":"-10px"
                }
            )
