"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de taxis")
    print("3- Parte A ")
    print("4- Parte C ")
    print("0- Salir")
    print("*******************************************")
# ___________________________________________________
#  Opciones
# ___________________________________________________

def optionTwo():
    print("\nCargando información de taxis ....")
    size=str(input("Tamaño del archivo (small, medium, large) : "))
    taxisfile=str('taxi-trips-wrvz-psew-subset-'+ size +'.csv')
    controller.loadData(analyzer,taxisfile)
    print("\nCargado con éxito !! ")

def optionThree():
    print("\nParte A")
    N=int(input("¿De qué cantidad desea el Top de compañías que más servicios prestaron? : "))
    M=int(input("¿De qué cantidad desea el Top de compañías que más taxis afiliados tiene ? : "))
    num_taxis_comp=controller.allTaxisCompanies(analyzer)
    print("El número total de taxis en los servicios reportados es:",num_taxis_comp[0])
    print("El número total de compañías que tienen al menos un taxi inscrito es: ",num_taxis_comp[1])
    print(" ")
    topN=controller.topN(analyzer,N)
    print("TOP #. Company: #Services")
    n=1
    for x,y in topN.items():
            for i in y:
                print(str(n)+".  "+str(i)+": "+str(x))
                n+=1
    topM=controller.topM(analyzer,M)
    print(" ")
    print("TOP #. Company: #Taxis")
    f=1
    for x,y in topM.items():
            for i in y:
                print(str(f)+".  "+str(i)+": "+str(x))
                f+=1
    
def optionFour():
    print("\nParte C")
    print("función para ver el mejor horario y ruta para un viaje entre dos comunity area")
    station1=input("Escriba el numero de la community area de salida: ")
    station2=input("Escriba el numero de la community area de destimo: ")
    timestart=input("Escriba la hora minima que estima para su salida: ")
    timeend=input("Escriba la hora maxima que estima para su salida: ")
    result=controller.theBestRoute(analyzer["grafos"],station1,station2,timestart,timeend)
    print("la mejor hora para salir es :", result[0])
    print("el camino que se debe seguir es")
    if result[1] != None:
        while not(stack.isEmpty(result[1])):
            station=stack.pop(result[1])
            vertA=station['vertexA'].split(";;",1)[0]
            vertB=station['vertexB'].split(";;",1)[0]
            print(vertA,'->',vertB)
        print("El tiempo estimado de viaje es: ",result[2])
    else:
        print("No existe ruta entre ",station1," y ",station2)

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        analyzer = controller.init()

    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(optionTwo, number=1)

        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 3:
        executiontime = timeit.timeit(optionThree, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 4:
        executiontime = timeit.timeit(optionFour, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    else:
        sys.exit(0)
sys.exit(0)
