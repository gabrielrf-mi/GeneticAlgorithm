import random
from plot import *
TAXA_MUTACAO = 0.01
TAXA_CRUZAMENTO = 0.9
TAMANHO_POPULACAO = 50
NUMERO_GERACOES = 20


class no:
    def __init__(self,x,y,vizinhos=[]):
        self.x=x
        self.y=y
        self.vizinhos=vizinhos

    def addVizinho(self,vizinho):
        self.vizinhos=self.vizinhos+[vizinho]
        vizinho.vizinhos=vizinho.vizinhos+[self]


    def vizinhoAleatorio(self):
        return self.vizinhos[random.randint(0,len(self.vizinhos)-1)]

    def aindaTemVizinhosForaDessaLista(self, lista):
        for vizinho in self.vizinhos:
            if not lista.__contains__(vizinho):
                return True
        return False
    def __repr__(self):
        return '(%i,%i)' % (self.x,self.y)

class grafo:
    def __init__(self):
        self.grafo=[]

    def posicao(self, x, y):
        for i in range(0, len(self.grafo)):
            if x == self.grafo[i].x and y == self.grafo[i].y:
                return i

        return None

    def ligarNos(self, x1, y1, x2, y2):

        indexNoUm = self.posicao(x1, y1)
        indexNoDois = self.posicao(x2, y2)

        if not indexNoUm:
            no1 = no(x1, y1)
            self.grafo.append(no1)
        else:
            no1 = self.grafo[indexNoUm]
        if not indexNoDois:
            no2 = no(x2, y2)
            self.grafo.append(no2)
        else:
            no2 = self.grafo[indexNoDois]

        no1.addVizinho(no2)



# Cria o Grafo
grafo = grafo()

# No momento que você liga os nos eles já são criados automaticamente
# Para ligar dois nos usem a funçao da classe grafo ligarNos(x1, y1, x2, y2)
# EX: Supondo que temos dois nos: (1, 0) e (2,0)
# Criamos ali em cima um grafo chamado de grafo
# Para liga-los basta fazer grafo.ligarNos(1,0,2,0)

grafo.ligarNos(78,421,78,262)
grafo.ligarNos(78,262,139,262)
grafo.ligarNos(139,262,139,106)
grafo.ligarNos(78,262,176,262)
grafo.ligarNos(176,262,176,418)
grafo.ligarNos(78,421,176,418)
grafo.ligarNos(176,262,217,262)
grafo.ligarNos(217,262,217,106)
grafo.ligarNos(139,106,217,106)
grafo.ligarNos(217,262,253,262)
grafo.ligarNos(253,262,253,418)
grafo.ligarNos(253,262,295,263)
grafo.ligarNos(295,263,295,106)
grafo.ligarNos(217,106,295,106)
grafo.ligarNos(295,263,332,263)
grafo.ligarNos(332,263,332,418)
grafo.ligarNos(253,418,332,418)
grafo.ligarNos(332,263,371,263)
grafo.ligarNos(371,263,371,106)
grafo.ligarNos(295,106,371,106)
grafo.ligarNos(371,263,437,263)
grafo.ligarNos(437,263,437,418)

# Coloca o no de inicio e fim nas funcoes grafo.index(x,y)
INICIO = grafo.grafo[grafo.posicao(78,421)]
FINAL = grafo.grafo[grafo.posicao(437,418)]



