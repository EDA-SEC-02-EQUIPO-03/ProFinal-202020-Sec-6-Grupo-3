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

import config as cf
from App import model
import csv
import os 
from DISClib.Algorithms.Graphs import scc


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    taxis = model.newAnalyzer()
    return taxis
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadData(analyzer, taxisfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    taxisfile = cf.data_dir + taxisfile
    input_file = csv.DictReader(open(taxisfile, encoding="utf-8"),
                                delimiter=",")

    for taxi in input_file:
        model.addService(analyzer, taxi)
        model.addgraph(analyzer,taxi)
 
    return analyzer

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def topN(analyzer,N):
    return model.topN(analyzer['theServices'],N)

def topM(analyzer,M):
    return model.topM(analyzer['theServices'],M)

def allTaxisCompanies(analyzer):
    return model.allTaxisCompanies(analyzer['theServices'])
def theBestRoute(analyzer,station1,station2,time1,time2):
    return model.theBestRoute(analyzer,station1,station2,time1,time2)