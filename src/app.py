# Dash app libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Importing app header & body from the other .py scripts
from appHeader import header
from appBody import body


# Creating app dash object                     # importing modern-looking buttons, tables, etc
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Building the app layout from header, body
app.layout = html.Div(
                id='main_page',
                children=[
                    header(),
                    body(),
                         ],
                     )


# App interactivity 1: top right About button
@app.callback(
    Output("popover", "is_open"),
    [Input("popover-target", "n_clicks")],
    [State("popover", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open



# Main function, runs the app
if __name__ == '__main__':
    app.run_server(debug=True)

