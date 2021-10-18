import random 


def read(filename):
	file = open(filename, 'r')
	data = file.readlines()

	nodenum = 500

	graph = [[] for i in range(nodenum+1)]

	for line in data[1:]:
		item = line.split()
		graph[int(item[0])] += [(int(item[1]), int(item[2]))]
		graph[int(item[1])] += [(int(item[0]), int(item[2]))]


	return graph


def mst(graph):
	X = set()
	T = 0

	X.add(random.choice([i for i in range(1, len(graph))]))


	while len(X) < len(graph) - 1:
		E = {}

		for node in X:
			for v in graph[node]:
				if v[0] not in X:
					E[(node, v[0])] = v[1]

		(u, v), cost = min(E.items(), key = lambda y: y[1])

		X.add(v)
		T += cost

	return T


def main():
	graph = read('edges.txt')
	T = mst(graph)
	print(T)


main()


 #-3612829

