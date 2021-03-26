
import os
import re
import itertools


# Pregunta 1 
# Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma: los 5 mas bajos y los 5 mas altos
aleatorios = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mas_bajos(aleatorio):
    aleatorio.sort()
    suma = 0
    for x in aleatorio[:5]:
            suma+=x
    print('Pregunta 1 - mas bajos: ')
    print(suma)
    return suma

def mas_altos(aleatorio):
    aleatorio.sort()
    suma = 0
    for x in aleatorio[5:]:
            suma+=x
    print('Pregunta 1 - mas altos: ')
    print(suma)
    return suma

        
mas_bajos(aleatorios)
mas_altos(aleatorios)

# Pregunta 2
# Escribir un codigo en python que sume y multiplique respectivamente todos los numeros de una lista, ejemplo: Numeros=1 2 3 4, suma 10, multiplicacion 24.

listanum = [1, 2, 3, 4]

def suma_lista(lista):
    suma = 0
    for x in lista:
        suma += x
    print('Pregunta 2 - suma: ')
    print(suma)
    return suma

def multiplicacion_lista(lista):
    multiplicacion = 1
    for x in lista:
        multiplicacion *= x
    print('Pregunta 2 - multiplicación: ')
    print(multiplicacion)
    return multiplicacion

        
suma_lista(listanum)
multiplicacion_lista(listanum)

        

# Pregunta 3
# Que es INDEX (indice) en base de datos, indicar beneficios y desventajas
# Un indice es una estructura dentro de una base de datos la cual no cambia los datos de la tabla pero establece una nueva estructura de datos que hace referencia a la tabla.
    # Beneficios:
    # - Mayor velocidad a la hora de hacer búsquedas ya que se evita un escaneo completo de la tabla
    # - Evita sobrecarga de CPU y disco

    # Desventajas
    # - Si usas demasiados indices en una tabla puede ralentizar el proceso de escritura
    # - Cualquier indice aumenta el tiempo de INSERT / UPDATE
    # - Ocupa mas espacio de almacenamiento.


# Pregunta 4
# Hacer un programa que tenga la funcion de listar las carpetas y archivos y ordenar por tamaño o fecha, y que muestre si hay archivos duplicados en contenido

def obtener_archivos(): 
    contenido = os.listdir('archivos')
    nombres = []
    tamaños = []
    duplicados = []
    for x in contenido:
        nombres.append(x)
        tamaños.append(os.path.getsize('archivos' + '/' + x))
    print("Pregunta 4: ")
    print("Nombres de archivos : ")
    print(nombres)
    print("Tamaños de archivos : ")
    print(tamaños)


    for c in range(len(contenido)):
        for k in range(c + 1, len(contenido)):
            archivoc = open('archivos' + '/' + contenido[c], "r")
            archivok = open('archivos' + '/' + contenido[k], "r")
            if archivoc.read() == archivok.read():
                duplicados.append(contenido[c])
                duplicados.append(contenido[k])


    print("Archivos duplicados: ")
    print(duplicados)

    n = 0
    while(n < len(tamaños)):
        j = n + 1
        while(j < len(tamaños)):
            if(tamaños[n] > tamaños[j]):
                temp = nombres[n]
                nombres[n] = nombres[j]
                nombres[j] = temp
            j = j + 1
        n = n + 1

    print("Nombres de archivos ordenados por tamaño: ")
    print(nombres)

    return nombres

obtener_archivos()



# Pregunta 5 (repetido)


# Pregunta 6
parentesis1 = '(()()())()()(())'
parentesis2 = '(()('


def parentesis_balanceados(parentesis):
    pila = []
    abierto = "("
    cerrado = ")"

    for p in parentesis:
        if p == abierto:
            pila.append(p)
        elif p == cerrado:
            if len(pila) == 0:
                return False
            else:
                top_pila = pila.pop()
                par_balanceado = abierto[cerrado.index(p)]
                if top_pila != par_balanceado:
                    return False
    print('Pregunta 6: ')
    print(not len(pila))
    return not len(pila)

        
parentesis_balanceados(parentesis1)


# Pregunta 7
# Desarrollar una funcion que me devuelva el n-esimo fibonacci
# Recordar que la serie fibonacci inicia en uno, es decir que fibonacci(1) = 1, ademas que
# el fibonacci(3) = fibonacci(2) + fibonacci(1)
# Nota: Implementarlo de modo iterativo.

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def printfibonacci(n):
    print("Pregunta 7: ")
    print(fibonacci(n))

printfibonacci(8)



# Pregunta 8
# Escribir un programa que tenga como input 10 numeros positivos de 3 digitos, y como output liste los que son capicuas,
# ordenandolos de menor a mayor

arr_capicuas = [101, 223, 421, 521, 333, 202, 999, 113, 929, 343]

def capicua_orden(capicuas):
  capicua = []
  for x in capicuas:
    valor = x
    valor = str(valor)
    if valor[0] == valor[2]:
        valor = int(valor)
        capicua.append(valor)
  capicua.sort()
  print("Pregunta 9: ")
  print(capicua)
  return capicua
 
capicua_orden(arr_capicuas)


# Pregunta 9 -- 

# Teoría de SQL
# como hacer un flujo de respaldo, como operar con null
# En base de datos null no es un tipo de dato, simplemente ejemplifica un valor que no ha sido enviado, cualquier operación aritmética que involucre null siempre devolvera null, cuando
# se realiza un conteo en una tabla por un campo, si hay valores nulos estos no seran considerados como parte del conteo. Para valores enteros es siempre recomendable crearlos con la clausula
# NOT NULL para asegurar que siempre se puedan realizar operaciones aritmenticas con sus valores.   



