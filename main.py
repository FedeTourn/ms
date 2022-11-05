from matplotlib import pyplot as plt
from datos import Datos as d
import numpy as np
import sympy as s
import scipy.interpolate as interpol

def main():
    
    splines()
    

    # x, y = d.modeloDerivadas()
    # seleccionIntervalos(x,y)

def splines():
    x,y = d.modelo()
    z=interpol.splrep(x,y)

    arreglo=np.arange(x[0],x[-1],33.3e-6)#No se si esta bien eso
    zn=interpol.splev(arreglo,z)
    plt.plot(x,y,marker='o',markerfacecolor='blue',linestyle='None')
    plt.plot(arreglo,zn,color='red')
    plt.show()

def seleccionIntervalos(px,py):
    x = s.Symbol('x')
    #Suponemos que vamos a tener 10 intervalos

    iX1,iX2,iX3,iX4,iX5,iX6,iX7,iX8,iX9,iX10,iX11=seleccion(px)
    iY1,iY2,iY3,iY4,iY5,iY6,iY7,iY8,iY9,iY10,iY11=seleccion(py)
    
    # expresion1=diferenciasDivididas(iX1,iY1)
    # expresion2=diferenciasDivididas(iX2,iY2)
    expresiones=[]
    args=[]
    for i in range(11):
        i=i+1
        match i:
            case 1:
                expresion=diferenciasDivididas(iX1,iY1,0)
                args.append([x,iX1[0],iX1[-1]])
            case 2:
                expresion=diferenciasDivididas(iX2,iY2,1)
                args.append([x,iX2[0],iX2[-1]])
            case 3:
                expresion=diferenciasDivididas(iX3,iY3,2)
                args.append([x,iX3[0],iX3[-1]])
            case 4:
                expresion=diferenciasDivididas(iX4,iY4,3)
                args.append([x,iX4[0],iX4[-1]])
            case 5:
                expresion=diferenciasDivididas(iX5,iY5,4)
                args.append([x,iX5[0],iX5[-1]])
            case 6:
                expresion=diferenciasDivididas(iX6,iY6,5)
                args.append([x,iX6[0],iX6[-1]])
            case 7:
                expresion=diferenciasDivididas(iX7,iY7,6)
                args.append([x,iX7[0],iX7[-1]])
            case 8:
                expresion=diferenciasDivididas(iX8,iY8,7)
                args.append([x,iX8[0],iX8[-1]])
            case 9:
                expresion=diferenciasDivididas(iX9,iY9,8)
                args.append([x,iX9[0],iX9[-1]])
            case 10:
                expresion=diferenciasDivididas(iX10,iY10,9)
                args.append([x,iX10[0],iX10[-1]])
            case 11:
                expresion=diferenciasDivididas(iX11,iY11,10)
                args.append([x,iX11[0],iX11[-1]])

        expresiones.append(expresion)
    
    s.plot((expresiones[0], (args[0])),
    (expresiones[1], (args[1])),
    (expresiones[2], (args[2])),
    (expresiones[3], (args[3])),
    (expresiones[4], (args[4])),
    (expresiones[5], (args[5])),
    (expresiones[6], (args[6])),
    (expresiones[7], (args[7])),
    (expresiones[8], (args[8])),
    (expresiones[9], (args[9])),
    (expresiones[10], (args[10])),
    )

def mostrarFuncion(px, py):
    plt.grid(True)
    plt.plot(px,py,marker='o')
    plt.show()

def diferenciasDivididas(x,y,n):
    dD = []
    coef = []
    coef.append(y[0])
    n=n-1
    derivadas=[0, 32.01666667, 128.2565608, 197.1565608, 0, -143.5000000, 0, 2.988571429, 6.467936508,-6.012063492]#Completar con las derivadas
    
    #Si los valores de x son iguales es pq agregamos la derivada
    #Si los valores de x son iguales produce excepcion
    for j in range(len(x)-1):
        if(j == 0):
            for i in range(len(x)-1):
                try:
                    valor = (y[i+1]-y[i])/(x[i+1]-x[i])
                except:
                    #reemplazamos por la derivada
                    valor = derivadas[n]
                dD.append(valor)
        else:
            dD1=[]
            for i in range(len(dD)-1):
                try:
                    valor = (dD[i+1]-dD[i])/(x[i+j+1]-x[i])
                except:
                    #reemplazamos por la derivada
                    valor = derivadas[n]
                dD1.append(valor)
            dD = dD1
        coef.append(dD[0])
    expresion=polinomio(coef,x)
    return expresion

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
                expresion=expresion#Deberia agregar 0 pero no aporta nada
        
    #print(expresion)
    return expresion

def seleccion(x):
    iX1=[]
    iX2=[]
    iX3=[]
    iX4=[]
    iX5=[]
    iX6=[]
    iX7=[]
    iX8=[]
    iX9=[]
    iX10=[]
    iX11=[]
    
    #SELECCIONAMOS PUNTOS DE CADA INTERVALO#
    # puntos x = 0; 0,4 -->Linear
    iX1.append(x[0])
    iX1.append(x[1])
    
    # puntos x = 0,4; 0,8 ; 1 -->Linear
    iX2.append(x[1])#Agrego para restringir derivada en 0,4
    iX2.append(x[2])
    iX2.append(x[3])
    iX2.append(x[4])
    
    # puntos x = 1; 1,15; 1,30; 1,50   
    iX3.append(x[4])#Agrego para restringir derivada en 1
    iX3.append(x[5])
    iX3.append(x[6])
    iX3.append(x[7])
    iX3.append(x[8])
    
    # puntos x = 1,50; 1,70; 1,90
    iX4.append(x[8])#Agrego para restringir derivada en 1,5
    iX4.append(x[9])
    iX4.append(x[10])
    iX4.append(x[11])
    
    # puntos x = 1,90; 2
    iX5.append(x[11])#Agrego para restringir la derivada en 1,9
    iX5.append(x[12])
    iX5.append(x[13])
    
    # puntos x = 2; 2,10; 2,30 #No restrinjo al inicio ni al final porque es muy linda
    iX6.append(x[13])
    iX6.append(x[14])
    iX6.append(x[15])
    
    # puntos x = 2,3; 2,4; 2,5; 2,6
    iX7.append(x[15])
    iX7.append(x[16])
    iX7.append(x[17])
    iX7.append(x[18])
    
    # puntos x = 2,6; 2,7; 3
    iX8.append(x[18])
    iX8.append(x[19])
    iX8.append(x[20])
    iX8.append(x[21])#Agrego para restringir la derivada en 3

    # puntos x = 3; 3,3; 3,6; 4
    iX9.append(x[21])
    iX9.append(x[22])
    iX9.append(x[23])
    iX9.append(x[24])
    
    # puntos x = 4; 4,5; 5
    iX10.append(x[24])#Agrego para restringir la derivada en 4
    iX10.append(x[25])
    iX10.append(x[26])
    iX10.append(x[27])

    # puntos x = 5; 5,5; 6
    iX11.append(x[27])#Agrego para restringir la derivada en 5
    iX11.append(x[28])
    iX11.append(x[29])
    iX11.append(x[30])

    return iX1,iX2,iX3,iX4,iX5,iX6,iX7,iX8,iX9,iX10,iX11

main()