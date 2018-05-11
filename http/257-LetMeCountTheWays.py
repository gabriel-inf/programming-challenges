import sys

def main():

	coins = [0,1,5,10,25,50]
	quant = [0]*(30001)
	quant[0] = 1

	for c in range(1,len(coins)):
		for j in range(coins[c],30001):
			quant[j] += quant[j-coins[c]]

	for line in sys.stdin:
		change = int(line)
		if quant[change] > 1:
			print("There are " +str(quant[change])+ " ways to produce " + str(change) + " cents change.")
		else:
			print("There is only 1 way to produce " + str(change) + " cents change.")

if __name__ == '__main__':
	main()
