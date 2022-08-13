# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 17:25:20 2022

@author: raulm
"""
digito={0:'cero',1:'uno',2:'dos',3:'tres',4:'cuatro',5:'cinco',6:'seis',7:'siete',8:'ocho',
         9:'nueve',10:'diez',11:'once',12:'doce',13:'trece',14:'catorce',15:'quince'}

decena={20:'veinte',30:'treinta',40:'cuarenta',50:'cincuenta',60:'sesenta',70:'setenta',
        80:'ochenta',90:'noventa'}

centena={100:'ciento',200:'doscientos',300:'trescientos',400:'cuatrocientos',500:'quinientos',
         600:'seiscientos',700:'setecientos',800:'ochocientos',900:'novecientos'}

def num(n):
    """
    Parameters
    ----------
    n : Un numero entero positivo

    Returns
    -------
    d : Un diccionario que se genera con los digitos de n, creando llaves d[x] con valor del digito
    correspondiente a la posicion x. Ejemplo n=123 devuelve d={d0:1,d1:2,d2:3}

    """
    d={}
    x=str(n)
    for i in range(len(x)):
        d['d'+str(i)]=int(x[i])
    return d

def f(n):
    '''
    Parameters
    ----------
    n : Un número entero positivo de 0 a 9999999.

    Returns
    -------
    El número ingresado (n) en su forma textual.

    '''
    dicc=num(n)
    #Mediante globals()[''] se pueden crear variables con las llaves y valores correspondientes 
    #del diccionario  creado en num(n): d0=1,d1=2,d3=3. globals()['d1']=1 crea la variable
    #d1=1, es decir que al str 'd1' se le asignó una variable con ese nombre con valor 1.
    for k,v in dicc.items():
        globals()[k]=v
    if n<100:
        if n<30:
            if n<16:
                return(digito[n])
            elif n<20:
                return('dieci'+digito[d1])
            #d1 sale como no definida porque aun no se ejecuta el código y por tanto
            # tampoco la función num(n) que crea el diccionario de donde salen las variables d[x]
            elif n==20:
                return(decena[n])
            else:
                return('veinti'+digito[d1])
        else:
            if d1==0:
                return(decena[n])
            else:
                return(decena[d0*10]+' y '+digito[d1])
    elif n<1000:
        c=d0*100
        if n==100:
            return('cien')
        elif (d1,d2)==(0,0):
            return(centena[n])
        else:
            return(centena[c]+' '+f(d1*10+d2))
    elif n<10000:
        if n<2000:
            if n==1000:
                return('mil')
            else:
                return('mil '+f(d1*100+d2*10+d3))
        else:
            if (d1,d2,d3)==(0,0,0):
                return(digito[d0]+' mil')
            else:
                return(digito[d0]+' mil '+f(d1*100+d2*10+d3))
    elif n<100000:
        dn=int(str(d0)+str(d1))
        if (d1,d2,d3,d4)==(0,0,0,0):
            return(f(dn))+' mil'
        else:
            if (d2,d3,d4)==(0,0,0):
                return(f(dn)+' mil')
            else:
                return(f(dn)+' mil ' + f(d2*100+d3*10+d4))
    elif n<1000000:
        dn=int(str(d0)+str(d1)+str(d2))
        if (d1,d2,d3,d4,d5)==(0,0,0,0,0):
            return(f(dn)+' mil')
        else:
            if (d2,d3,d4,d5)==(0,0,0,0):
                return(f(dn)+' mil')
            else:
                return(f(dn)+' mil ' + f(d3*100+d4*10+d5))
    elif n<10000000:
        if n==1000000:
            return('un millón')
        elif n<2000000:
            return('un millón'+' ' +f(d1*100000+d2*10000+d3*1000+d4*100+d5*10+d6))
        else:
            if (d1,d2,d3,d4,d5,d6)==(0,0,0,0,0,0):
                return(digito[d0]+' millones')
            else:
                return(digito[d0]+' millones '+f(d1*100000+d2*10000+d3*1000+d4*100+d5*10+d6))
                                 #Alternativa: f(int(str(d1)+str(d2)+...+str(d6)))

n=int(input('Digite un entero entre 0 y 9999999: '))
print(f(n))
