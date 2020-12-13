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
from DISClib.ADT import minpq as mpq
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.ADT import minpq 
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.DataStructures import edge as ed
from DISClib.Utils import error as error
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------
def newAnalyzer():

    try:
        taxis = {
                'theServices': None,
                    'grafos': None
                    
                    }
        taxis['theServices']=m.newMap(numelements=1000,
                                     maptype='PROBING',
                                     comparefunction=compareCompanies)
        taxis['grafos']=gr.newGraph(datastructure='ADJ_LIST',
                        directed=True,
                        size=1000,
                        comparefunction=compareCompanies)
        
        
        return taxis
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')
    
# Funciones para agregar informacion al grafo
def addService(analyzer,taxi):
    try:
        company=str(taxi['company'])
        if company=="":
            company="Independent Owner"
        taxiID= taxi['taxi_id']
        addCompany(analyzer['theServices'],company,taxiID)
    except Exception as exp:
        error.reraise(exp, 'model:addService')

def addCompany(theServices,company,taxiID):
    trip=0
    entry=m.get(theServices,company)
    if entry==None:
       taxislst=lt.newList('ARRAY_LIST',compare)
       lt.addLast(taxislst,taxiID)
       trip=1   
    else:
        oldtrips=entry['value'][1]
        taxislst=entry['value'][0]
        trip=oldtrips+1
        if lt.isPresent(taxislst,taxiID)==0:
            lt.addLast(taxislst,taxiID)
    value=(taxislst,trip)
    m.put(theServices,company,value)
    return theServices

def getentry(entry,hour):
    try:
        
        Start=entry['pickup_community_area'][:-2]
        Finish=entry['dropoff_community_area'][:-2]
        if Start!="" and Finish !="":
            
            timehour= int(hour[0:2])*60
            timemin= (int(hour[3:5])//15)*15
            timestamp=timehour+timemin
            
            Start_entry=Start+";;"+str(timestamp)
            Finish_entry=Finish+";;"+str(timestamp)
            return Start_entry,Finish_entry
    except Exception as exp:
        error.reraise(exp, 'model:getentry')

def addgraph(Analyzer,entry):
    hour=entry['trip_start_timestamp'][11:]
   

    entries=getentry(entry,hour)
    if entry['trip_seconds']!="":
        duration=float(entry['trip_seconds'])
        if entries!=None:
            if entries[0]!=entries[1] :
                
                addStation(Analyzer,entries[0])
                addStation(Analyzer,entries[1])
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

def topN(theServices,N):
    valores=[]
    res={}
    i=0
    keys= m.keySet(theServices)
    values=m.valueSet(theServices)
    itv=it.newIterator(values)
    itk=it.newIterator(keys)
    orden=mpq.newMinPQ(comparemaxpq)
    while it.hasNext(itv):
        value=it.next(itv)
        key= it.next(itk)
        if key!= "Independent Owner":
            mpq.insert(orden,value[1])
    while i<N:
        valor=mpq.min(orden)
        valores.append(valor)
        res[valor]=[]
        mpq.delMin(orden)
        i+=1
    itval=it.newIterator(values)
    itke=it.newIterator(keys)
    while it.hasNext(itval):
        val=it.next(itval)
        ke= it.next(itke)
        if ke!= "Independent Owner":
            for i in valores:
                if i==val[1]:
                    if ke not in res[i]:
                        res[i].append(ke)
    return res

def topM(theServices,M):
    valores=[]
    res={}
    i=0
    keys= m.keySet(theServices)
    values=m.valueSet(theServices)
    itv=it.newIterator(values)
    itk=it.newIterator(keys)
    orden=mpq.newMinPQ(comparemaxpq)
    while it.hasNext(itv):
        valu=it.next(itv)
        key= it.next(itk)
        value=int(lt.size(valu[0]))
        if key!= "Independent Owner":
            mpq.insert(orden,value)
    while i<M:
        valor=mpq.min(orden)
        valores.append(valor)
        res[valor]=[]
        mpq.delMin(orden)
        i+=1
    itval=it.newIterator(values)
    itke=it.newIterator(keys)
    while it.hasNext(itval):
        valor=it.next(itval)
        ke= it.next(itke)
        val=int(lt.size(valor[0]))
        if ke!= "Independent Owner":
            for i in valores:
                if i==val:
                    if ke not in res[i]:
                        res[i].append(ke)
    return res
def allTaxisCompanies(theServices):
    taxis= lt.newList('ARRAY_LIST',compare)
    companies=0
    keys= m.keySet(theServices)
    values=m.valueSet(theServices)
    itv=it.newIterator(values)
    itk=it.newIterator(keys)
    while it.hasNext(itv):
        value=it.next(itv)
        key= it.next(itk)
        valit=it.newIterator(value[0])
        while it.hasNext(valit):
            taxi=it.next(valit)
            if lt.isPresent(taxis,taxi)==0:
                lt.addLast(taxis,taxi)
        if key!= "Independent Owner":
            companies+=1
    num_taxis=lt.size(taxis)
    t=(num_taxis,companies)
    return t

def theBestRoute(graph,station1,station2,timemin,timemax):
    best=None
    bestpath=None
    besttime=100000000
    timemax=timechange(timemax)
    timemin=timechange(timemin)
    i=timemin
    while i<=timemax:
        
        stationstart=station1+";;"+str(i)
        stationend=station2+";;"+str(i)
        if gr.containsVertex(graph,stationstart):
            dijk=djk.Dijkstra(graph,stationstart)
            wa=djk.pathTo(dijk,stationend)
            y=djk.distTo(dijk,stationend)
            if wa!=None:
                if y<=besttime:
                    besttime=y
                    best =i
                    bestpath= wa
        i+=15
    if best!=None:
        best=timechangeback(best)
    way=[best,bestpath,besttime]

    return way 


# ==============================
# Funciones Helper
# ==============================
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

def timechange(hour):
    timehour= int(hour[0:2])*60
    timemin= (int(hour[3:5])//15)*15
    timestamp=timehour+timemin
    return timestamp
def timechangeback(timestamp):
    timehour=timestamp//60
    timemin=timestamp%60
    
    hour=str(timehour)+":"+str(timemin)
    if timemin==0:
        hour=str(timehour)+":"+"00"
    return hour
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

def compareCompanies(c1, ser2):
    """
    Compara dos compañias
    """
    c2=ser2['key']
    if (c1 == c2):
        return 0
    elif (c1 > c2):
        return 1
    else:
        return -1


def comparemaxpq(x1, x2):
    """
    Compara dos elementos
    """
    if (x1 == x2):
        return 0
    elif (x1 < x2):
        return 1
    else:
        return -1