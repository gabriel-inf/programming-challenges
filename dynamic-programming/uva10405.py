import sys

def main():
	for line in sys.stdin:
		w1 = line
		w2 = input()

		n1 = len(w1)
		n2 = len(w2)
		
		table = [[0 for i in range(n2+1)]for j in range(n1+1)]
    
		for i in range(n1+1):
			for j in range(n2+1):
				if i == 0 or j == 0:
					table[i][j] = 0
				elif w1[i-1] == w2[j-1]:
					table[i][j] = table[i-1][j-1] + 1
				else:
					table[i][j] = max(table[i-1][j], table[i][j-1])

		
		print(table[n1][n2])


if __name__ == '__main__':
	main()
