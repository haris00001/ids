#haris shoaib ~FA21-BSE-076~ 

#question 1



import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
]

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
G.add_nodes_from(nodes)

# Add edges to the graph based on the adjacency matrix
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        if adjacency_matrix[i][j] == 1:
            G.add_edge(nodes[i], nodes[j])

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()


#question 2
import random
import networkx as nx

# Assuming G is already defined as a graph

# Assign random weights to the edges
for edge in G.edges(data=True):
    edge[2]['weight'] = random.randint(1, 10)

# Find the shortest path between nodes A and B
shortest_path = nx.shortest_path(G, 'a', 'b', weight='weight')
shortest_path_length = nx.shortest_path_length(G, 'a', 'b', weight='weight')

print("Shortest path between A and B:", shortest_path)
print("Length of the shortest path:", shortest_path_length)
