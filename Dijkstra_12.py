import heapq

class Grafo:
    def __init__(self, adjacencias):
        self.cidades = {}

    
    def dijkstra(self, origem):
        dist = {cidade: float('inf') for cidade in self.adjacencias}
        dist[origem] = 0
        pred = {cidade: None for cidade in self.adjacencias}
        fila = [(0, origem)]

        while fila:
            atual_dist, 