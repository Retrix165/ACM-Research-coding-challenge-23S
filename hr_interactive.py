"""
MY CODE

IDEA: Visualize an HR diagram of the stars, then, given user input of new star data, find closest star to input and output likely type

"""
from matplotlib import pyplot as plt
import pandas as pd

#Sets up and displays attempt at HR Diagram
#Missing: combined double axes on single figure, organization of spectral classes on upper x-axis
def hr_diagram(data):

    ax.scatter(data["Temperature (K)"], data["Luminosity(L/Lo)"])
    ax.set_yscale("log")

    ax.invert_xaxis()
    ax.set_title("HR Diagram")
    ax.set_ylabel("Luminosity (L/Lo)")
    ax.set_xlabel("Temperature (K)")
    graph.tight_layout()
    
    graph.canvas.mpl_connect("button_press_event", on_click)
    plt.show()

#Event for displaying line to closest star
def on_click(event):
    curs_x, curs_y = event.xdata, event.ydata
    if curs_x is not None and curs_y is not None:
        ax_twin.clear()
        points = [[curs_x],[curs_y]]
        closest_point = get_closest_point(curs_x, curs_y, data["Temperature (K)"], data["Luminosity(L/Lo)"])
        print("The closest star to your click has a temperature of %d K and a luminosity of %1.5f L/Lo!" % (closest_point[0], closest_point[1]))
        points[0].append(closest_point[0])
        points[1].append(closest_point[1])
        ax_twin.plot(points[0],points[1], color="#FF0000")
        ax_twin.set_yscale("log")
        ax_twin.set_ybound(ax.get_ybound())
        plt.draw()

def get_closest_point(x, y, dom, ran):
    def dist_calc(x1, y1):
        return (x-x1) ** 2 + (y-y1) ** 2
    assert(len(dom) == len(ran))
    min_x, min_y = dom[0], ran[0]
    min_dist = dist_calc(min_x,min_y)
    for i in range(1,len(dom)):
        if dist_calc(dom[i], ran[i]) < min_dist:
            min_x = dom[i]
            min_y = ran[i]
            min_dist = dist_calc(dom[i],ran[i])
    return (min_x,min_y)
        
graph, ax = plt.subplots()
ax_twin = ax.twinx()

data = pd.read_csv("star_info.csv")
print("Click on left graph within the axes to show closest point")
hr_diagram(data)
