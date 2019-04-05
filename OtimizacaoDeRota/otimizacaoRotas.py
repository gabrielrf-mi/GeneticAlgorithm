import random
from plot import *

TAXA_MUTACAO = 0.01
TAXA_CRUZAMENTO = 0.9
TAMANHO_POPULACAO = 1000
NUMERO_GERACOES = 5000


class no:
    def __init__(self, x, y, vizinhos=[]):
        self.x = x
        self.y = y
        self.vizinhos = vizinhos

    def addVizinho(self, vizinho):
        self.vizinhos = self.vizinhos + [vizinho]
        vizinho.vizinhos = vizinho.vizinhos + [self]

    def vizinhoAleatorio(self):
        return self.vizinhos[random.randint(0, len(self.vizinhos) - 1)]

    def aindaTemVizinhosForaDessaLista(self, lista):
        for vizinho in self.vizinhos:
            if vizinho not in lista:
                return True
        return False

    def __repr__(self):
        return '(%i,%i)' % (self.x, self.y)


class grafo:
    def __init__(self):
        self.grafo = []

    def posicao(self, x, y):
        for i in range(0, len(self.grafo)):
            if x == self.grafo[i].x and y == self.grafo[i].y:
                return i
        return None

    def ligarNos(self, x1, y1, x2, y2):

        indexNoUm = self.posicao(x1, y1)
        indexNoDois = self.posicao(x2, y2)

        if indexNoUm is None:
            self.grafo = self.grafo + [no(x1, y1)]
            indexNoUm = len(self.grafo)-1

        if indexNoDois is None:
            self.grafo = self.grafo + [no(x2, y2)]
            indexNoDois = len(self.grafo)-1

        self.grafo[indexNoUm].addVizinho(self.grafo[indexNoDois])


# Cria o Grafo
grafo = grafo()

# No momento que você liga os nos eles já são criados automaticamente
# Para ligar dois nos usem a funçao da classe grafo ligarNos(x1, y1, x2, y2)
# EX: Supondo que temos dois nos: (1, 0) e (2,0)
# Criamos ali em cima um grafo chamado de grafo
# Para liga-los basta fazer grafo.ligarNos(1,0,2,0)

