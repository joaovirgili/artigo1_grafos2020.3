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

    def __eq__(self, obj):
        return isinstance(obj, Vertice) and obj.id == self.id


class Node:
    # pai = Node()
    # filho_e = Node()
    # filho_d = Node()

    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas
        self.verticesNaoConectados = vertices

    def __eq__(self, obj):
        if not isinstance(obj, Node):
            return False
        self.vertices = sorted(self.vertices, key=id)
        obj.vertices = sorted(obj.vertices, key=id)
        #self.arestas = sorted(self.arestas, key=id)
        #obj.arestas = sorted(obj.arestas, key=id)
        return obj.vertices == self.vertices #and obj.arestas == self.arestas

class ArestaArvore:
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

class Arvore:
    nos = []
    arestasArvore = []
    # def __init__(self):
        # self.root = root
        # self.largura = largura



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


def printArvore(arvore):
    texto = ""
    for no in arvore.nos:
        textoNo = ""
        for aresta in no.arestas:
            textoNo = "{0}{1} | ".format(textoNo, aresta)
        texto = "{0}{1}\n".format(texto, textoNo)

    print(texto)


def deveAdicionar(novoNo, nos):
    if len(nos) == 0:
        return True
    for aresta in novoNo.arestas:
        flag = True
        for no in nos:
            if existeNaLista(aresta, no.arestas):
                flag = False
                break
        if flag == True:
            return True
    return False

def existeNoPrecisaConectar(no, nos):
    return no


def calculaArestasArvore(nos):
    arestasNos = []
    noArbitrario = nos[random.randint(0, len(nos))]
    noConectar = existeNoPrecisaConectar(noArbitrario, nos)
    # if noConectar is not None:
        #conecta o nó e finaliza a rodada
        # arestasNos.append()
        #continue
    return []

class NodesContendoVertice:
    def __init__(self, node, vertices):
        self.node = node
        self.vertices = vertices

    def __eq__(self, obj):
        return isinstance(obj, NodesContendoVertice) and obj.node == self.node

    def addVertice(self, vertice):
        if not vertice.__class__ == Vertice.__class__:
            return
        self.vertices.append(vertice)

def getQuantidadeArestasNoArvore(node, arvore):
    cont = 0
    for aresta in arvore.arestasArvore:
        if aresta.no1 == node or aresta.no2 == node:
            cont = cont + 1
    return cont


def criaArestaNaArvore(noNovo, nos, arvore):

    #adiciono o noNovo como filho de uma das tais interseções.

    #para cada vértice v em noNovo, busco na árvore todos os Nós com aquele vértice
    listaNodesContendoVertices = []
    for v in noNovo.vertices:
        for no in nos:
            for ver in no.vertices:
                if v == ver:
                    n = NodesContendoVertice(no, [v])
                    if listaNodesContendoVertices.__contains__(n):
                        for item in listaNodesContendoVertices:
                            if item == no:
                                item.addVertice(v)
                                break
                    else:
                        listaNodesContendoVertices.append(n)
                    break
        #listaNodesContendoVertices.append(NodesContendoVertice(nosComV, v))
    if len(listaNodesContendoVertices) == 0:
        return None #not possible to find any node with any vertex v of noNovo

    #encontro então a maior interseção entre todos os resultados das buscas para atender o méximo de vértices v de noNovo
    maior = 0
    indexParaNoPai = -1
    for i in range(len(listaNodesContendoVertices)):
        nodeComVertices = listaNodesContendoVertices.__getitem__(i)
        if nodeComVertices.node.__eq__(noNovo):
            continue
        if getQuantidadeArestasNoArvore(nodeComVertices.node, arvore) >= 3:
            continue
        qtdVertices = len(nodeComVertices.vertices)
        if maior < qtdVertices:
            maior = qtdVertices
            indexParaNoPai = i

    if indexParaNoPai == -1:
        return None
    #agora eu adiciono o no indexado por indexParaNoPai como pai de noNovo
    aresta = ArestaArvore(noNovo, nos.__getitem__(indexParaNoPai))

    # print("Nó 1: vértices: ")
    # for a in aresta.no1.vertices:
    #     print(a)
    return aresta



def tree_decomposition(k, grafo):
    arvore = Arvore()
    nosLivres = []
    # print(temTodosOsVertices(nos, grafo.vertices))
    # print(temTodasAsArestas(nos, grafo.arestas))
    while (True):
        no = criarNo(k, grafo)
        if not deveAdicionar(no, arvore.nos):
            continue
        arvore.nos.append(no)
        nosLivres.append(no)
        for no in nosLivres:
            aresta = criaArestaNaArvore(no, arvore.nos, arvore)
            if aresta is not None:
                arvore.arestasArvore.append(aresta)
                nosLivres.remove(no)

        if temTodosOsVertices(arvore.nos, grafo.vertices) and temTodasAsArestas(arvore.nos, grafo.arestas):
            for no in nosLivres:
                aresta = criaArestaNaArvore(no, arvore.nos, arvore)
                if aresta is not None:
                    arvore.arestasArvore.append(aresta)
                    nosLivres.remove(no)
            if len(nosLivres) == 0:
                break
            else:
                print("Erro: não foi possível criar uma árvore. Tente novamente.")

    printArvore(arvore)
    #arestas = calculaArestasArvore(nosLivres)


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
