import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

def plot(caminho,grafo):
    im = plt.imread("mapa.PNG")
    im2 = plt2.imread("mapa 2.PNG")

    plt.imshow(im, zorder=1)
    plt2.imshow(im2, zorder=1)

    x = []
    x2 = []
    y = []
    y2 = []

    for no in caminho:
        plt.scatter(no.x, no.y, zorder=3, color='#1f77b4')
        x.append(no.x)
        y.append(no.y)

    for no in grafo:
        plt2.scatter(no.x, no.y, zorder=3, color='#1f77b4')
        x2.append(no.x)
        y2.append(no.y)

    plt.figure(1)
    plt.plot(x, y, label='line 2')
    # plt.show()

    plt2.figure(2)
    plt2.plot(x2, y2, label='line 2')
    plt2.show()