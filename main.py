import pydot
import pandas as pd
import pathlib
import os
from PIL import Image
current_path = pathlib.Path(__file__).parent.resolve()



data = pd.read_csv("Data.csv", sep=",", dtype={'Node1': 'string', 'Node2': 'string', 'Type': 'string'})

graph = pydot.Dot("my_graph", graph_type="digraph", overlap=False, splines='true')
graph.set_edge_defaults(color="blue")

"""
To add a node: graph.add_node(pydot.Node(<node name>, shape="circle"))
To add an edge: graph.add_edge(pydot.Edge(<start node name>, <end node name>, color="blue"))
Save output as png: graph.write_png("output.png")
"""

user_name = "Daniel"
all_nodes = data.iloc[:, 0].dropna()
second_nodes = data.iloc[:, 1].dropna()


def create_root():
    graph.add_node(pydot.Node(user_name))
    first_nodes = list(set(all_nodes) - set(second_nodes))

    # Distinct initial nodes
    initial_nodes = []
    for member in all_nodes:
        if member not in first_nodes:
            initial_nodes.append(member)
        else:
            continue

    return first_nodes

first_nodes = create_root()


def create_initial_nod(first_nodes):
    # For each node in the first column...
    for initial_node in first_nodes:
        # Add the node
        graph.add_node(pydot.Node(initial_node, shape="rectangle"))
        # Add an edge from each of the initial nodes to the parent user node.
        graph.add_edge(pydot.Edge(user_name, initial_node))


create_initial_nod(first_nodes)


def create_pairs():
    pairs = list(zip(all_nodes, second_nodes))
    return pairs


pairs = create_pairs()


def plot_pairs2():
    # For each unique main node create a cluster.
    for pair in pairs:
        # First try to see if there is an image with the node name:
        try:
            # If there is, then see if it is in the desired .png format:
            if os.path.isfile(str(current_path) + "/" + str(pair[1]) + ".png"):
                # If true then add a new node with the .png image as the node.
                graph.add_node(pydot.Node(pair[1], shape="rectangle", fixedsize="true",
                                          image=(str(current_path) + "/" + str(pair[1]) + ".png"), width=2, height=2,
                                          label=""))
                graph.add_edge(pydot.Edge(pair[0], pair[1], color='red', penwidth=4.0))
            # If there is an image, but it is not in .png format, then convert to .png first then add as the node as
            # before
            else:
                im1 = Image.open(str(current_path) + "/" + str(pair[1]) + ".jpg")
                im1.save(str(current_path) + "/" + str(pair[1]) + ".png")
                graph.add_node(pydot.Node(pair[1], shape="rectangle", fixedsize="true",
                                          image=(str(current_path) + "/" + str(pair[1]) + ".png"), width=2, height=2,
                                          label=""))
                graph.add_edge(pydot.Edge(pair[0], pair[1], color='red', penwidth=4.0))
        except FileNotFoundError: # If no file is found then add a new node with text.
            graph.add_node(pydot.Node(pair[1], shape="rectangle"))
            graph.add_edge(pydot.Edge(pair[0], pair[1], color='red', penwidth=2.0))


plot_pairs2()


def plot_pairs():
    colours = ["red", "orange", "blue", "yellow", "black", "green", "lightgrey", "purple", "pink"]
    colour_id = 0

    # For each unique main node create a cluster.
    for initial_node in first_nodes:
        cluster_bar = pydot.Cluster(initial_node)
        for pair in pairs:
            if pair[0] == initial_node:
                cluster_bar.add_node(pydot.Node(pair[1], shape="rectangle", image="image.png"))
                cluster_bar.add_edge(pydot.Edge(pair[0], pair[1], color=colours[colour_id], penwidth=2.0))
            else:
                continue
        colour_id += 1
        graph.add_subgraph(cluster_bar)


#plot_pairs()


graph.write_png("output2.png", prog="circo")


