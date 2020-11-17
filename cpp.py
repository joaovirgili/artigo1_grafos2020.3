# importlib.import_module('random')
import random

class Grafo:
    def __init__(self, vertices, arestas, arcos):
        self.vertices = vertices
        self.arestas = arestas
        self.arcos = arcos

class Aresta:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.id = v1.id + v2.id

class Arco:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Vertice:
    def __init__(self, id):
        self.id = id

    def display(self):
        print(self.id)

class Node:
    # pai = Node()
    # filho_e = Node()
    # filho_d = Node()

    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas

class Arvore:
    def __init__(self, root, largura):
        self.root = root
        self.largura = largura

def vizinhosDoVertice(grafo, verticeId, outroId):
    # Retornar um subgrafo com vertices e arestas
    vizinhos = []

    for aresta in grafo.arestas:
        if aresta.v1.id == verticeId and aresta.v2.id != outroId:
            vizinhos.append(aresta.v2)
        elif aresta.v2.id == verticeId and aresta.v1.id != outroId:
            vizinhos.append(aresta.v1)

    return vizinhos

def criarNo(k, grafo):
    randomAresta = grafo.arestas[random.randint(0, len(grafo.arestas) - 1)]
    randomVertice = randomAresta.v1 if random.randint(0, 1) == 0 else randomAresta.v2
    outroVertice = randomAresta.v2 if randomVertice.id == randomAresta.v1.id else randomAresta.v1

    print("randomVertice: " + randomVertice.id)
    print("outroVerice: " + outroVertice.id)

    no = Node([randomVertice, outroVertice], [randomAresta])
    vizinhos = vizinhosDoVertice(grafo, randomVertice.id, outroVertice.id)
    print("vizinhos:")
    for v in vizinhos:

        v.display()
    
    max = k if k < len(vizinhos) else len(vizinhos)
    vizinhoCount = random.randint(0, max) # Quantidade de vizinhos que serao adicionados a bag

    print("vizinhoCount: " + str(vizinhoCount))

    for i in range(vizinhoCount):
        verticeIndex = random.randint(0, len(vizinhos) -1)
        verticeVizinho = vizinhos[verticeIndex]

        no.vertices.append(verticeVizinho)
        del vizinhos[verticeIndex]

    print("vizinhos:")
    for v in vizinhos:
        v.display()

    print("vertices do no")
    for v in no.vertices:
        v.display()

    return no

def temTodosOsVertices(nos, vertices):
    for v in vertices:
        flag = False
        for no in nos:
            if flag == True:
                break
            for v1 in no.vertices:
                if v1.id == v.id:
                    flag = True
                    break
        if not flag:
            return flag

    return True

def temTodasAsArestas(nos, arestas):
    for v in arestas:
        flag = False
        for no in nos:
            if flag == True:
                break
            for v1 in no.arestas:
                if v1.id == v.id:
                    flag = True
                    break
        if not flag:
            return flag

    return True

def tree_decomposition(k, grafo):
    # arvore = Arvore()
    nos = []
    criarNo(k, grafo)
    # while (true):
    #     no = criarNo(k, grafo)
    #     nos.append(no)
    #     if temTodosOsVertices(nos, grafos.vertices) and temTodasAsArestas(nos, grafos.arestas):
    #         print("asd")

v1 = Vertice("v1")
v2 = Vertice("v2")
v3 = Vertice("v3")
arco1 = Arco(v1, v2) #v1v2
aresta1 = Aresta(v1, v2) #v1v2
aresta2 = Aresta(v2, v3) #v2v3

vertices = [v1, v2]
arestas = [aresta1, aresta2]
arcos = [arco1]

grafo = Grafo(vertices, arestas, arcos)

tree_decomposition(1, grafo)
