#Dijkstra's Algorithm
import networkx as nx
G=nx.Graph()
e=[('a','b',8),('a','c',2),('a','d',5),('b','f',13),('b','d',2),('c','d',2),('c','e',5),('e','g',1),('d','g',3),('d','e',1),('f','g',2),('g','h',6),('f','h',3)]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G,'a','h'))