# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd



df = pd.read_csv("formatted_data.csv")
app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


app.layout = html.Div([
    html.H1("Formatted sales data visualization"),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'sales', 
             'value': 'sales'},
        ],

        value = 'sales'
    ),
    dcc.Graph(id='line-chart')
])

@app.callback(
    Output('line-chart', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_chart(selected_metric):
    if selected_metric not in df.columns:
        return px.line(title="Invalid metric selected")


    fig =px.line(df, x='sales',
                 y=selected_metric,
                 title=f'''data viz:
                 {selected_metric.replace("_", "")}''')
    fig.update_layout(xaxis_title='date',
                      yaxis_title=selected_metric.replace("_", ""))
    return fig
if __name__ == '__main__':
    app.run(debug=True)
