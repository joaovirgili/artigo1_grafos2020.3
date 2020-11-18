# importlib.import_module('random')
import random


def existeNaLista(aresta, lista):
    try:
        lista.index(aresta)
        return True
    except:
        return False


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

    def __eq__(self, obj):
        return isinstance(obj, Aresta) and ((obj.v1 == self.v1 and obj.v2 == self.v2) or (obj.v2 == self.v1 and obj.v1 == self.v2))

    def __str__(self):
        return "E({0}, {1})".format(self.v1.id, self.v2.id)


class Arco:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


class Vertice:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "V({0})".format(self.id)


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
    vizinhos = []
    arestas = []

    for aresta in grafo.arestas:
        if aresta.v1.id == verticeId and aresta.v2.id != outroId:
            arestas.append(aresta)
            vizinhos.append(aresta.v2)
        elif aresta.v2.id == verticeId and aresta.v1.id != outroId:
            arestas.append(aresta)
            vizinhos.append(aresta.v1)

    return Grafo(vizinhos, arestas, [])


def criarNo(k, grafo):
    randomAresta = grafo.arestas[random.randint(0, len(grafo.arestas) - 1)]
    randomVertice = randomAresta.v1 if random.randint(
        0, 1) == 0 else randomAresta.v2
    outroVertice = randomAresta.v2 if randomVertice.id == randomAresta.v1.id else randomAresta.v1

    no = Node([randomVertice, outroVertice], [randomAresta])
    subgrafo = vizinhosDoVertice(grafo, randomVertice.id, outroVertice.id)

    max = k if k < len(subgrafo.vertices) else len(subgrafo.vertices)

    # Quantidade de vizinhos que serao adicionados a bag
    vizinhoCount = random.randint(0, max)

    for i in range(vizinhoCount):
        verticeIndex = random.randint(0, len(subgrafo.vertices) - 1)
        verticeVizinho = subgrafo.vertices[verticeIndex]

        no.vertices.append(verticeVizinho)
        no.arestas.append(Aresta(verticeVizinho, randomVertice))

        del subgrafo.vertices[verticeIndex]

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
    for a in arestas:
        flag = False
        for no in nos:
            if flag == True:
                break
            for a1 in no.arestas:
                if a1 == a:
                    flag = True
                    break
        if not flag:
            return flag

    return True


def printArvore(nos):
    texto = ""
    for no in nos:
        textoNo = ""
        for aresta in no.arestas:
            textoNo = "{0}{1} | ".format(textoNo, aresta)
        texto = "{0}{1}\n".format(texto, textoNo)

    print(texto)


def deveAdicionar(novoNo, nos):

    for aresta in novoNo.arestas:
        flag = True
        for no in nos:
            if existeNaLista(aresta, no.arestas):
                flag = False
                break
        if flag == True:
            return True
    return False


def tree_decomposition(k, grafo):
    # arvore = Arvore()
    nos = []
    # print(temTodosOsVertices(nos, grafo.vertices))
    # print(temTodasAsArestas(nos, grafo.arestas))
    while (True):
        no = criarNo(k, grafo)
        if len(nos) == 0 or deveAdicionar(no, nos):
            nos.append(no)
            if temTodosOsVertices(nos, grafo.vertices) and temTodasAsArestas(nos, grafo.arestas):
                break

    printArvore(nos)


v1 = Vertice("v1")
v2 = Vertice("v2")
v3 = Vertice("v3")
v4 = Vertice("v4")
v5 = Vertice("v5")
v6 = Vertice("v6")

aresta1 = Aresta(v1, v2)
aresta2 = Aresta(v2, v3)
aresta3 = Aresta(v3, v1)

aresta4 = Aresta(v3, v4)
aresta5 = Aresta(v4, v1)
aresta6 = Aresta(v6, v3)
aresta7 = Aresta(v5, v1)

vertices = [v1, v2, v3, v4, v5, v6]
arestas = [aresta1, aresta2, aresta3, aresta4, aresta5, aresta6, aresta7]
arcos = []

grafo = Grafo(vertices, arestas, arcos)


tree_decomposition(1, grafo)
