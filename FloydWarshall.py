def floyd_warshall(grafo):
    dist = list(map(lambda i: list(map(lambda j: j, i)), grafo))
    n = len(grafo)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

INF = float('inf')
grafo = [
    [0,   3, INF, 5, 4],
    [2,   0, INF, 4, 6],
    [INF, 1, 0,   INF, 3],
    [INF, INF, 2, 0, 1],
    [4, 4, 8, 2, 8]
]

distancias = floyd_warshall(grafo)
for fila in distancias:
    print(fila)