grafo.ligarNos(78, 421, 78, 262)
grafo.ligarNos(78, 262, 139, 262)
grafo.ligarNos(139, 262, 139, 106)
grafo.ligarNos(139, 262, 176, 262)
grafo.ligarNos(176, 262, 176, 418)
grafo.ligarNos(176, 418, 78, 421)
grafo.ligarNos(176, 262, 217, 262)
grafo.ligarNos(217, 262, 217, 106)
grafo.ligarNos(139, 106, 217, 106)
grafo.ligarNos(217, 262, 253, 262)
grafo.ligarNos(253, 262, 253, 418)
grafo.ligarNos(253, 262, 295, 263)
grafo.ligarNos(295, 263, 295, 106)
grafo.ligarNos(217, 106, 295, 106)
grafo.ligarNos(295, 263, 332, 263)
grafo.ligarNos(332, 263, 332, 418)
grafo.ligarNos(253, 418, 332, 418)
grafo.ligarNos(332, 263, 371, 263)
grafo.ligarNos(371, 263, 371, 106)
grafo.ligarNos(295, 106, 371, 106)
grafo.ligarNos(371, 263, 437, 263)
grafo.ligarNos(437, 263, 437, 418)
grafo.ligarNos(176, 418, 253, 418)
grafo.ligarNos(332, 418, 437, 418)
grafo.ligarNos(437, 263, 525, 266)
grafo.ligarNos(525, 266, 527, 315)
grafo.ligarNos(527, 315, 485, 389)
grafo.ligarNos(485, 389, 485, 419)
grafo.ligarNos(485, 389, 600, 372)
grafo.ligarNos(437, 418, 485, 419)
grafo.ligarNos(527, 315, 600, 372)
grafo.ligarNos(485, 419, 488, 449)
grafo.ligarNos(488, 449, 660, 449)
grafo.ligarNos(660, 449, 663, 370)
grafo.ligarNos(663, 370, 600, 372)
grafo.ligarNos(660, 449, 751, 449)
grafo.ligarNos(751, 449, 758, 368)
grafo.ligarNos(758, 368, 663, 370)
grafo.ligarNos(525, 266, 576, 268)
grafo.ligarNos(576, 268, 578, 299)
grafo.ligarNos(578, 299, 763, 307)
grafo.ligarNos(763, 307, 758, 368)
grafo.ligarNos(758, 368, 790, 336)
grafo.ligarNos(763, 307, 790, 336)
grafo.ligarNos(790, 336, 1012, 360)
grafo.ligarNos(1012, 360, 1131, 360)
grafo.ligarNos(1131, 360, 1175, 391)
grafo.ligarNos(332, 418, 334, 520)
grafo.ligarNos(253, 418, 258, 511)
grafo.ligarNos(334, 520, 258, 511)
grafo.ligarNos(258, 511, 144, 500)
grafo.ligarNos(258, 511, 267, 645)
grafo.ligarNos(144, 500, 176, 418)
grafo.ligarNos(267, 645, 136, 628)
grafo.ligarNos(136, 628, 32, 616)
grafo.ligarNos(136, 628, 144, 500)
grafo.ligarNos(258, 511, 47, 491)
grafo.ligarNos(32, 616, 47, 491)
grafo.ligarNos(47, 491, 50, 418)
grafo.ligarNos(78, 421, 50, 418)
grafo.ligarNos(50, 418, 58, 261) 
grafo.ligarNos(58, 261, 53, 107) 
grafo.ligarNos(53, 107, 139, 106) 
grafo.ligarNos(58, 261, 78, 262) 
grafo.ligarNos(267, 645, 427, 662)
grafo.ligarNos(427, 662, 441, 530)
grafo.ligarNos(441, 530, 334, 520)
grafo.ligarNos(441, 530, 488, 533)
grafo.ligarNos(488, 533, 627, 549)
grafo.ligarNos(488, 533, 488, 449)
grafo.ligarNos(427, 662, 614, 678)
grafo.ligarNos(614, 678, 627, 549)
grafo.ligarNos(371, 106, 583, 106)
grafo.ligarNos(583, 106, 576, 268)
grafo.ligarNos(627, 549, 743, 560)
grafo.ligarNos(614, 678, 732, 682)
grafo.ligarNos(732, 682, 743, 560)
grafo.ligarNos(743, 560, 751, 449)
grafo.ligarNos(751, 449, 783, 421)
grafo.ligarNos(758, 368, 783, 421)
grafo.ligarNos(783, 421, 908, 437)
grafo.ligarNos(908, 437, 1012, 360)
grafo.ligarNos(732, 682, 871, 696)
grafo.ligarNos(871, 696, 1009, 619)
grafo.ligarNos(1009, 619, 1012, 360)
grafo.ligarNos(1009, 619, 1237, 461)
grafo.ligarNos(871, 696, 1236, 735)
grafo.ligarNos(1237, 461, 1236, 735)
grafo.ligarNos(1237, 461, 1237, 390)
grafo.ligarNos(1237, 390, 1175, 391)


# Coloca o no de inicio e fim nas funcoes grafo.index(x,y)
LOCAL_ATUAL = grafo.grafo[grafo.posicao(78, 262)]
DCA = grafo.grafo[grafo.posicao(1175, 391)]


INICIO = LOCAL_ATUAL
FINAL = DCA


