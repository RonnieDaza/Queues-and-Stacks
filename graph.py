import networkx as nx
print(nx.nx_agraph.read_dot("/Users/user/Desktop/New folder/roadmap.dot"))

import networkx as nx
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])