import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv('output/pink_morsel_sales.csv')

# Convert date column to datetime for sorting
df['date'] = pd.to_datetime(df['date'])

app = Dash(__name__)

# Available regions plus 'all'
regions = ['north', 'east', 'south', 'west', 'all']

app.layout = html.Div(
    style={'font-family': 'Arial, sans-serif', 'max-width': '800px', 'margin': 'auto', 'padding': '20px'}, children=[

        # Header with styling
        html.H1('Soul Foods Pink Morsel Sales Visualiser', style={
            'text-align': 'center',
            'color': '#4B0082',
            'margin-bottom': '40px'
        }),

        # Radio buttons for region filter
        html.Div([
            html.Label('Select Region:', style={'font-weight': 'bold', 'margin-right': '10px'}),
            dcc.RadioItems(
                id='region-radio',
                options=[{'label': r.title(), 'value': r} for r in regions],
                value='all',
                inline=True,
                inputStyle={'margin-right': '5px', 'margin-left': '15px'}
            )
        ], style={'text-align': 'center', 'margin-bottom': '30px'}),

        # Line chart container
        dcc.Graph(id='sales-line-chart')
    ])


# Callback to update chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region.lower()]

    # Aggregate sales by date
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()

    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        title=f'Daily Sales of Pink Morsels ({selected_region.title()})',
        labels={'date': 'Date', 'sales': 'Sales (Total)'}
    )

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='whitesmoke',
        font=dict(color='#333', size=14)
    )

    fig.update_traces(line=dict(color='#8A2BE2', width=3))  # Purple line

    return fig


if __name__ == '__main__':
    app.run(debug=True)
