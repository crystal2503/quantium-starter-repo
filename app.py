import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
df = pd.read_csv('output/pink_morsel_sales.csv')
df['date'] = pd.to_datetime(df['date'])
daily_sales = df.groupby('date')['sales'].sum().reset_index()
app = Dash(__name__)
app.layout = html.Div([
    html.H1('Soul Foods Pink Morsel Sales Visualiser'),
    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            daily_sales,
            x='date',
            y='sales',
            title='Daily Sales of Pink Morsels',
            labels={
                'date': 'Date',
                'sales': 'Sales (Total)'
            }
        )
    )
])
if __name__ == '__main__':
    app.run(debug=True)

