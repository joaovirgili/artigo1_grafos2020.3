class Caminho:
    tamanho = 0

    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas


class Ciclo:
    tamanho = 0

    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas


class Associacao:
    def __init__(self, nodeDominio, valor):
        self.nodeDominio = nodeDominio
        self.valor = valor


class Configuracao:
    def __init__(self, verticesDominio, associacoes):
        self.associacoes = associacoes
        self.verticesDominio = verticesDominio


class Realizacao:
    def __init__(self, subgrafo, caminhos, ciclos):
        self.subgrafo = subgrafo
        self.caminhos = caminhos
        self.ciclos = ciclos
        self.peso = 0
        for caminho in caminhos:
            self.peso += caminho.tamanho
        for ciclo in ciclos:
            self.peso += ciclo.tamanho

# cada vértice da árvore precisa ter uma lista de soluções parciais


class SolucaoParcial:
    def __init__(self, configuracao, d_realizacao):
        self.d_configuracao = configuracao
        self.d_realizacao = d_realizacao


def obterListaDeSolucoesNode(node, d_configuracao):
    # testar se não tem filhos ou se só tem um
    t1 = node.filhoEsq
    t2 = node.filhoDir

    l1 = t1.solucoesParciais
    l2 = t2.solucoesParciais

#    for solucaoL1 in l1:
#        for solucaoL2 in l2:


def calculaTodasSolucoesParciais(arvore):
    arvore = 1
