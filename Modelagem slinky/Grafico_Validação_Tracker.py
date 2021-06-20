import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

serie_temporal = []
posicao_y_topo = []
velocidade_y_topo = []
posicao_y_base = []
velocidade_y_base = []
text_file = open("Tracker_topo.txt", 'r')
lines = text_file.readlines()
text_file.close()
for line in lines:
    serie_temporal.append(float(line.split()[0])-1.387312398)
    posicao_y_topo.append(float(line.split()[1])*(-1))
    velocidade_y_topo.append(float(line.split()[2])*(-1))
text_file = open("Tracker_base.txt", 'r')
lines = text_file.readlines()
text_file.close()
for line in lines:
    posicao_y_base.append(float(line.split()[1])*(-1))
    velocidade_y_base.append(float(line.split()[2])*(-1))
plt.plot(serie_temporal, posicao_y_topo, 'ro', label='Topo')
plt.plot(serie_temporal, posicao_y_base, 'go', label='base')
plt.xlabel("Tempo em segundos")
plt.ylabel("Altura em centímetros")
plt.grid(True)
plt.legend()
plt.show()
