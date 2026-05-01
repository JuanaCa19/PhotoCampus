import json
import utilidades

def editar_servicio():
    
    listas_servicios = utilidades.leerJson()
    codigo = utilidades.validarEntero("Digita el codigo del servicio")
    ServicioEncontrado = utilidades.buscarServicio (codigo)

    if ServicioEncontrado:
        nombre   = utilidades.validarStr("Ingrese el nombre del servicio: ")
        precio   = utilidades.validarFloat("Ingrese el precio: ")
        evento   = utilidades.validarTipoEvento("Ingrese el tipo de evento(Boda/Retrato/Producto): ")
        duracion = utilidades.validarEntero("Ingrese la duracion: ")
        for servicio in listas_servicios:
           
            if codigo == servicio ["codigo"]:
                servicio["nombre"]   = nombre
                servicio["precio"]   = precio
                servicio["evento"]   = evento
                servicio["duracion"] = duracion

        utilidades.escribirJson(listas_servicios)
        print("servicio actualizado corretamente")
    else: 
        print ("no se encontro el servicio con el codigo asignado")
        