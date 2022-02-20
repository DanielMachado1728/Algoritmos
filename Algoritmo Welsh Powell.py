# MINHA IMPLEMENTAÇÃO DO ALGORITMO WELSH POWELL


# recebe o nome do grafo em seguida dois vertices, e retorna um valor booleano respondendo se há ou não adjacencia entre esses dois vertices
def tem_adjacencia(grafo,v1,v2):
  bol = False
  for chave,valor in grafo.items():
    if chave == v1 or chave == v2:
      if v1 in valor or v2 in valor:
        bol = True
        break
  return bol

# recebe uma lista de vertices nao adjacentes a um certo vertice. E retorna a maior lista possível de vertices que podem ser pintados pela mesma cor
def checar_adjacencias(lista):
  adjacentes = [[] for i in range(len(lista))]
  for i in lista:
    for j in adjacentes:
      if j == []:
        j.append(i)
      else:
        flag = True
        for k in j:
          if tem_adjacencia(grafo,i,k):
            flag = False
            break
        if flag:
          j.append(i)
          break
        else:
          continue
  lmax = len(adjacentes[0])
  maior_lista = adjacentes[0]
  return maior_lista

# retorna lista de vertices não adjacentes a v
def sem_adjacencia(grafo,v): 
  l = []
  for i in grafo:
    if i not in grafo[v] and i != v:
      l.append(i)
  return l

# o algoritmo 
def welsh_powell(grafo):
  ordenado = sorted(list(grafo.keys()), key=lambda x: len(grafo[x]), reverse=True)# ordenação pelo número de vertices. OBS: o resultado será uma lista
  cores = {}#dicionario que guardará os vértices e suas cores
  estados = [False] * len(ordenado)

  cont = 1
  for i in range(len(estados)):
    if estados[i] == False: #se nao foi pintado
      cores[ordenado[i]] = cont # dicionario recebe o vertice(chave) e cor(valor)
      estados[i] = True # nao será pintado novamente porque agora tem o valor booleano "True"
      vertices_n_adjacentes_i = sem_adjacencia(grafo,ordenado[i]) # vertices_n_adjacentes será uma lista com os todos os vertices que não forem adjacentes
      for vertice in range(len(ordenado)):#caso um vertice pintado não seja adjacente a esse vertice atual, ele precisa ser removido da lista 
        if estados[vertice] == True and ordenado[vertice] in vertices_n_adjacentes_i:
          vertices_n_adjacentes_i.remove(ordenado[vertice])
      if vertices_n_adjacentes_i == []: # se nao tiver vertices nao adjacentes
        cont += 1 # mudar de cor
        continue
      #caso contrario a maior lista sem adjacencia ao meu vertice será pintada para aproveitar a cor atual ao máximo.OBS: a maior, levando em conta os ciclos
      maior_lista_sem_adjacencias = checar_adjacencias(vertices_n_adjacentes_i)
      for cada in maior_lista_sem_adjacencias:
        cores[cada] = cont
        indice = ordenado.index(cada) #descobrir o indice em ordenado 
        estados[indice] = True # para marcar como "True"
      cont += 1 #mudar de cor
    else: # no caso de ter sido pintado
      continue # voltar ao loop
  print(cores) # imprimir meu dicionario com vertices e cores
  numero_cromatico = 0
  for valor in cores.values():
    if valor > numero_cromatico:
      numero_cromatico = valor
  print('Número cromático do grafo: %d'%numero_cromatico)


"""
    EXEMPLO DE ENTRADA
a b c d   = vertices
b c       = vertices adjacentes a A
a c d     = vertices adjacentes a B
a b       = vertices adjacentes a C
b         = vertices adjacentes a D
"""
grafo = {}
entrada = input("Digite os vértices separados por um espaço: ").split()
#loop para criar um dicionario com os vertices nas chaves. Seus valores serão uma lista com cada uma de suas adjacencias
for i in range(len(entrada)):
  adj = input('Digite, separando por um espaço, as adjacencias do vertice %s: '%(entrada[i])).split()
  grafo[entrada[i]] = adj
welsh_powell(grafo)
