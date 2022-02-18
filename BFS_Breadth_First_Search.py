# BFS 
# Busca em Largura
vertices = int(input('Digite a quantidade de vértices: '))
grafo = [[]for i in range(vertices)]
for i in range(vertices-1):
  v1, v2 = map(int,input('Digite os 2 vértices que são adjacentes: (EX: 1 2) ').split())
  grafo[v1-1] += [v2]
  grafo[v2-1] += [v1]
print('Grafo: ',grafo)
print('BFS --> ',end=' ')
def bfs(grafo, vertice):
  visitado = [False] * vertices
  fila = []
  fila.append(vertice)
  visitado[vertice-1] = True
  while fila:
    vertice = fila.pop(0)
    print(vertice, end = ' ')
    for i in grafo[vertice-1]:
      if visitado[i-1] == False:
        fila.append(i)
        visitado[i-1] = True

bfs(grafo, 3)
