import pydot
import pandas as pd
import pathlib
import os
from PIL import Image
current_path = pathlib.Path(__file__).parent.resolve()

graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')

"""
To add a node: graph.add_node(pydot.Node(<node name>, shape="circle"))
To add an edge: graph.add_edge(pydot.Edge(<start node name>, <end node name>, color="blue"))
Save output as png: graph.write_png("output.png")
"""

user_name = "Daniel"

graph.add_node(pydot.Node(user_name, shape="rectangle"))


def plot_pairs(data, colour):
    all_nodes = data.iloc[:, 0].dropna()
    second_nodes = data.iloc[:, 1].dropna()
    graph.add_node(pydot.Node(data.iloc[0, 0], shape="rectangle"))
    graph.add_edge(pydot.Edge(user_name, data.iloc[0, 0]))
    pairs = list(zip(all_nodes, second_nodes))
    # For each unique main node create a cluster.
    cluster_bar = pydot.Cluster(data.iloc[0, 0])
    for pair in pairs:
        # First try to see if there is an image with the node name:
        try:
            # If there is, then see if it is in the desired .png format:
            if os.path.isfile(str(current_path) + "/Images/" + str(pair[1]) + ".png"):
                # If true then add a new node with the .png image as the node.
                cluster_bar.add_node(pydot.Node(pair[1], shape="rectangle", fixedsize="true",
                                          image=(str(current_path) + "/Images/" + str(pair[1]) + ".png"), width=2, height=2,
                                          label=""))
                cluster_bar.add_edge(pydot.Edge(pair[0], pair[1], color=colour, penwidth=4.0))
            # If there is an image, but it is not in .png format, then convert to .png first then add as the node as
            # before
            else:
                im1 = Image.open(str(current_path) + "/Images/" + str(pair[1]) + ".jpg")
                im1.save(str(current_path) + "/Images/" + str(pair[1]) + ".png")
                cluster_bar.add_node(pydot.Node(pair[1], shape="rectangle", fixedsize="true",
                                                image=(str(current_path) + "/Images/" + str(pair[1]) + ".png"), width=2,
                                                height=2, label=""))
                cluster_bar.add_edge(pydot.Edge(pair[0], pair[1], color=colour, penwidth=4.0))
        except FileNotFoundError:  # If no file is found then add a new node with text.
            cluster_bar.add_node(pydot.Node(pair[1], shape="rectangle"))
            cluster_bar.add_edge(pydot.Edge(pair[0], pair[1], color=colour, penwidth=4.0))

    graph.add_subgraph(cluster_bar)


colour_id = 0
for file_path in os.listdir(current_path):
    colours = ["red", "blue", "green", "orange", "purple", "pink", "black"]
    if file_path.endswith(".csv"):
        data = pd.read_csv(file_path, sep=",", dtype={'Node1': 'string', 'Node2': 'string', 'Type': 'string'})
        plot_pairs(data, colours[colour_id])
        colour_id += 1
    else:
        continue

graph.write_png("output2.png", prog="circo")


