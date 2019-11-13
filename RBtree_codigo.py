class Nodo():
  def __init__(self,cor=None,chave=None,pai=None,direita=None,esquerda=None):
    self.cor = cor
    self.chave = chave
    self.pai = pai
    self.direita = direita
    self.esquerda = esquerda
  
class Arvore_Vermelho_Preto():
  def __init__(self,raiz,nil): 
    self.raiz = Nodo(None,None,None,None,None)
    self.nil = Nodo('preto',None,None,None,None)
  
  #Rotações
  def rotacao_esquerda(self,x):
    y = x.direita
    x.direita = y.esquerda
    if y.esquerda != self.nil: 
      y.esquerda.pai = x
    y.pai = x.pai
    if x.pai == self.nil:
      self.raiz = y
    elif x == x.pai.esquerda:
      x.pai.esquerda = y
    else:
      x.pai.direita = y
    y.esquerda = x
    x.pai = y
  
  def rotacao_direita(self,x):
    y = x.esquerda
    x.esquerda = y.direita
    if y.direita != self.nil:
      y.direita.pai = x
    y.pai = x.pai
    if x.pai == self.nil:
      self.raiz = y
    elif x == x.pai.direita:
      x.pai.direita = y
    else:
      x.pai.esquerda = y
    y.direita = x
    x.pai = y
  
  #Inserir
  def arvore_inserir(self,z):
    y = self.nil
    x = self.raiz
    while x != self.nil:
      y = x
      if z.chave < x.chave:
        x = x.esquerda
      else:
        x = x.direita
    z.pai = y
    if y == self.nil:
      self.raiz = z
    elif z.chave < y.chave:
      y.esquerda = z
    else:
      y.direita = z

  def RB_inserir(self,x):
    self.arvore_inserir(self,x)
    x.cor = 'vermelho'
    while x != self.raiz and x.pai.cor == 'vermelho':
      if x.pai == x.pai.pai.esquerda:
        y = x.pai.pai.direita
        if y.cor == 'vermelho':
          x.pai.cor = 'preto'
          y.cor = 'preto'
          x.pai.pai.cor = 'vermelho'
          x = x.pai.pai
        else:
          if x == x.pai.direita:
            x = x.pai
            self.rotacao_esquerda(x)
          x.pai.cor = 'preto'
          x.pai.pai.cor = 'vermelho'
          self.rotacao_direita(x.pai.pai)
      else:
        y = x.pai.pai.esquerda
        if y.cor == 'vermelho':
          x.pai.cor = 'preto'
          y.cor = 'preto'
          x.pai.pai.cor = 'vermelho'
          x = x.pai.pai
        else:
          if x == x.pai.esquerda:
            x = x.pai
            self.rotacao_direita(x)
          x.pai.cor = 'preto'
          x.pai.pai.cor = 'vermelho'
          self.rotacao_esquerda(x.pai.pai)
    self.raiz.cor = 'preto'

  #Deletar

  def deleteFixup(self,x):
    while x != self.raiz and x.cor == 'preto':
      if x == x.pai.esquerda:
        w = x.pai.direita
        if w.cor == 'vermelho':
          w.cor = 'preto'
          x.pai.cor = 'vermelho'
          self.rotacao_esquerda(x.pai)
          w = x.pai.direita
        if w.esquerda.color == 'preto' and w.direita.cor == 'preto':
          w.cor = 'vermelho'
          x = x.pai
        else:
          if w.direita.cor == 'preto':
            w.esquerda.cor = 'preto'
            w.cor = 'vermelho'
            self.rotacao_direita(w)
            w = x.pai.direita
          w.cor = x.pai.cor
          x.pai.cor = 'preto'
          w.direita.cor = 'preto'
          self.rotacao_esquerda(x.pai)
          x = self.raiz
      else:
        w = x.pai.esquerda
        if w.cor == 'vermelho':
          w.cor = 'preto'
          x.pai.cor = 'vermelho'
          self.rotacao_direita(x.pai)
          w = x.pai.esquerda
        if w.direita.cor == 'preto' and w.esquerda.cor == 'preto':
          w.cor = 'vermelho'
          x = x.pai
        else:
          if w.esquerda.cor == 'preto':
            w.direita.cor = 'preto'
            w.cor = 'vermelho'
            self.rotacao_esquerda(w)
            w = x.pai.esquerda
          w.cor = x.pai.cor
          x.pai.cor = 'preto'
          w.esquerda.cor = 'preto'
          self.rotacao_direita(x.pai)
          x = self.raiz
    x.cor = 'preto'

  def RB_deletar(self,z):
    if not z or z == self.nil:
      return
    if z.esquerda == self.nil or z.direita == self.nil:
      y = z
    else:
      y = z.direita
      while y.esquerda != self.nil:
        y = y.esquerda
    if y.esquerda != self.nil:
      x = y.esquerda
    else:
      x = y.direita
    x.pai = y.pai
    if y.pai:
      if y == y.pai.esquerda:
        y.pai.esquerda = x
      else:
        y.pai.direita = x
    else:
      self.raiz = x
    if y != z:
      z.chave = y.chave
      z.chave = y.chave
    if y.cor == 'preto':
      self.deleteFixup(x)