class cromossomo:
    def __init__(self,caminho=[]):
        self.caminho = caminho if caminho != [] else self.criarAletorio(INICIO,FINAL)

    def criarAletorio(self,inicio,final):
        if inicio == final:
            return [inicio]
        noAtual=inicio
        caminhoAleatorio=[noAtual]
        while noAtual!=final and noAtual.aindaTemVizinhosForaDessaLista(caminhoAleatorio):
            proximoNo=noAtual.vizinhoAleatorio()
            while caminhoAleatorio.__contains__(proximoNo):
                proximoNo=noAtual.vizinhoAleatorio()
            noAtual=proximoNo
            caminhoAleatorio=caminhoAleatorio+ [noAtual]
        if caminhoAleatorio[-1] != final:
            return self.criarAletorio(inicio,final)
        return caminhoAleatorio

    def mutacao(self):
        inicial=random.randint(0,len(self.caminho)-1)
        final=random.randint(inicial,len(self.caminho)-1)
        if inicial != final:
            novoCaminho=self.criarAletorio(self.caminho[inicial],self.caminho[final])
            self.caminho=self.caminho[:inicial] + novoCaminho + self.caminho[final+1:]

    def cruzamento(self,parceiro):
        inter = [x for x in self.caminho if x in parceiro.caminho]
        noEscolhido= inter[random.randint(0,len(inter)-1)]
        if noEscolhido :
            filhoUm = cromossomo(self.caminho[:self.caminho.index(noEscolhido)]+parceiro.caminho[parceiro.caminho.index(noEscolhido):])
            filhoDois = cromossomo(parceiro.caminho[:parceiro.caminho.index(noEscolhido)]+self.caminho[self.caminho.index(noEscolhido):])
        return filhoUm,filhoDois

    def fitness(self):
        custo = 0
        for i in range(0,len(self.caminho)-1):
            custo += ((self.caminho[i].x-self.caminho[i+1].x)**2+(self.caminho[i].y-self.caminho[i+1].y)**2)**0.5       
        return custo

    def __repr__(self):
        return self.caminho.__repr__()


def torneio(populacao):
    novaPopulacao = []
    for i in range(len(populacao)):
        candidatoUm = random.randint(0,len(populacao)-1)    
        candidatoDois = random.randint(0,len(populacao)-1)    
        candidatoTres = random.randint(0,len(populacao)-1)
        disputa = [populacao[candidatoUm],populacao[candidatoDois],populacao[candidatoTres]]
        disputa = sorted(disputa, key=lambda cromossomo: cromossomo.fitness())

        novaPopulacao.append(disputa[0])

    return novaPopulacao

def elitismo(populacao,quantidadeDesejada):
    return sorted(populacao, key=lambda cromossomo: cromossomo.fitness())[0:quantidadeDesejada-1]


def coeficienteDeVariancia(populacao):
    media = 0
    tamanho=len(populacao)
    for individuo in populacao:
        # print(individuo.caminho)
        media += individuo.fitness()
    media/=tamanho
    desvioPadrao = 0
    for individuo in populacao:
        desvioPadrao += (media-individuo.fitness())**2
    desvioPadrao /= (tamanho-1)
    desvioPadrao = (desvioPadrao)**0.5
    cv = desvioPadrao/abs(media)

    return cv


populacao = [cromossomo() for i in range(0, TAMANHO_POPULACAO)]

geracao = 0

while geracao < NUMERO_GERACOES and coeficienteDeVariancia(populacao) > 0.001:
    geracao += 1
    populacao = torneio(populacao)
    # print(populacao)
    novaGeracao = []
    for  i in range(TAMANHO_POPULACAO):
        if random.random() < TAXA_CRUZAMENTO:
            pai = random.randint(0, len(populacao)-1)
            mae = random.randint(0, len(populacao)-1)
            # print('pai',pai,populacao[pai])
            # print(mae,populacao[mae])
            while mae == pai:
                mae = random.randint(0, len(populacao)-1)
            filhoUm,filhoDois=populacao[pai].cruzamento(populacao[mae])
            novaGeracao.append(filhoUm)
            novaGeracao.append(filhoDois)
    
    for novoIndividuo in novaGeracao:
        if random.random() < TAXA_MUTACAO:
            novoIndividuo.mutacao()

    populacao = elitismo(populacao+novaGeracao,TAMANHO_POPULACAO)

plot(populacao[0].caminho, grafo.grafo)


