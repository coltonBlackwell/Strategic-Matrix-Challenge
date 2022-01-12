import matplotlib.pyplot as plt
import matplotlib.pyplot as xyz



def graphicGame(x1, x2, y1, y2, secondsList2, secondsList, gameNumber, gameStyle):
    plt.clf()
    plt.plot(x1, x2, "^-", label="User values")
    if gameStyle == "AI":
        plt.plot(y1, y2, "o:", label="AI values")
    plt.plot(secondsList2, secondsList, "s--", label="seconds each time")
    plt.legend()
    plt.title("Graphic Game {}".format(gameNumber))
    plt.savefig("GraphicGame{}.png".format(gameNumber))