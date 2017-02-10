# -*- coding: utf-8 -*-
"""
@author: linda
"""

from itertools import combinations #Paquete que permite la iteración de combinaciones o permutaciones entre los datos que se indican.

archivo = open("UFMmapreduce.txt", "r") #Se lee el archivo que contiene los datos que se utilizarán para el mapeo.

for linea in archivo: #Todas las instrucciones que se encuentran dentro del for se ejecutarán para cada linea del archivo.
    linea = linea.strip().split("\t") #Elimina los espacios en blanco al inicio y final de la linea y separa cada string en base a un espacio en blanco.
    llave = int(linea[0]) #Se obtiene la llave de la linea (registro) que es el primer valor de la linea y se convierte en un entero.
    if len(linea)>1: #Si la linea (registro) tiene dos o mas valores se ejecutrá lo que sigue, lo cual siguifica que debe tener por lo menos un amigo.
        amigos = linea[1] #Se obtienen los amigos que tiene la persona.
        if amigos!='': #Si tiene amigos seguirá ejecuntando las siguientes lineas, de lo contrario regresa al for.
            amigos = linea[1].split(",") #Se separan a los amigos en base a la coma que hay entre ellos.
            amigos = sorted(map(int,amigos)) #Se ordenan los amigos para lo cual se utiliza la funcion de map para convertir a cada amigo en un entero.
            for amigo in amigos: #Recorre toda la lista de amigos
                par = tuple(sorted([llave,amigo])) #Se arma la pareja de la persona con el amigo, pero se ordena de menor a mayor para mantener un estandar que permita más adelante hacer calculos.
                par = ','.join(map(str,par)) #Se  mapea cada elemento de la pareja para convertirlo en string y unirolos por medio de una coma.
                print par,"\t",1 #Muestra a la par de la pareja el valor 1
            for par in combinations(amigos,2): #Se realiza la combinación de los amigos de la linea (registro) de 2 en 2, es decir, se hacen parejas entre los amigos de la persona
                par = ','.join(map(str,par)) #Mapea cada elemento de la pareja para convertirlo en string y unirolos por medio de una coma.
                print par,"\t",0 #Muestra a la par de la pareja el valor 0 lo cual permite diferenciar que son las parejas de los amigos de una persona.