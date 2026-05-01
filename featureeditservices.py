import json
import utilidades

def editar_servicio():
    
    listas_servicios = utilidades.leerJson()
    codigo = utilidades.validarEnteros("Digita el codigo del servicio")
    ServicioEncontrado = utilidades.buscarServicio (codigo)

    if lista_servicios:
        
        nombre = utilidades.valiarStr(" Ingrese el nombre del servicio: ")
        precio = utilidades.valiarStr(" Ingrese la duracion : ")
        evento = utilidades.validarFloat(" Ingrese el precio : ")
        duracion = utilidades.validarEntero(" Ingrese el tipo de evento : ")
        for servicio in lista_servicios:
            if codigo == servicio ["codigo"]:
                servicio["nombre"] = nombre
                servicio["precio"] = precio
                servicio["evento"] = evento
                servicio["duracion"] = duracion
        utilidades.escrbirJson(lista_servicios)
        print("servicio actualizado corretamente")
    else: 
        print ("no se encontro el servicio con el codigo asignado")
        