from operator import attrgetter


def read(filename):
	file = open(filename, 'r')
	data = file.readlines()

	E = []

	for line in data[1:]:
		item = line.split()
		E.append(Edge(int(item[0])-1, int(item[1])-1, int(item[2])))

	return E


class Edge: 
	def __init__(self, start, end, cost):
		self.start = start
		self.end = end 
		self.cost = cost


class unionfind: 
	def __init__(self, n): 
		self.root = list(range(n))
		self.rank = [0] * n 
		self.num = n 

	def find(self, x):
		s_list = self.root
		if s_list[x] != x:
			s_list[x] = self.find(s_list[x])

		return s_list[x]

	def count(self):
		return self.num

	def union(self, x, y): 
		s = self.root
		rank_list = self.rank

		s1 = self.find(x)
		s2 = self.find(y)

		if s1 == s2:
			return 

		self.num -= 1
		if rank_list[s1] == rank_list[s2]:
			s[s2] = s1
			rank_list[s1] += 1
		elif rank_list[s1] > rank_list[s2]:
			s[s2] = s1
		else:
			s[s1] = s2

	def connected(self, x, y): 
		return self.find(x) == self.find(y)


def clustering(E, num_clusters, num_vertices):
	E = sorted(E, key = attrgetter('cost'))

	UF = unionfind(num_vertices)

	for edge in E:
		if UF.count() != num_clusters and not UF.connected(edge.start, edge.end):
			UF.union(edge.start, edge.end)
		if UF.count() == num_clusters and not UF.connected(edge.start, edge.end):
			return edge.cost


def main():
	E = read('clustering1.txt')

	max_dis = clustering(E, 4, 500)
	print(max_dis)


main()
#106




