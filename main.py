from BFS_12 import RedeSocial
# from Dijkstra_12 import 

# Exemplo de uso:
rede = RedeSocial()
rede.add_pessoa("Ana")
rede.add_pessoa("Bruno")
rede.add_pessoa("Carla")
rede.add_pessoa("Daniel")
rede.add_pessoa("Elaine")
rede.add_pessoa("Fabio")

# Adiciona as amizades (conexões) na rede
rede.forma_amizade("Ana", "Bruno")
rede.forma_amizade("Ana", "Carla")
rede.forma_amizade("Bruno", "Daniel")
rede.forma_amizade("Carla", "Elaine")
rede.forma_amizade("Daniel", "Elaine")
rede.forma_amizade("Elaine", "Fabio")

# Exibe as recomendações de amigos para "Ana"
rede.exibe_rede("Ana")