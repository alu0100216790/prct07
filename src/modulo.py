#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
import sys       # hay que incluirla al principio del programa
import math
PI35DT= 3.1415926535897931159979634685441852

#***************FUNCION PI*******************
def calcular_pi (n):
  valor_pi= 3.1415926535897931159979634685441852
  sumatorio=0.0
  ini=0
  intervalo= 1.0 / float(n)
  for i in range (n):
    x_i= ((i+1) - 1.0 / 2.0) /n     # así lo hacemos ahora
    #x_i=calcular_xi (n,i+1)     # así, si utilizáramos la función definida aal principio.
    fx_i= 4.0/(1.0+ x_i * x_i)
    # print " " ,i+1,". Subintervalo:[", ini,"," ,ini+intervalo,"] x_",i+1,":" ,x_i,"f(x_",i+1,"):",fx_i
    ini += intervalo                   #Incrementamos ini con el valor de intervalo.
    sumatorio += fx_i                  #Incrementamos el sumatorio con cada pasada por fx_i
  pi=sumatorio / n                     #calculamos la aproximación de π (notar que tiene que estar fuera del for¡¡)
  return (pi)
#****************************************
if (__name__=="__main__"):             # Muy importante para que puede leer el modulo, para que lo pueda transformar en .pyc
  argumentos =sys.argv[1:]

  print argumentos            #muestra la lista de parámetros
  if (len(argumentos)==2):
    n=int(argumentos[0])
    aproximaciones = int(argumentos[1])
  else:     #2. O que el usuario, introduzca el intervalo por teclado.
    print "Introduzca el intervalo (n>0)"
    n=int(raw_input())
    print "Introduaca el número de aproximaciones:"
    aproximaciones = int( raw_input())
  if (n>=0):
    PI35DT= 3.1415926535897931159979634685441852
    intervalo = n
    lista = [] 
    diferencia = [] # SE INICIALIZA LA LISTA
    for i in range(aproximaciones):   # me va calculando cada una de las iteraciones
      valor = calcular_pi(intervalo)
      lista.append (valor)        # añade el valor concreto a lista. Se podría poner directamente lista.append (calcular_pi (intervalo))  
      intervalo +=n
    print lista
    for i in range(aproximaciones):    #CREAMOS OTRO BUCLE PARA LA SEGUNDA LISTA DIFERENCIA
      dif = abs (PI35DT - lista [i])
      diferencia.append (dif)
    print "************************************************************"  
    print "************************************************************"
    print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"   # me saca las palabras¡¡¡
    print "************************************************************"
    for i in range (aproximaciones) :
      print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,PI35DT,lista [i],diferencia [i]) 
  else:
    print "El valor del numero de intervalos debe ser positivo."
    