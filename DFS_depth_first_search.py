# DFS depth-first search
# Busca em Profundidade
vertices = int(input('Digite a quantidade de vértices: '))
grafo = [[] for i in range(vertices)]
for i in range(vertices-1):
  v1, v2 = map(int,input('Digite os 2 vértices que são adjacentes: (EX: 1 2) ').split())
  grafo[v1-1] += [v2]
  grafo[v2-1] += [v1]
print()
print('Grafo: ',grafo)
print('DFS -->',end=' ')
visitado = [False] * vertices
def dfs(grafo,vertice,visitado):
  visitado[vertice-1] = True
  print(vertice, end= ' ')
  for i in grafo[vertice-1]:
    if visitado[i-1] == False:
      dfs(grafo,i,visitado)

dfs(grafo,3,visitado)
