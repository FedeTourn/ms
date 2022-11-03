from matplotlib import pyplot as plt
from datos import Datos as d
import sympy as s

def main():
    x, y = d.modelo()
    # x, y = d.medido()
    
    # x=[1,2,3,4]
    # y=[-2,1,6,13]

    seleccionIntervalos(x,y)
    #mostrarFuncion(x,y)
    # diferenciasDivididas(x,y)

def seleccionIntervalos(px,py):
    x = s.Symbol('x')
    #Suponemos que vamos a tener 10 intervalos

    iX1,iX2,iX3,iX4,iX5,iX6,iX7,iX8,iX9,iX10=seleccion(px)
    iY1,iY2,iY3,iY4,iY5,iY6,iY7,iY8,iY9,iY10=seleccion(py)
    
    # expresion1=diferenciasDivididas(iX1,iY1)
    # expresion2=diferenciasDivididas(iX2,iY2)
    expresiones=[]
    args=[]
    for i in range(10):
        i=i+1
        match i:
            case 1:
                print('entraaca')
                expresion=diferenciasDivididas(iX1,iY1)
                args.append([x,iX1[0],iX1[-1]])
            case 2:
                expresion=diferenciasDivididas(iX2,iY2)
                args.append([x,iX2[0],iX2[-1]])
            case 3:
                expresion=diferenciasDivididas(iX3,iY3)
                args.append([x,iX3[0],iX3[-1]])
            case 4:
                expresion=diferenciasDivididas(iX4,iY4)
                args.append([x,iX4[0],iX4[-1]])
            case 5:
                expresion=diferenciasDivididas(iX5,iY5)
                args.append([x,iX5[0],iX5[-1]])
            case 6:
                expresion=diferenciasDivididas(iX6,iY6)
                args.append([x,iX6[0],iX6[-1]])
            case 7:
                expresion=diferenciasDivididas(iX7,iY7)
                args.append([x,iX7[0],iX7[-1]])
            case 8:
                expresion=diferenciasDivididas(iX8,iY8)
                args.append([x,iX8[0],iX8[-2]])
            case 9:
                expresion=diferenciasDivididas(iX9,iY9)
                args.append([x,iX9[0],iX9[-1]])
            case 10:
                expresion=diferenciasDivididas(iX10,iY10)
                args.append([x,iX10[0],iX10[-1]])

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
    )


def mostrarFuncion(px, py):
    plt.grid(True)
    plt.plot(px,py,marker='o')
    plt.show()

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
                expresion=expresion+'+0'
        
    print(expresion)
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
    
    #SELECCIONAMOS PUNTOS DE CADA INTERVALO#
    iX1.append(x[0])# puntos x = 0; 0,4 -->Linear
    iX1.append(x[1])
    
    iX2.append(x[1])# puntos x = 0,4; 0,8 -->Linear
    iX2.append(x[2])
    
    iX3.append(x[2])# puntos x = 0,8; 1; 1,15; 1,3 -->Cubica
    iX3.append(x[3])
    iX3.append(x[4])
    iX3.append(x[5])
    
    iX4.append(x[5])# puntos x = 1,3; 1,5; 1,7; 1,9; 2 -->Grado 4 (cubica con suerte)
    iX4.append(x[6])
    iX4.append(x[7])
    iX4.append(x[8])
    iX4.append(x[9])
    
    iX5.append(x[9])# puntos x = 2; 2,1; 2,3 -->
    iX5.append(x[10])
    iX5.append(x[11])
    
    iX6.append(x[11])# puntos x = 2,3; 2,4; 2,5; 2,6
    iX6.append(x[12])
    iX6.append(x[13])
    iX6.append(x[14])
    
    iX7.append(x[14])# puntos x = 2,6; 2,7; 3
    iX7.append(x[15])
    iX7.append(x[16])
    
    # puntos x = 3,3; 3,6; 4; 4,5
    iX8.append(x[16])
    iX8.append(x[17])
    iX8.append(x[18])
    iX8.append(x[19])
    iX8.append(x[20])
    
    iX9.append(x[19])# puntos x = 4; 4,5; 5
    iX9.append(x[20])
    iX9.append(x[21])
    
    iX10.append(x[21])# puntos x = 5; 5,5; 6
    iX10.append(x[22])
    iX10.append(x[23])
    
    return iX1,iX2,iX3,iX4,iX5,iX6,iX7,iX8,iX9,iX10

main()