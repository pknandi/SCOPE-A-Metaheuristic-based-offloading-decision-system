import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

x1 = []
y1 = []
y2 = []
y3 = []
y4 = []


def prepareDataSet(s):
    for line in open(s, 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))


def clearDataSet():
    x1.clear()
    y1.clear()
    y2.clear()
    y3.clear()
    y4.clear()


def subtaskVsLatency():
    prepareDataSet('Data/subtasklatency.txt')

    plt.xlabel('Number of subtasks', fontsize=11, fontname='monospace')
    plt.ylabel('Service Latency', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.10, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.11, marker='^', capsize=2, linestyle='dotted', linewidth=2.0,
                 markersize=4.2, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.10, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.0, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.09, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.7, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/subtaskvslatency.png")
    plt.show()
    clearDataSet()


def subtaskVsEnergy():
    prepareDataSet('Data/subtaskenergy.txt')

    plt.xlabel('Number of subtasks', fontsize=11, fontname='monospace')
    plt.ylabel('Energy Consumption', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.010, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.010, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.008, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.007, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.7, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/subtaskvsenergy.png")
    plt.show()
    clearDataSet()


def subtaskVsTaskDrop():
    prepareDataSet('Data/subtaskvstaskdrop.txt')

    plt.xlabel('Number of subtasks', fontsize=11, fontname='monospace')
    plt.ylabel('Task Drop Rate', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.22, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.25, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.25, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.15, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.8, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/subtaskvstaskdrop.png")
    plt.show()
    clearDataSet()


def subtaskVsUtilCost():
    prepareDataSet('Data/subtaskutilitypercost.txt')

    # plt.title("Number of subtasks vs Utility per Unit Cost")
    plt.xlabel('Number of subtasks', fontsize=11, fontname='monospace')
    plt.ylabel('Utility per Unit Cost', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.016, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.015, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.014, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.013, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.7, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/subtaskvsutilitypercost.png")
    plt.show()
    clearDataSet()


def serverVsLatency():
    prepareDataSet('Data/serverlatency.txt')

    plt.xlabel('Number of Servers', fontsize=11, fontname='monospace')
    plt.ylabel('Service Latency', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.026, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.025, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.022, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.021, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.7, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/servervslatency.png")
    plt.show()
    clearDataSet()


def serverVsEnergy():
    prepareDataSet('Data/servervsenergy.txt')

    plt.xlabel('Number of Servers', fontsize=11, fontname='monospace')
    plt.ylabel('Energy Consumption', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.0032, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.0031, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.1, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.0030, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=3.8, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.0026, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.5, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/servervsenergy.png")
    plt.show()
    clearDataSet()


def serverVsUtilityPerUnitCost():
    prepareDataSet('Data/serverutilitypercost.txt')

    plt.xlabel('Number of Servers', fontsize=11, fontname='monospace')
    plt.ylabel('Utility per Unit Cost', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.022, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.025, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.1, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.026, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=3.8, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.017, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.5, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/servervsutilcost")
    plt.show()
    clearDataSet()


def serverVsTaskDrop():
    prepareDataSet('Data/servervstaskdrop.txt')

    plt.xlabel('Number of Servers', fontsize=11, fontname='monospace')
    plt.ylabel('Task Drop Rate', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.25, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.3, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.3, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.8, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.17, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.8, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/servervstaskdrop.png")
    plt.show()
    clearDataSet()


def serverVsTaskDropBar():
    prepareDataSet('Data/servervstaskdrop.txt')

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
    clearDataSet()


def taskSizeVsLatency():
    prepareDataSet('Data/tasksizevslatency.txt')

    plt.xlabel('Task Size', fontsize=11, fontname='monospace')
    plt.ylabel('Service Latency', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.18, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.21, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.22, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.16, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.7, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/tasksizevslatency.png")
    plt.show()
    clearDataSet()


def taskSizeVsEnergy():
    prepareDataSet('Data/tasksizevsenergy.txt')

    plt.xlabel('Task size', fontsize=11, fontname='monospace')
    plt.ylabel('Energy Consumption', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.026, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.025, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.022, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.021, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.7, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/tasksizevsenergy.png")
    plt.show()
    clearDataSet()


def taskSizeVsUtilityPerUnitCost():
    prepareDataSet('Data/tasksizevsutilitypercost.txt')

    plt.xlabel('Task size', fontsize=11, fontname='monospace')
    plt.ylabel('Utility per unit Cost', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.026, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.025, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.022, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.021, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.7, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/tasksizevsutilitypercost.png")
    plt.show()
    clearDataSet()


def taskSizeVsTaskDrop():
    prepareDataSet('Data/tasksizevstaskdrop.txt')

    plt.xlabel('Task size', fontsize=11, fontname='monospace')
    plt.ylabel('Task Drop Rate', fontsize=11, fontname='monospace')

    plt.errorbar(x1, y4, color='g', label='SCOPE', yerr=0.25, marker='o', capsize=2, linestyle='solid', linewidth=0.9,
                 markersize=4.5, fillstyle='full')
    plt.errorbar(x1, y1, color='b', label='MTMS', yerr=0.3, marker='^', capsize=2, linestyle='dotted', linewidth=1.5,
                 markersize=4.7, fillstyle='full')
    plt.errorbar(x1, y2, color='r', label='Random Assignment', yerr=0.3, marker='s', capsize=2, linestyle='dashed',
                 linewidth=1.3, markersize=4.8, fillstyle='full')
    plt.errorbar(x1, y3, color='k', label='Greedy Assignment', yerr=0.17, marker='P', capsize=2, linestyle='dashdot',
                 linewidth=1.3, markersize=4.8, fillstyle='full')

    font = font_manager.FontProperties(family='monospace', weight='regular', style='normal', size=10)
    plt.legend(prop=font)

    plt.savefig("Images/tasksizevstaskdrop.png")
    plt.show()
    clearDataSet()


def taskSizeVsTaskDropBar():
    prepareDataSet('Data/tasksizevstaskdrop.txt')

    x = np.arange(len(x1))  # the label locations
    # width = 0.24  # the width of the bars

    fig, ax = plt.subplots()
    # rects1 = ax.bar(x - width, y4, width/2, color='g', label='SCO')
    # rects2 = ax.bar(x - width / 2, y1, width/2, color='navy', label='MTMS')
    # rects3 = ax.bar(x, y2, width/2, color='r', label='Random Assignment')
    # rects4 = ax.bar(x + width/2, y3, width/2, color='k', label='Greedy Assignment')

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
    clearDataSet()


# subtaskVsLatency()
# subtaskVsEnergy()
# subtaskVsUtilCost()
# subtaskVsTaskDrop()

# serverVsLatency()
# serverVsEnergy()
# serverVsUtilityPerUnitCost()
# serverVsTaskDrop()
# serverVsTaskDropBar()

# taskSizeVsLatency()
# taskSizeVsEnergy()
# taskSizeVsUtilityPerUnitCost()
# taskSizeVsTaskDrop()
# taskSizeVsTaskDropBar()
