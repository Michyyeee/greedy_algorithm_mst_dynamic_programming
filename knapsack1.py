def read(filename):
	file = open(filename, 'r')
	data = file.readlines()

	capacity = int(data[0].split()[0])
	n = int(data[0].split()[1])

	V = [0] * (n+1)
	W = [0] * (n+1)

	for index, line in enumerate(data[1:]):
		V[index+1] = int(line.split()[0])
		W[index+1] = int(line.split()[1])

	return V, W, capacity, n


def knapsack(V, W, capacity, n):
	A = [[0]*(capacity+1) for j in range(n+1)]
	for i in range(1, n+1):
		for x in range(capacity+1):
			if W[i]>x:
				A[i][x] = A[i-1][x]
			else:
				A[i][x] = max(A[i-1][x], A[i-1][x-W[i]] + V[i])

	return A

def main():
	V, W, capacity, n = read('knapsack_big.txt')
	A = knapsack(V, W, capacity, n)
	print(A[-1][-1])

main()
#2493893