class cromossomo:
    def __init__(self, caminho=[]):
        self.caminho = caminho if caminho != [] else self.criarAletorio(INICIO, FINAL)

    def criarAletorio(self, inicio, final):
        if inicio == final:
            return [inicio]

        visitados = [inicio]
        caminhoAleatorio = [inicio]

        while caminhoAleatorio[-1] != final:
            while not caminhoAleatorio[-1].aindaTemVizinhosForaDessaLista(visitados):
                caminhoAleatorio.pop()
            proximoNo = caminhoAleatorio[-1].vizinhoAleatorio()
            while proximoNo in visitados:
                proximoNo = caminhoAleatorio[-1].vizinhoAleatorio()
            caminhoAleatorio = caminhoAleatorio + [proximoNo]
            visitados = visitados + [proximoNo]
        return caminhoAleatorio

    def mutacao(self):
        inicial = random.randint(0, len(self.caminho) - 1)
        final = random.randint(inicial, len(self.caminho) - 1)
        if inicial != final:
            novoCaminho = self.criarAletorio(self.caminho[inicial], self.caminho[final])
            self.caminho = self.caminho[:inicial] + novoCaminho + self.caminho[final + 1:]

    def cruzamento(self, parceiro):
        inter = [x for x in self.caminho if x in parceiro.caminho]
        noEscolhido = inter[random.randint(0, len(inter) - 1)]
        if noEscolhido:
            filhoUm = cromossomo(
                self.caminho[:self.caminho.index(noEscolhido)] + parceiro.caminho[parceiro.caminho.index(noEscolhido):])
            filhoDois = cromossomo(
                parceiro.caminho[:parceiro.caminho.index(noEscolhido)] + self.caminho[self.caminho.index(noEscolhido):])
        return filhoUm, filhoDois

    def fitness(self):
        custo = 0
        for i in range(0, len(self.caminho) - 1):
            custo += ((self.caminho[i].x - self.caminho[i + 1].x)**2 + (
                        self.caminho[i].y - self.caminho[i + 1].y)**2)**0.5
        return custo

    def __repr__(self):
        return self.caminho.__repr__()


def torneio(populacao):
    novaPopulacao = []
    for i in range(len(populacao)):
        candidatoUm = random.randint(0, len(populacao) - 1)
        candidatoDois = random.randint(0, len(populacao) - 1)
        candidatoTres = random.randint(0, len(populacao) - 1)
        disputa = [populacao[candidatoUm], populacao[candidatoDois], populacao[candidatoTres]]
        disputa = sorted(disputa, key=lambda cromossomo: cromossomo.fitness())

        novaPopulacao = novaPopulacao + [disputa[0]]

    return novaPopulacao


def elitismo(populacao, quantidadeDesejada):
    return sorted(populacao, key=lambda cromossomo: cromossomo.fitness())[0:quantidadeDesejada - 1]


def coeficienteDeVariancia(populacao):
    media = 0
    tamanho = len(populacao)
    for individuo in populacao:
        # print(individuo.caminho)
        media += individuo.fitness()
    media /= tamanho
    desvioPadrao = 0
    for individuo in populacao:
        desvioPadrao += (media - individuo.fitness()) ** 2
    desvioPadrao /= (tamanho - 1)
    desvioPadrao = desvioPadrao ** 0.5
    cv = desvioPadrao / abs(media)

    return cv


populacao = [cromossomo() for i in range(0, TAMANHO_POPULACAO)]

geracao = 0

while geracao < NUMERO_GERACOES and coeficienteDeVariancia(populacao) > 0.001:
    geracao += 1

    for i in populacao:
        print(i)
    populacao = torneio(populacao)
    novaGeracao = []
    for i in range(TAMANHO_POPULACAO):
        if random.random() < TAXA_CRUZAMENTO:
            pai = random.randint(0, len(populacao) - 1)
            mae = random.randint(0, len(populacao) - 1)
            while mae == pai:
                mae = random.randint(0, len(populacao) - 1)
            filhoUm, filhoDois = populacao[pai].cruzamento(populacao[mae])
            novaGeracao = novaGeracao + [filhoUm]
            novaGeracao = novaGeracao + [filhoDois]

    for novoIndividuo in novaGeracao:
        if random.random() < TAXA_MUTACAO:
            novoIndividuo.mutacao()

    populacao = elitismo(populacao + novaGeracao, TAMANHO_POPULACAO)

print("final: ", populacao[0].caminho)

plot(populacao[0].caminho, grafo.grafo)


