#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-

import modulo

#Programa principal
#Ojo, para hacer uso de la función sys, debemos incluirla al principio del progrma.

#tupla = (10,20,30,40)
tupla = (100,200,300,400)



lista= []

for i in tupla:
  #time()     #calcula en tiempo entre cada ejecución. Tiempo inicial.
  valor_pi = modulo.calcular_pi (i)
  #time()     #tiempo final
  lista.append (valor_pi)
print lista

pi35 = []
for i in tupla:
  pi35.append (modulo.PI35DT)
dif35 = []
for i in range (len(tupla)):                #cuantos elementos hay?
  dif35.append (abs(pi35[i]-lista[i]))       # ultima columna de la practica 6
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"
print "***********************************************************"
for i in range  (len(tupla)):   
  print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,pi35[i] ,lista[i], dif35 [i])
#dependiendo de la maquina, en nuestra maquina: 1000000000.
#Se puede añadir notación científica sin problemas.
#cuando se convierte a .pyc es que se ha comprovado que existe el módulo y lo transforma en .pyc.

# Esto sería para sbaer mas...
print " Pasando la salida de una matriz ....."
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i" , #         # El #, nos deja el cursor en la misma linea

matriz = []
for i in range (len(tupla)): 
  matriz.append ([i+1,pi35[i],lista[i],dif35[i]])
for i in range (len(tupla)): 
  print
  print matriz[i][0], #
  for j in range (1,4):
    print "\t%1.10f" % matriz[i][j], #