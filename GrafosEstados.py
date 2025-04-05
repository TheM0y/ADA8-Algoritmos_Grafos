import networkx as nx
import matplotlib.pyplot as plt
import itertools

estados = ["CDMX", "Jalisco", "Nuevo León", "Veracruz", "Chiapas", "Oaxaca", "Yucatán"]

G = nx.Graph()

G.add_nodes_from(estados)

aristas = [
    ("CDMX", "Jalisco", 80),
    ("CDMX", "Veracruz", 90),
    ("CDMX", "Oaxaca", 70),
    ("Jalisco", "Nuevo León", 120),
    ("Jalisco", "Oaxaca", 60),
    ("Nuevo León", "Veracruz", 110),
    ("Nuevo León", "Yucatán", 130),
    ("Veracruz", "Chiapas", 140),
    ("Veracruz", "Yucatán", 100),
    ("Chiapas", "Oaxaca", 80),
    ("Oaxaca", "Yucatán", 150)
]

for (u, v, cost) in aristas:
    G.add_edge(u, v, weight=cost)

def calcular_costo(recorrido, grafo):
    costo_total = 0
    for i in range(len(recorrido)-1):
        costo_total += grafo[recorrido[i]][recorrido[i+1]]['weight']
    return costo_total

def encontrar_camino_hamiltoniano(grafo, nodos):
    for perm in itertools.permutations(nodos):
        valido = True

        for i in range(len(perm)-1):
            if not grafo.has_edge(perm[i], perm[i+1]):
                valido = False
                break
        if valido:
            return list(perm)
    return None


def encontrar_ciclo_hamiltoniano(grafo, nodos):

    inicio = nodos[0]
    for perm in itertools.permutations(nodos[1:]):
        recorrido = [inicio] + list(perm) + [inicio]
        valido = True
        for i in range(len(recorrido)-1):
            if not grafo.has_edge(recorrido[i], recorrido[i+1]):
                valido = False
                break
        if valido:
            return recorrido
    return None

camino_ham = encontrar_camino_hamiltoniano(G, estados)
ciclo_ham = encontrar_ciclo_hamiltoniano(G, estados)

if camino_ham:
    costo_camino = calcular_costo(camino_ham, G)
else:
    costo_camino = None

if ciclo_ham:
    costo_ciclo = calcular_costo(ciclo_ham, G)
else:
    costo_ciclo = None

print("Recorrido sin repetir estados (camino hamiltoniano):")
if camino_ham:
    print(" -> ".join(camino_ham))
    print("Costo total:", costo_camino)
else:
    print("No se encontró un camino hamiltoniano.")

print("\nRecorrido con repetición (ciclo hamiltoniano):")
if ciclo_ham:
    print(" -> ".join(ciclo_ham))
    print("Costo total:", costo_ciclo)
else:
    print("No se encontró un ciclo hamiltoniano.")

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6), num="Grafo de Estados y Conexiones")
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=800)
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

plt.title("Grafo de Estados y Costos de Traslado")
plt.axis("off")
plt.show()

print("\nEstados y sus relaciones (adyacencia):")
for estado in G.nodes():
    vecinos = list(G.neighbors(estado))
    relaciones = []
    for vecino in vecinos:
        costo = G[estado][vecino]["weight"]
        relaciones.append(f"{vecino} (costo {costo})")
    print(f"{estado}: {', '.join(relaciones)}")
