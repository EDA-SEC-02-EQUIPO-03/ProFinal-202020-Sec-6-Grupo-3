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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------
def NewAnalizer():

    try:
        taxis = {
                    '': None,
                    '': None,
                    '': None,
                    '': None
                    }

    
        return taxis
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')
    
# Funciones para agregar informacion al grafo
def loadTrips(taxis):

    for taxi_file in os.listdir(cf.data_dir):
        if taxis_file.endswith('.csv'):
            print('Cargando archivo: ' + taxis_file)
            loadFile(taxis,taxis_file)
    return taxis 


def loadFile(taxis, taxis_file):
    
    tripfile = cf.data_dir + taxis_file
    input_file = csv.DictReader(open(tripfile, encoding='utf-8'), delimiter=',')
    for trip in input_file:
        model.addTrip(taxis, trip)
    return taxis



# ==============================
# Funciones de consulta
# ==============================

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def compare(x1, x2):
    """
    Compara dos elementos
    """
    if (x1 == x2):
        return 0
    elif (x1 > x2):
        return 1
    else:
        return -1