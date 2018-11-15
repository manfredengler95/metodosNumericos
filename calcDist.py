def calcDist(tamObjSensor, distFocalLente, tamObjReal):

    distNodalObj = (tamObjReal * distFocalLente)/ tamObjSensor
    #Está de más decir que deben estar en las mismas unidades  (mm izq y m der  ref: link 8 en documentos_relacionados)
    #Debe cumplir la relación x/f = X/d  (con x tamaño del objeto
    #en el sensor, f distancia focal del lente, X tamaño real del
    # objeto y d distancia desde el punto nodal al objeto  )
    return distNodalObj

def calcTamañoReal(tamObjSensor, distFocalLente, distNodalObj):
    tamañoReal = (tamObjSensor * distNodalObj) / distFocalLente
    return tamañoReal

def calcDistFocalLente(tamObjSensor, distNodalObj, tamObjReal):
    distFocalLente = (tamObjSensor * distNodalObj) / tamObjReal
    return distFocalLente
def verificarRelacion(tamObjSensor, distFocalLente, distNodalObj, tamObjReal):
    if ((tamObjSensor / distFocalLente) == (tamObjReal / distNodalObj)):
        print "Se cumple la relación"
        print (tamObjSensor / distFocalLente) + " == " + (tamObjReal / distNodalObj)
    else:
        print "No se cumple la relación"
        print (tamObjSensor / distFocalLente) + " =/= " + (tamObjReal / distNodalObj)
    return