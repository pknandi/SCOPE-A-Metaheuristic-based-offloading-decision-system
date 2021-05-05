import random
import math
import numpy as np

f1 = open("serverlatency.txt", 'r')
f2 = open("servervsenergy.txt", 'r')
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
divide = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
alpha = .5
for i in range(0, len(sco1)):
    mcts3.append(((float(mcts1[i])/1) * alpha + float(mcts2[i]) * 5 * (1 - alpha)))
    randm3.append(((float(randm1[i])/1) * alpha + float(randm2[i]) * 5 * (1 - alpha)))
    greedy3.append(((float(greedy1[i])/1) * alpha + float(greedy2[i]) * 5 * (1 - alpha)))
    sco3.append(((float(sco1[i])/1) * alpha + float(sco2[i]) * 5 * (1 - alpha)))

tasksize = 200
subtask = 1
for i in range(0, len(mcts3)):
    print(str(subtask), "  ", round(mcts3[i], 3), "  ", round(randm3[i], 3), "  ", round(greedy3[i], 3), "  ", round(sco3[i], 3))
    subtask += 1
