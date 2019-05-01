import random
import sys
import numpy as np

valor = int(sys.argv[1])


matrix = np.random.randint(0,10,(valor,valor))

f= open("nodos"+str(sys.argv[1])+".txt","w+")

for i in range(valor):
    #print("entrou no for")
    for j in range(valor):
        #print(matrix[i][j])
        #if matrix[i][j] !=0:
        matrix[j][i] = matrix[i][j]
        #print(matrix[i][j])


for i in range(valor):
    for j in range(valor):
        if i==j:
            matrix[i][j] = 0
            f.write( "%d " % 0)
        else:
            f.write( "%d " % matrix[i][j])
    f.write("\n")
print (sys.argv[1])
print (matrix)
