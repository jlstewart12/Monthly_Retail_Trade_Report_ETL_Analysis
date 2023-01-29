import dash
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

data = pd.read_csv("src\ETL\data\mrtssales92-present.csv")
data["Month"] = pd.to_datetime(data["Month"], format="%Y-%m-%d")
data.sort_values("Month", inplace=True)
# data['Adjusted'] = data['Adjusted'].apply(lambda x: x.capitalize())

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Monthly Retail Trade 1992 - Present"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🛒", className="header-emoji"),
                html.H1(
                    children="Monthly Retail Trade", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of monthly retail sales"
                    " and percent changes"
                    " between 1992 and 2022",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Kind of Business", className="menu-title"),
                        dcc.Dropdown(
                            id="industry-filter",
                            options=[
                                {"label": industry, "value": industry}
                                for industry in np.sort(data['Kind of Business'].unique())
                            ],
                            value="Retail and food services sales total",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                # html.Div(
                #     children=[
                #         html.Div(children="Adjusted", className="menu-title"),
                #         dcc.Dropdown(
                #             id="Adjusted-filter",
                #             options=[
                #                 {"label": Adjusted, "value": Adjusted}
                #                 for Adjusted in data.Adjusted.unique()
                #             ],
                #             value="Organic",
                #             clearable=False,
                #             searchable=False,
                #             className="dropdown",
                #         ),
                #     ],
                # ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range", className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.Month.min().date(),
                            max_date_allowed=data.Month.max().date(),
                            start_date=data.Month.min().date(),
                            end_date=data.Month.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="sales-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="change-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    [Output("sales-chart", "figure"), Output("change-chart", "figure")],
    [
        Input("industry-filter", "value"),
        # Input("Adjusted-filter", "Adjusted"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(industry, start_date, end_date):
    mask = (
        (data['Kind of Business'] == industry)
        # & (data.Adjusted == Adjusted)
        & (data['Month'] >= start_date)
        & (data['Month'] <= end_date)
    )
    filtered_data = data.loc[mask, :]
    sales_chart_figure = {
        "data": [
            {
                "x": pd.to_datetime(filtered_data["Month"]),
                "y": filtered_data["Sales"],
                "type": "lines",
                "hovertemplate": "Date: %{x:%B}<br>Sales: $%{y:,.f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Monthly Retail Sales",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True, "spikemode": 'across', "spikedash":"dot"},
            "yaxis": {"tickprefix": "$", "fixedrange": True, "spikemode": 'across', "spikedash":"dot"},
            "colorway": ["#17B897"],
        },
    }

    changes_chart_figure = {
        "data": [
            {
                "x": pd.to_datetime(filtered_data["Month"]),
                "y": filtered_data["Percent Change"],
                "hovertemplate": "Date: %{x:%B}<br>Percent Change: %{y:.2p}<extra></extra>",
                "type": "bar",
                "marker": dict(color=np.where(filtered_data["Percent Change"] < 0, '#990000', '#0a75ad')),
            },
        ],
        "layout": {
            "title": {"text": "Percent Changes", "x": 0.05, "xanchor": "left"},
            "yaxis": {"fixedrange": True, "spikemode": 'across', "spikedash":"dot"},
            "colorway": ["#ff8040"],
        },
    }

    return sales_chart_figure, changes_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)