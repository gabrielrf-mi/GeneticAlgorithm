import matplotlib.pyplot as plt

def plot(caminho, grafo):
    plt.figure(1)
    im = plt.imread("mapa.PNG")
    plt.imshow(im, zorder=1)
    x = []
    y = []
    for no in caminho:
        plt.scatter(no.x, no.y, zorder=3, color='#1f77b4')
        x.append(no.x)
        y.append(no.y)

    plotNos(grafo, plt)
    plt.plot(x, y, label='line 2')

    plotCaminhosPossiveis(grafo, plt)

    plt.show()

def plotNos(grafo, plot):

    for no in grafo:
        plot.scatter(no.x, no.y, zorder=3, color='#1f77b4')



def plotCaminhosPossiveis(grafo, plt):

    plt.figure(2)
    im = plt.imread("mapa.PNG")
    plt.imshow(im, zorder=1)

    for no in grafo:
        for vizinho in no.vizinhos:
            plt.plot([no.x, vizinho.x], [no.y, vizinho.y], label='line 2')

    plt.show()
