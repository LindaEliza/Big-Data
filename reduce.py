# -*- coding: utf-8 -*-
"""
@author: Linda
"""
#python map.py | python reduce.py > resultado.txt

import sys #Importación del paquete sys que se utilizará para tomar los datos que resulta de un procedimiento anterior.

def Relacion(personas,k1,k2,AmigoA): #se define la funcion que indica si tiene amigos en común.
    if AmigoA==1: #Si es la relación de la persona con su amigo.
        AmigoA = True #Tomará un valor verdadero.
    else: #De lo contrario.
        AmigoA = False #Tomará un valor falso.

    if k1 not in personas: #Si el primer elemento de la pareja enviado no está en el diccioanrio de personas.
        personas[k1] = {} #Se creará un subdiccionario dentro de la diccionario de personas en la posición del elemento de la pareja.
        personas[k1][k2] = [1,False] #Se asigna dentro del subdiccionario en la posición del segundo elemento de la pareja el valor de 1, False.
    else: #De lo contrario.
        if k2 in personas[k1]: #Si el segundo elemento de la pareja ya se encuentra dentro del subdiccionario del primer elemento de la pareja.
            personas[k1][k2][0] += 1 #Se le sumará uno al número que se encuentre en la primera posición del subdiccionario, en la posición del segundo elemento del diccionario.
        else: #Si no esta
            personas[k1][k2] = [1,False] #Se asigna dentro del subdiccionario en la posición del segundo elemento de la pareja el valor de 1, False.
    if AmigoA==True: #Si la relación es de la persona con su amigo
        personas[k1][k2][0] -= 1 #Se quitara uno al valor del número que se encuentra en la primera posición del subdiccionario, en la posición del segundo elemento del diccionario.
        personas[k1][k2][1] = True #Se le cambiará el valor de False a True en la posición del segundo elemento de la pareja, debido a que ya son amigos y no los vamos a recomendar entre ellos.


personas = {} #Declaración de una diccionario vacio llamada personas

for registro in sys.stdin: #Este ciclo sirve para recorrer cada registro de los datos que se obtienen del procedimiento anterior.
    registro = registro.strip().split("\t") #Elimina los espacios en blanco al inicio y final de la line y separa cada string en base a un espacio en blanco.
    llave = tuple(map(int,registro[0].strip().split(","))) #Se obtiene la pareja de amigos en donde cada elemento se convierte en un entero, y se toma como la llave de la linea (registro).  
    AmigoA = int(registro[1]) #Se obtiene el 0 o 1 según la linea (registro)
    k1,k2 = llave #A k1 se le asigna el primer elemento de la pareja y a k2 se le asigna el segundo elemento de la pareja.
    Relacion(personas,k1,k2,AmigoA) #Se llama a la funcion Relacion en donde se envía el diccioanrio personas, k1, k2 y la llave.
    Relacion(personas,k2,k1,AmigoA) #Se llama a la funcion Relacion en donde se envía el diccioanrio personas, k2, k1 y la llave.

for k1 in personas.keys(): #Con este ciclo se recorre el listado de las llaves del diccionario personas
    recomendacion = [] #Se crea la lista recomendaciones
    for k2 in personas[k1].keys(): #Para cada llave que se encuentra dentro del subdiccionario según la llame del diccionario personas
        n,flag = personas[k1][k2] #Se toma el valor que indica la cantidad de veces que sus amigos tienen a ese amigo, y a flag se le asigna el True o False que indica si ya son o no son amigos.
        if flag==False: #Si flag es igual a False significa que no son amigos.
            if n>10: #Este if sirve para determinar la cantidad mínima de amigos que deben tener en común          
                recomendacion.append((k2,n)) #Se agrega este dato junto con su valor n a la lista de recomendacion
    recomendacion = sorted(recomendacion,key=lambda x: x[1],reverse=True) #Esta linea permite ordenar la lista de recomendación por medio de la cantidad de amigos en comun que tiene, el cual esta en reversa para ir de mayor a menor.
    if len(recomendacion)>0: #Si el largo de recomendacion es mayor a cero.
        recomendacion = list(map(str,zip(*recomendacion)[0])) #lista recomentaciones que está compuesta por elementos de tipo string los cuales surgen de una combinación que se hacen entre cada persona que puede ser amigo con otro.
        print k1,"\t",','.join(recomendacion[:10]) #Muuestran las recomendaciones, cuya cantidad esta definida por el número que se encuentra dentro de los corchetes cuadrados.