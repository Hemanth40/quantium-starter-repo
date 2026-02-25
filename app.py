import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the formatted data
df = pd.read_csv("formatted_data.csv")

# Sort by date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create the line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales ($)"}
)

# Add a vertical line to show price increase date
fig.add_shape(
    type="line",
    x0="2021-01-15", x1="2021-01-15",
    y0=0, y1=1,
    yref="paper",
    line=dict(color="red", dash="dash")
)

# Add annotation for the line
fig.add_annotation(
    x="2021-01-15",
    y=1,
    yref="paper",
    text="Price Increase",
    showarrow=False,
    font=dict(color="red")
)

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)