from matplotlib import pyplot as plt
from datos import Datos as d

# x, y = d.medido()

# plt.plot(x,y)
# plt.show()

x, y = d.modelo()

# plt.plot(x,y)
# plt.show()

def diferenciasDivididas(x,y):
    dD = []
    tIndep = []
    tIndep.append(y[0])
    
    for j in range(len(x)-1):
        if(j == 0):
            for i in range(len(x)-1):
                valor = (y[i+1]-y[i])/(x[i+1]-x[i])
                dD.append(valor)    
        else:
            dD1=[]
            for i in range(len(dD)-1):
                valor = (dD[i+1]-dD[i])/(x[i+j+1]-x[i])
                
                dD1.append(valor)
            dD = dD1
        tIndep.append(dD[0])
    #print(tIndep)
    return tIndep

terminosIndep = diferenciasDivididas(x,y)