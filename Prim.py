import csv
import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    def printMST(self, parent):
        print("Aresta \tPeso")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][ parent[i] ])
 
    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
 
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True 
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u

        self.printMST(parent)

arquivo = open('prim.csv', newline='', )
tabela = list(csv.reader(arquivo, delimiter=',', quoting=csv.QUOTE_NONNUMERIC))
novo = []
cont = 0
for line in tabela:
    cont =  cont + 1                                                                                                                          
    novo.append([int(i) for i in line])

g = Graph(cont)
g.graph = novo
g.primMST()