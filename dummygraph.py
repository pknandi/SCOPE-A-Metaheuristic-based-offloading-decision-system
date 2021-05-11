import matplotlib.pyplot as plt
import numpy as np


def subtaskVsLatency():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []

    for line in open('Data/subtasklatency.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Number of subtasks')
    plt.ylabel('Service Latency')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/subtasklatency.png")
    plt.show()


def subtaskVsEnergy():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('Data/subtaskenergy.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Number of subtasks')
    plt.ylabel('Energy Consumption')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/subtaskenergy.png")
    plt.show()


def subtaskVsTaskDrop():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('Data/subtaskvstaskdrop.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Number of subtasks')
    plt.ylabel('Task Drop Rate')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/subtaskvstaskdrop.png")
    plt.show()


def subtaskVsUtilCost():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('Data/subtaskutilitypercost.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    # plt.title("Number of subtasks vs Utility per Unit Cost")
    plt.xlabel('Number of subtasks')
    plt.ylabel('Utility per Unit Cost')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/subtaskutilitypercost.png")
    plt.show()


def serverVsLatency():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []

    for line in open('Data/serverlatency.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Number of Servers')
    plt.ylabel('Service Latency')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/serverlatency.png")
    plt.show()


def serverVsEnergy():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []

    for line in open('Data/servervsenergy.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Number of Servers')
    plt.ylabel('Energy Consumption')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/servervsenergy.png")
    plt.show()


def serverVsUtilityPerUnitCost():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('Data/serverutilitypercost.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Number of Servers')
    plt.ylabel('Utility per Unit Cost')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/servervsutilcost")
    plt.show()


def serverVsTaskDrop():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []

    for line in open('Data/servervstaskdrop.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Number of Servers')
    plt.ylabel('Task Drop Rate')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/servervstaskdrop.png")
    plt.show()


def serverVsTaskDropBar():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('servervstaskdrop.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    x = np.arange(len(x1))  # the label locations
    width = 0.24  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width, y4, width/2, color='g', label='SCO')
    ax.bar(x - width / 2, y1, width/2, color='navy', label='MTMS')
    ax.bar(x, y2, width/2, color='r', label='Random Assignment')
    ax.bar(x + width/2, y3, width/2, color='k', label='Greedy Assignment')

    ax.set_ylabel('Task Drop Rate')
    plt.xlabel("Number of Server")
    # ax.set_title('Task Size vs Task Drop Rate')
    ax.set_xticks(x)
    ax.set_xticklabels(x1)
    ax.legend()

    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig("servervstaskdropbar.png")
    plt.show()


def taskSizeVsLatency():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('Data/tasksizevslatency.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(float(lines[0]))
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Task Size')
    plt.ylabel('Service Latency')
    # plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.errorbar(x1, y4, color='green', label='SCOPE', yerr=0.05, marker='o')
    # plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    # plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    # plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/tasksizevslatency.png")
    plt.show()


def taskSizeVsEnergy():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('Data/tasksizevsenergy.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Task size')
    plt.ylabel('Energy Consumption')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/tasksizevsenergy.png")
    plt.show()


def taskSizeVsUtilityPerUnitCost():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('Data/tasksizevsutilitypercost.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Task size')
    plt.ylabel('Utility per unit Cost')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/tasksizevsutilitypercost.png")
    plt.show()


def taskSizeVsTaskDrop():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('Data/tasksizevstaskdrop.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    plt.xlabel('Task size')
    plt.ylabel('Task Drop Rate')

    plt.plot(x1, y4, marker='o', c='g', label='SCOPE')
    plt.plot(x1, y1, marker='v', c='b', label='MTMS')
    plt.plot(x1, y2, marker='^', c='r', label='Random Assignment')
    plt.plot(x1, y3, marker='P', c='k', label='Greedy Assignment')

    plt.legend()
    plt.savefig("Images/tasksizevstaskdrop.png")
    plt.show()


def taskSizeVsTaskDropBar():
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for line in open('tasksizevstaskdrop.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))

    x = np.arange(len(x1))  # the label locations
    width = 0.24  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, y4, width/2, color='g', label='SCO')
    rects2 = ax.bar(x - width / 2, y1, width/2, color='navy', label='MTMS')
    rects3 = ax.bar(x, y2, width/2, color='r', label='Random Assignment')
    rects4 = ax.bar(x + width/2, y3, width/2, color='k', label='Greedy Assignment')

    ax.set_ylabel('Task Drop Rate')
    plt.xlabel("Task Size")
    ax.set_title('Task Size vs Task Drop Rate')
    ax.set_xticks(x)
    ax.set_xticklabels(x1)
    ax.legend()

    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig("tasksizevstaskdropbar.png")
    plt.show()


# subtaskVsLatency()
# subtaskVsEnergy()
# subtaskVsUtilCost()
# subtaskVsTaskDrop()

# serverVsLatency()
# serverVsEnergy()
# serverVsUtilityPerUnitCost()
# serverVsTaskDrop()
# serverVsTaskDropBar()

taskSizeVsLatency()
# taskSizeVsEnergy()
# taskSizeVsUtilityPerUnitCost()
# taskSizeVsTaskDrop()
# taskSizeVsTaskDropBar()
