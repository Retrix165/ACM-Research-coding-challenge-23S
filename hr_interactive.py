"""
MY CODE

IDEA: Visualize an HR diagram of the stars, then, given user input of new star data, find closest star to input and output likely type

"""
from matplotlib import pyplot as plt
import pandas as pd

def main():
    data = pd.read_csv("star_info.csv")
    print("Click on left graph within the axes to show closest point")
    hr_diagram(data)
    plt.connect("button_click_event", on_click)

#Sets up and displays attempt at HR Diagram
#Missing: combined double axes on single figure, organization of spectral classes on upper x-axis
def hr_diagram(data):
    graph, (ax1,ax2) = plt.subplots(1,2)
    ax1.scatter(data["Temperature (K)"], data["Luminosity(L/Lo)"])
    ax1.set_yscale("log")

    ax1.invert_xaxis()
    ax1.set_title("HR Diagram")
    ax1.set_ylabel("Luminosity (L/Lo)")
    ax1.set_xlabel("Temperature (K)")

    ax2.scatter(data["Spectral Class"][::-1], data["Absolute magnitude(Mv)"][::-1],color="#FF0000")
    ax2.set_xlabel("Spectral Class")
    ax2.set_ylabel("Absolute magnitude(Mv)")
    ax2.xaxis.tick_top()
    ax2.invert_yaxis()
    ax2.yaxis.set_ticks_position("right")
    ax2.yaxis.set_label_position("right")
    ax2.xaxis.set_label_position("top")

    graph.tight_layout()
    plt.show()

def on_click(event):
    print('Event received:',event.x,event.y)

main()

