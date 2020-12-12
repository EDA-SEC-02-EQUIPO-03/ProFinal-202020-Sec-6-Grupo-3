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
def newAnalyzer():

    try:
        taxis = {
                'theServices': None,
                    '': None,
                    '': None,
                    '': None
                    }
        taxis['theServices']=m.newMap(numelements=1000,
                                     maptype='PROBING',
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
    orden=mpq.newMinPQ(comparemax)
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
    orden=mpq.newMinPQ(comparemax)
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
# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def comparemax(x1, x2):
    """
    Compara dos elementos
    """
    if (x1 == x2):
        return 0
    elif (x1 < x2):
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