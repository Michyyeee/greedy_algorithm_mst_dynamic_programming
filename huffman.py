import heapq
from collections import namedtuple


Node = namedtuple('Node', ('weight', 'index'))


def read(filename):
	file = open(filename, 'r')
	data = file.readlines()

	tree = []

	for index, line in enumerate(data[1:]):
		item = line.split()
		tree.append(Node(int(item[0]), str(index)))

	heapq.heapify(tree)
	return tree


def combine(a, b):
	return Node(a.weight+b.weight, '+'.join([a.index, b.index]))


def huffman(tree):
	code_len = [0] * len(tree)

	while len(tree) > 1:
		a = heapq.heappop(tree)
		b = heapq.heappop(tree)

		new_node = combine(a, b)
		heapq.heappush(tree, new_node)

		com = [int(item) for item in new_node.index.split('+')]
		for i in com:
			code_len[i] += 1

	return code_len


def main():
	tree = read('huffman.txt')
	code_len = huffman(tree)
	print(max(code_len), min(code_len))


main()
#19, 9