def warshall(grafo):
    n = len(grafo)
    cierre_transitivo = [fila[:] for fila in grafo]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cierre_transitivo[i][j] = cierre_transitivo[i][j] or (cierre_transitivo[i][k] and cierre_transitivo[k][j])
    return cierre_transitivo

grafo = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

resultado = warshall(grafo)
for fila in resultado:
    print(fila)
