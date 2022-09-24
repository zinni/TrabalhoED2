from asyncio.windows_events import NULL
from queue import PriorityQueue
from tracemalloc import start

class Graph:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.edges = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]
        self.visitados = []

    def add_aresta(self, u, v, peso):
        self.edges[u][v] = peso
        self.edges[v][u] = peso

def dijkstra(graph, comeco_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[comeco_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, comeco_vertex))
    lista = []
    lista2 = []

    while not pq.empty():
        (dist, vertice_atual) = pq.get()
        graph.visitados.append(vertice_atual)
        for vizinho in range(graph.v):
            if graph.edges[vertice_atual][vizinho] != -1:
                distancia = graph.edges[vertice_atual][vizinho]
                #VERIFICAR SE JA FOI VISITADO
                if vizinho not in graph.visitados:
                    custo_ant = D[vizinho]
                    custo_novo = D[vertice_atual] + distancia
                    if custo_novo < custo_ant:
                        pq.put((custo_novo, vizinho))
                        D[vizinho] = custo_novo
                        lista.append(vizinho)
                        lista2.append(vertice_atual)
                    
    return D, lista, lista2

def caminho(comeco, alvo, lista, lista2):
    trajetoria = [alvo]
    while alvo is not comeco:
        x = lista.index(alvo)
        trajetoria.append(lista2[x])
        alvo = lista2[x]
    trajetoria.reverse()
    return trajetoria

g = Graph(29)
g.add_aresta(1, 2, 12.8)
g.add_aresta(1, 8, 27.7)
g.add_aresta(1, 9, 23.6)
g.add_aresta(2, 3, 24.1)
g.add_aresta(2, 4, 42)
g.add_aresta(2, 7, 17)
g.add_aresta(2, 8, 22.3)
g.add_aresta(3, 4, 12.8)
g.add_aresta(3, 6, 30.8)
g.add_aresta(3, 7, 32)
g.add_aresta(4, 5, 20)
g.add_aresta(5, 6, 25)
g.add_aresta(5, 14, 45)
g.add_aresta(5, 15, 21.6)
g.add_aresta(6, 7, 14.8)
g.add_aresta(6, 12, 37.3)
g.add_aresta(6, 13, 33.4)
g.add_aresta(6, 14, 31.3)
g.add_aresta(7, 8, 24.8)
g.add_aresta(7, 11, 32.5)
g.add_aresta(7, 13, 41.3)
g.add_aresta(8, 9, 26.3)
g.add_aresta(8, 10, 50)
g.add_aresta(8, 11, 19.8)
g.add_aresta(9, 10, 24)
g.add_aresta(10, 11, 24)
g.add_aresta(10, 19, 20)
g.add_aresta(10, 20, 39.8)
g.add_aresta(11, 12, 23)
g.add_aresta(11, 19, 38)
g.add_aresta(12, 13, 20)
g.add_aresta(12, 17, 39)
g.add_aresta(12, 18, 59)
g.add_aresta(13, 14, 16)
g.add_aresta(13, 16, 32.5)
g.add_aresta(13, 17, 34.3)
g.add_aresta(14, 15, 23.8)
g.add_aresta(14, 16, 39)
g.add_aresta(16, 17, 62.2)
g.add_aresta(16, 27, 38)
g.add_aresta(16, 28, 33)
g.add_aresta(17, 18, 22.6)
g.add_aresta(17, 23, 12.2)
g.add_aresta(18, 19, 14.7)
g.add_aresta(18, 22, 28.3)
g.add_aresta(18, 23, 20.4)
g.add_aresta(19, 20, 34)
g.add_aresta(19, 22, 29)
g.add_aresta(20, 21, 15.7)
g.add_aresta(22, 23, 58.3)
g.add_aresta(23, 24, 9.5)
g.add_aresta(23, 26, 24.2)
g.add_aresta(24, 25, 23.6)
g.add_aresta(24, 26, 21)
g.add_aresta(24, 28, 58)
g.add_aresta(25, 28, 42)
g.add_aresta(27, 28, 26)

D, lista, lista2 = dijkstra(g, 8)

print("A melhor rota encontradas para cada cidade foi de:")
print("Para a cidade 15: ",round(D[15],2), "na rota", caminho(8, 15, lista, lista2))
print("Para a cidade 26: ",round(D[26],2), "na rota", caminho(8, 26, lista, lista2))
print("Para a cidade 27: ",round(D[27],2), "na rota", caminho(8, 27, lista, lista2))