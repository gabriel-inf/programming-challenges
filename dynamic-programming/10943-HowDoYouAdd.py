import sys
import numpy as np

k_max = 100+1
n_max = 100+1

def create_table():
    table = np.zeros((n_max, k_max))
    table[:,1] = int(1)
    table[0,:] = int(1)

    for n in range(1,n_max):
        for k in range(2,k_max):
            table[n][k] = int(table[n-1][k] + table[n][k-1])
    return table

def main():

    values = create_table()
    for line in sys.stdin:
        n,k = line.split()
        n = int(n)
        k = int(k)
        if n == k and k == 0:
            break
        else:
            print(int(values[n,k]))


if __name__ == '__main__':
    main()