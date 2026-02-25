import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
from plotly.express import line

# Path to the data file
FILE_PATH = "./formatted_data.csv"

# Read and sort the data
df = pd.read_csv(FILE_PATH)
df = df.sort_values(by="date")

# Initialize the app
app = Dash(__name__)

# Create header
title = html.H1(
    "Pink Morsel Sales Visualiser",
    id="title",
    style={
        "textAlign": "center",
        "color": "#ff69b4",
        "fontFamily": "Arial",
        "padding": "20px",
        "backgroundColor": "#1a1a2e",
        "margin": "0"
    }
)

# Create radio buttons
radio = dcc.RadioItems(
    id="region-filter",
    options=[
        {"label": "All", "value": "all"},
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"}
    ],
    value="all",
    inline=True,
    style={
        "textAlign": "center",
        "padding": "20px",
        "fontSize": "18px",
        "color": "white",
        "backgroundColor": "#16213e"
    }
)

# Create graph component
graph = dcc.Graph(id="sales-graph")

# Set app layout
app.layout = html.Div(
    [title, radio, graph],
    style={"backgroundColor": "#0f3460"}
)

# Callback to update chart based on region selected
@callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    # Filter data based on region
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == region]

    # Create updated chart
    chart = line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {region.capitalize()}",
        labels={"date": "Date", "sales": "Sales ($)"},
        color_discrete_sequence=["#ff69b4"]
    )

    chart.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font_color="white",
        title_font_size=22
    )

    return chart

if __name__ == "__main__":
    app.run(debug=True)