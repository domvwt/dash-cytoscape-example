import math
import random

import dash
import dash_cytoscape as cyto
from dash import html

app = dash.Dash(__name__)

# Define 20 nodes with random positions in two components
nodes = [
    {
        "data": {
            "id": f"node{i}",
            "label": f"Node {i+1}",
            "component": 1 if i < 10 else 2,
        },
        "position": {
            "x": random.randint(100, 800) if i < 10 else random.randint(900, 2000),
            "y": 250
            + (350 if i < 10 else 350) * math.sin(i * math.pi / 8)
            + random.randint(-50, 50),
        },
        "style": {
            "background-color": "#0074D9" if i < 10 else "#FF4136",
            "line-color": "#000000",
            "width": 40,
            "height": 40,
            "shape": "ellipse",
        },
    }
    for i in range(20)
]

# Define 90 edges connecting nodes within each component
edges = [
    {"data": {"source": f"node{i}", "target": f"node{j}", "label": f"Edge {i+1}-{j+1}"}}
    for i in range(10)
    for j in range(i + 1, 10)
] + [
    {"data": {"source": f"node{i}", "target": f"node{j}", "label": f"Edge {i+1}-{j+1}"}}
    for i in range(10, 20)
    for j in range(i + 1, 20)
]

app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytoscape",
            elements=nodes + edges,
            layout={
                "name": "preset",
                "padding": 10,
                "boundingBox": {"x1": 0, "y1": 0, "x2": 800, "y2": 500},
                "avoidOverlap": True,
            },
            style={"width": "100vw", "height": "100vh"},
        )
    ],
    style={
        "display": "flex",
        "justify-content": "space-between",
        "align-items": "center",
        "height": "100vh",
    },
)

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
