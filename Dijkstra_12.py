import networkx as nx
import matplotlib.pyplot as plt

class GrafoDijkstra:
    def __init__(self):
        self.grafo = {}
        self.cidades = [
            "Aurora", "Bonito", "Carmo", "Douras", "Estela", "Felice", 
            "Gema", "Herval", "Ipiaú", "Jaburu", "Lindoa", "Mundaú"
        ]

    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.grafo:
            self.grafo[origem] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[origem].append((destino, peso))
        self.grafo[destino].append((origem, peso))

    def dijkstra(self, inicio):
        distancias = {cidade: float('inf') for cidade in self.grafo}
        distancias[inicio] = 0
        antecessores = {cidade: None for cidade in self.grafo}
        visitados = set()

        while len(visitados) < len(self.grafo):
            atual = min((cidade for cidade in distancias if cidade not in visitados), key=lambda cidade: distancias[cidade])
            visitados.add(atual)

            for vizinho, peso in self.grafo[atual]:
                nova_distancia = distancias[atual] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    antecessores[vizinho] = atual

        return distancias, antecessores

    def encontrar_caminho(self, origem, destino, antecessores):
        caminho = []
        atual = destino
        while atual is not None:
            caminho.insert(0, atual)
            atual = antecessores[atual]
        return caminho

    def plot_grafos(self, caminho, origem, destino, desig, comprimento):
        G = nx.Graph()
        G_result = nx.Graph()

        # Adicionando arestas ao grafo
        for u, vizinhos in self.grafo.items():
            for v, peso in vizinhos:
                G.add_edge(u, v, weight=peso)
                G_result.add_edge(u, v, weight=peso)

        # Layout do grafo
        pos = nx.spring_layout(G, seed=42)  # Defina um seed para garantir layout consistente

        # Exibindo o gráfico
        plt.figure(figsize=(12, 8))

        # Grafo original
        plt.subplot(1, 2, 1)
        nx.draw(G, pos, with_labels=True, labels={i: desig[i] for i in self.grafo.keys()},
                node_color='lightgray', node_size=500, font_size=10, font_color='black',
                edge_color='black', linewidths=1, edgecolors='black')
        nx.draw_networkx_nodes(G, pos, nodelist=[origem], node_color='lightgreen', edgecolors='black')
        nx.draw_networkx_nodes(G, pos, nodelist=[destino], node_color='lightsalmon', edgecolors='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)},
                                    font_color='black', rotate=False)
        plt.title("Grafo Original")

        # Grafo com caminho mínimo
        plt.subplot(1, 2, 2)
        edge_colors = ['black' if u in caminho and v in caminho else 'lightgray' for u, v in G_result.edges()]
        nx.draw(G_result, pos, with_labels=True, labels={i: desig[i] for i in self.grafo.keys()},
                node_color='lightgray', node_size=500, font_size=10, font_color='black',
                edge_color=edge_colors, linewidths=1, edgecolors='black')
        nx.draw_networkx_nodes(G_result, pos, nodelist=[origem], node_color='lightgreen', edgecolors='black')
        nx.draw_networkx_nodes(G_result, pos, nodelist=[destino], node_color='lightsalmon', edgecolors='black')
        nx.draw_networkx_edge_labels(G_result, pos, edge_labels={(u, v): d['weight'] for u, v, d in G_result.edges(data=True)},
                                    font_color='black', rotate=False)

        plt.title("Grafo com Caminho Mínimo")
        plt.text(0.5, -0.1, f"Comprimento caminho: {comprimento}", fontsize=10, ha='center',
                transform=plt.gca().transAxes)
        plt.tight_layout()  # Para garantir que o layout se ajuste corretamente
        plt.show()

