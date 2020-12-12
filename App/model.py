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
from DISClib.ADT import minpq 
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.DataStructures import edge as ed
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
                   
                    'grafos': None
                    }
        taxis['grafos']=gr.newGraph('ADJ_LIST',True,1000,)
        for i in range(0,69)
            x=gr.newGraph('ADJ_LIST',True,1000,)
            taxis['grafos']
        
        return taxis
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')
    
# Funciones para agregar informacion al grafo
def getDateTimeTaxiTrip(taxitrip):
    """
    Recibe la informacion de un servicio de taxi leido del archivo de datos (parametro).
    Retorna de forma separada la fecha (date) y el tiempo (time) del dato 'trip_start_timestamp'
    Los datos date se pueden comparar con <, >, <=, >=, ==, !=
    Los datos time se pueden comparar con <, >, <=, >=, ==, !=
    """
    tripstartdate = taxitrip['trip_start_timestamp']
    taxitripdatetime = datetime.datetime.strptime(tripstartdate, '%Y-%m-%dT%H:%M:%S.%f')
    return taxitripdatetime.date(), taxitripdatetime.time()

def getentry(entry):
    try:
        Start=entry['pickup_community_area']
        Finish=entry['dropoff_community_area']
        timehour= int(hour[0,1])*60
        timemin= (int(hour[2,3])//15)*15
        timestamp=timehour+timemin
        Start_entry=Start+str(timestamp)
        Finish_entry=Start+str(timestamp)
        return Start_entry,Finish_entry
    except Exception as exp
    

def addgraph(Analyzer,entry):
    hour=getDateTimeTaxiTrip(entry)[1]
    entries=getentry(entry)
    if entry['trip_seconds']!=None:
        duration=round(int(entry['trip_seconds'])/60,2)
    if entries[0]!=entries[1]:

        addStation(Analyzer,entries[0])
        addStation(Analyzer,entries[0])
        addConnection (Analyzer, entries[0], entries[1], duration)

def addStation(Analyzer, entry):
    """
    Adiciona una estación como un vertice del grafo
    """
    try:
        if not gr.containsVertex(Analyzer['grafos'], entry):
            gr.insertVertex(Analyzer['grafos'], entry)
        return Analyzer
    except Exception as exp:
        error.reraise(exp, 'model:addStation')

def addConnection(Analyzer, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(Analyzer['grafos'], origin, destination)
    if edge is None:
        gr.addEdge(Analyzer['grafos'], origin, destination, duration)
    else:
        ed.averageWeight(edge,duration)
    return Analyzer


# ==============================
# Funciones de consulta
# ==============================


def theBestRoute(graph,station1,station2,timemin,timemax):
    best=None
    bestpath=None
    besttime=100000
    timemax=timechange(timemax)
    timemin=timechange(timemin)
    i=timemin
    while i=<timemax
        
        stationstart=station1+str(i)
        stationend=station2+str(i)
        best=djk.Dijkstra(graph,station1)
        wa=djk.pathTo(best,station2)
        y=djk.distTo(best,station2)
        if wa!=None:
            if best<=y:
                besttime=y
                best =time
                bestpath= wa
        i+=15
    way=[best,bestpath,besttime]
    return way 


# ==============================
# Funciones Helper
# ==============================
def timechange(hour):
    timehour= int(hour[0,1])*60
    timemin= (int(hour[2,3])//15)*15
    timestamp=timehour+timemin
    return timestamp
def timechangeback(timestamp):
    timehour=timestamp//60
    timemin=timemin%60
    hour=str(timehour)+":"+str(timemin)
# ==============================
# Funciones de Comparacion
# ==============================
def comparemaxpq(x1, x2):
    """
    Compara dos elementos
    """
    if (x1 == x2):
        return 0
    elif (x1 > x2):
        return -1
    else:
        return 1