def read(filename):
	file = open(filename, 'r')
	data = file.readlines()

	weights = [0] * (int(data[0])+1)

	for index, line in enumerate(data[1:]):
		item = line.split()
		weights[index + 1] = int(item[0])

	return weights


def mwis(weights):
	A = [0] * len(weights)
	A[0] = 0
	A[1] = weights[1]

	for i in range(2, len(weights)):
		A[i] = max(A[i-1], A[i-2]+weights[i])

	s = []
	i = len(weights) - 1

	while i >= 1:
		if A[i-1] >= A[i-2] + weights[i]:
			i -= 1
		else:
			s.append(i)
			i -= 2 

	return A, s


def main():
	w = read('mwis.txt')
	A, S = mwis(w)
	lista = [1,2,3,4,17,117,517,997]
	binary = []

	for i in lista:
		if i in S:
			binary.append(1)
		else:
			binary.append(0)

	print(binary)


main()
#10100110