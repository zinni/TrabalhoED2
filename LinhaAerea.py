from collections import defaultdict

class Grafo:
 
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []
 
    #Adiciona vértices no grafo
    def addEdge(self, u, v, w):
        self.grafo.append([u, v, w])
 
    #Localiza elemento i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    #Junta os elementos x e y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    #Funçaõ principal
    def KruskalMST(self):
 
        resultado = []
        i = 0
        e = 0
 
        # Arruma os pesos em ordem decrescente
        self.grafo = sorted(self.grafo,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        #Cria subsets
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Numero de arestas são igual a vértices-1
        while e < self.V - 1:

            # Pega o menor valor de aresta e incrementa
            # seu indice para iteração
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # Se incluir o vértice não criar um ciclo
            # incementa o indice para o proximo vertice
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.union(parent, rank, x, y)
        custoMinimo = 0
        print ("Distâncias entre as cidades")
        for u, v, peso in resultado:
            custoMinimo += peso
            print("%d -- %d == %d" % (u, v, peso))
        print("Custo mínimo de cobertura" , custoMinimo)
 
g = Grafo(7)
g.addEdge(0, 1, 2704)
g.addEdge(0, 2, 1846)
g.addEdge(0, 4, 337)
g.addEdge(0, 5, 1464)
g.addEdge(1, 2, 867)
g.addEdge(1, 3, 187)
g.addEdge(1, 6, 1258)
g.addEdge(2, 3, 740)
g.addEdge(2, 5, 802)
g.addEdge(3, 6, 1090)
g.addEdge(4, 5, 1235)
g.addEdge(4, 6, 2342)
g.addEdge(5, 6, 1121)
 
g.KruskalMST()