import networkx as nx
print(nx.nx_agraph.read_dot("/Users/user/Desktop/New folder/roadmap.dot"))

import networkx as nx
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])

from typing import NamedTuple

class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )

import networkx as nx

def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )

from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

nodes["london"]

print(graph)