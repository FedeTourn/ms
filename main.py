from matplotlib import pyplot as plt

from datos import Datos as d

x, y = d.medido()

plt.plot(x,y)
plt.show()

x, y = d.modelo()

plt.plot(x,y)
plt.show()