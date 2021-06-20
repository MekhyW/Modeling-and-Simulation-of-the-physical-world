def funcao(t):
    return t**2

import matplotlib.pyplot as plt
import numpy

serie_temporal = numpy.arange(0, 10, 0.01)
serie_resultado = []
i = 0
for intervalo in serie_temporal:
    serie_resultado.append(funcao(serie_temporal[i]))
    i += 1
plt.plot(serie_temporal, serie_resultado)
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)
plt.show()