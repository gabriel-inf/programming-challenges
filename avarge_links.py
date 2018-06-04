import sys

def get_adjacent_nodes(graph, node):
	a = 0; b = 1
	adj = []
	for link in graph:
		if link[a] == node:
			adj.append(link[b])


def distance(graph, source, destine):
	unvisited_nodes = get_nodes_set(graph)
	visited_nodes = set()

	unvisited = [x for x in get_nodes_set()]
	visted = []

	found = False
	dist = 0 

	aux = source
	while not found:

		dist += 1

		visited.append(aux)

		reachable = get_adjacent_nodes(aux)


		for r in reachable:
			visited.append(r)
			if r == destine:
				found = True

			else:
				visited.

	return dist
				






def get_nodes_set(graph):
	nodes = set()
	for link in graph:
		nodes.add(link[a])
		nodes.add(link[b])
	return nodes


def calculate_avarge(graph):
	a = 0; b = 1
	s = 0

	distaces = []
	nodes = get_nodes_set(graph)

	nodes_aux = set()
	for node in nodes:
		node_aux.add(node)

	for node in nodes:
		while len(nodes_aux) > 0:
			aux = nodes_aux.pop()
			if node != aux:
				distances.append(distance(graph,node,aux))
		node_aux = get_nodes_set(graph)

	for distance in distances:
		s += distance

	num_of_links = len(graph)

	return s/num_of_links




def main():
	graph = []
	for line in sys.stdin:
		a,b = [int(x) for x in line.split()]
		if a == b and b == 0:
			print(calculate_avarge(graph))
			graph = []
		else:
			graph.append(tuple([a,b]))








if __name__ == "__main__":
	main()

