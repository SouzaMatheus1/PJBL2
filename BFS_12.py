import matplotlib.pyplot as plt
import networkx as nx
from collections import deque, defaultdict

class RedeSocial:
    def __init__(self):
        # Cria um dicionario com listas como chave
        # defaultdict para inicializar as listas
        self.rede = defaultdict(list)

    def add_pessoa(self, pessoa):
        # se a pessoa nao estiver em rede,
        # eh adicionada com uma lista vazia de amigos 
        if pessoa not in self.rede:
            self.rede[pessoa] = []
    
    def forma_amizade(self, p1, p2):
        # forma amizade entre pessoa 1 e pessoa 2
        self.rede[p1].append(p2)
        self.rede[p2].append(p1)

    def recomenda_pessoa(self, usuario):

        visitado = set()
        recomendacoes = set()
        fila = deque([(usuario, 0)])
        visitado.add(usuario)

        while fila:
            pessoa, nivel = fila.popleft()

            if nivel == 2:
                recomendacoes.add(pessoa)
                continue

            for amigo in self.rede[pessoa]:
                if amigo not in visitado:
                    visitado.add(amigo)
                    fila.append((amigo, nivel + 1))

        recomendacoes -= set(self.rede[usuario])

        return list(recomendacoes)
    
    def exibe_rede(self, usuario):
        G = nx.Graph()
        for pessoa, amigos in self.rede.items():
            print(f'{pessoa} -> {amigos}')
            for amigo in amigos:
                G.add_edge(pessoa, amigo)

        # Disposição dos nós
        pos = nx.spring_layout(G)

        # Cria um dicionário para armazenar as cores dos nós
        cores_nomes = {}

        # Definir as cores dos nós com base no usuário e nas recomendações
        recomendacoes = self.recomenda_pessoa(usuario)
        
        for pessoa in self.rede:
            if pessoa == usuario:
                cores_nomes[pessoa] = 'green'  # Cor do usuário selecionado
            elif pessoa in recomendacoes:
                cores_nomes[pessoa] = 'red'  # Cor para recomendações
            else:
                cores_nomes[pessoa] = 'black'  # Cor para os outros nós

        # Definir o tamanho da figura
        plt.figure(figsize=(6, 4))

        # Título do gráfico
        nomes_recomendados = [pessoa for pessoa in recomendacoes]
        Tit = f"Recomendações de amizade para {usuario}:\n"
        Tit += ", ".join(nomes_recomendados) + "."
        plt.title(Tit)

        # Desenha o grafo com a configuração das cores e o peso da fonte em negrito
        nx.draw(G, pos, with_labels=True, node_color='white', font_weight='bold', node_size=3000, font_size=12, edge_color='black')

        # Itera sobre as posições dos nós e altera as cores de fundo
        for node, (x, y) in pos.items():
            # Se o nó for o usuário selecionado, usa uma cor de fundo diferente
            if node == usuario:
                facecolor = '#FFD700'  # Amarelo para o usuário selecionado
            elif node in recomendacoes:
                facecolor = '#ADD8E6'  # Azul claro para as recomendações
            else:
                facecolor = 'white'  # Branco para os outros nós

            # Desenha o nome do nó no gráfico com a cor de fundo e de texto
            plt.text(x, y, node, fontsize=12, ha='center', va='center',
                    bbox=dict(facecolor=facecolor, edgecolor='black', boxstyle='round,pad=0.2'),
                    color=cores_nomes[node])

        # Exibe o gráfico
        plt.show()

        # Exibe as recomendações
        print(f'Recomendações para {usuario}: {recomendacoes}')