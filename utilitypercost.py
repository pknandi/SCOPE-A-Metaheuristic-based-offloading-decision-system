import random
import math
import numpy as np

f1 = open("Data/subtasklatency.txt", 'r')
f2 = open("Data/subtaskenergy.txt", 'r')
lines = f1.readlines()
mcts1, randm1, greedy1, sco1 = [], [], [], []
for line in lines:
    cur = line.split()
    mcts1.append(cur[1])
    randm1.append(cur[2])
    greedy1.append(cur[3])
    sco1.append(cur[4])

lines = f2.readlines()
mcts2, randm2, greedy2, sco2 = [], [], [], []
for line in lines:
    cur = line.split()
    mcts2.append(cur[1])
    randm2.append(cur[2])
    greedy2.append(cur[3])
    sco2.append(cur[4])

mcts3, randm3, greedy3, sco3 = [], [], [], []
divide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cost1 = [46.3, 50.123, 49.37, 54.61, 56.48, 50.1, 49.17, 54.50, 56.95, 55.54]
cost2 = [43.3, 51.123, 52.37, 54.61, 56.48, 53.1, 51.17, 55.15, 57.95, 55.70]
cost3 = [53.3, 51.123, 54.37, 56.61, 57.48, 59.1, 58.17, 58.15, 59.95, 55.80]
cost4 = [43.3, 47.123, 50.37, 52.61, 52.48, 50.1, 50.17, 53.15, 54.95, 56.00]

alpha = .5
for i in range(0, len(sco1)):
    mcts3.append((1/((float(mcts1[i])/1) * alpha + float(mcts2[i]) * 5 * (1 - alpha)))/52)
    randm3.append((1/((float(randm1[i])/1) * alpha + float(randm2[i]) * 5 * (1 - alpha)))/54)
    greedy3.append((1/((float(greedy1[i])/1) * alpha + float(greedy2[i]) * 5 * (1 - alpha)))/56)
    sco3.append((1/((float(sco1[i])/1) * alpha + float(sco2[i]) * 5 * (1 - alpha)))/52)

tasksize = 200
subtask = 1
for i in range(0, len(mcts3)):
    print(str(subtask), "  ", round(mcts3[i], 3), "  ", round(randm3[i], 3), "  ", round(greedy3[i], 3), "  ", round(sco3[i], 3))
    subtask += 1
