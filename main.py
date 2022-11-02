from matplotlib import pyplot as plt
from datos import Datos as d
import sympy as s

def main():    
    # x, y = d.medido()

    # plt.plot(x,y)
    # plt.show()

    x, y = d.modelo()

    # plt.plot(x,y)
    # plt.show()
    x=[1,2,3,4]
    y=[-2,1,6,13]

    coeficientes = diferenciasDivididas(x,y)
    polinomio(coeficientes,x)

def diferenciasDivididas(x,y):
    dD = []
    coef = []
    coef.append(y[0])
    
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
        coef.append(dD[0])
    #print(tIndep)
    return coef

def polinomio(coef,px):
    
    x = s.Symbol('x')
    expresion = ''
    for i in range(len(coef)):
        if(i==0):
            expresion=expresion+str(coef[i])#Agrega el TI
        else:
            if coef[i]>0:
                expresion=expresion+'+'+str(coef[i])#Agrega el Coeficiente
                for j in range(i):#Agrega los(x-xa)
                    expresion=expresion+'*(x-'+str(px[j])+')'
            elif coef[i]<0:
                expresion=expresion+str(coef[i])#Agrega el Coeficiente
                for j in range(i):#Agrega los(x-xa)
                    expresion=expresion+'*(x-'+str(px[j])+')'
            else:
                expresion=expresion+'+0'
        
    print(expresion)
    
    s.plot(expresion)   


main()