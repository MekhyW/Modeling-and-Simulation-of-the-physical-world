import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

#reta que correlaciona pixeis com altura real em centimetros:
#y = 0.17693 x - 7.60798
serie_temporal = np.arange(0, 0.4, 1/60)
posicao_y_topo = []
posicao_y_base = []
text_file = open("position_top_base", 'r')
lines = text_file.readlines()
for line in lines:
    posicao_y_topo.append((int(line.split()[0])*0.17693) - 7.60798)
    posicao_y_base.append((int(line.split()[1])*0.17693) - 7.60798)
plt.plot(serie_temporal, posicao_y_topo, label='Topo')
plt.plot(serie_temporal, posicao_y_base, label='Base')
plt.xlabel("Tempo em segundos")
plt.ylabel("Altura em centímetros")
plt.grid(True)
plt.legend()
plt.show()