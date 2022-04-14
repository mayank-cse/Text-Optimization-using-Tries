import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
#edge=("a","b")

#add edge list
n=int(input('Enter number of edges: '))
print('Enter edge pairs separated by space: ')
for i in range(n):
	edge=tuple((x.strip()) for x in input().split())
	G.add_edge(*edge)

#G.add_node("a");
#G.add_nodes_from(edge)

print(edge)

print("Nodes: ",G.nodes())
print("Edges: ",G.edges())
nx.draw(G, with_labels= True)
#plt.savefig("graph1.png") #change name of file
plt.show()  #immediate output
