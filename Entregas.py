from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                            
                    
    return D

g = Graph(29)
g.add_edge(1, 2, 12.8)
g.add_edge(1, 8, 27.7)
g.add_edge(1, 9, 23.6)
g.add_edge(2, 3, 24.1)
g.add_edge(2, 4, 42)
g.add_edge(2, 7, 17)
g.add_edge(2, 8, 22.3)
g.add_edge(3, 4, 12.8)
g.add_edge(3, 6, 30.8)
g.add_edge(3, 7, 32)
g.add_edge(4, 5, 20)
g.add_edge(5, 6, 25)
g.add_edge(5, 14, 45)
g.add_edge(5, 15, 21.6)
g.add_edge(6, 7, 14.8)
g.add_edge(6, 12, 37.3)
g.add_edge(6, 13, 33.4)
g.add_edge(6, 14, 31.3)
g.add_edge(7, 8, 24.8)
g.add_edge(7, 11, 32.5)
g.add_edge(7, 13, 41.3)
g.add_edge(8, 9, 26.3)
g.add_edge(8, 10, 50)
g.add_edge(8, 11, 19.8)
g.add_edge(9, 10, 24)
g.add_edge(10, 11, 24)
g.add_edge(10, 19, 20)
g.add_edge(10, 20, 39.8)
g.add_edge(11, 12, 23)
g.add_edge(11, 19, 38)
g.add_edge(12, 13, 20)
g.add_edge(12, 17, 39)
g.add_edge(12, 18, 59)
g.add_edge(13, 14, 16)
g.add_edge(13, 16, 32.5)
g.add_edge(13, 17, 34.3)
g.add_edge(14, 15, 23.8)
g.add_edge(14, 16, 39)
g.add_edge(16, 17, 62.2)
g.add_edge(16, 27, 38)
g.add_edge(16, 28, 33)
g.add_edge(17, 18, 22.6)
g.add_edge(17, 23, 12.2)
g.add_edge(18, 19, 14.7)
g.add_edge(18, 22, 28.3)
g.add_edge(18, 23, 20.4)
g.add_edge(19, 20, 34)
g.add_edge(19, 22, 29)
g.add_edge(20, 21, 15.7)
g.add_edge(22, 23, 58.3)
g.add_edge(23, 24, 9.5)
g.add_edge(23, 26, 24.2)
g.add_edge(24, 25, 23.6)
g.add_edge(24, 26, 21)
g.add_edge(24, 28, 58)
g.add_edge(25, 28, 42)
g.add_edge(27, 28, 26)

D = dijkstra(g, 8)

print("A melhor rota encontradas para cada cidade foi de:")
print("Para a cidade 15: ",round(D[15],2))
print("Para a cidade 26: ",round(D[26],2))
print("Para a cidade 27: ",round(D[27],2))

#for vertex in range(len(D)):
#    print("Distance from vertex 8 to vertex", vertex, "is", D[vertex])