import json
import utilidades

def eliminar_servicio():

    listas_servicios = utilidades.leerJson()
    codigo = utilidades.validarEntero("Digita el codigo del servicio")
    ServicioEncontrado = utilidades.buscarServicio (codigo)
    if ServicioEncontrado:

        for servicio in listas_servicios:
            if  servicio["codigo"] == codigo:
                listas_servicios.remove(servicio)
                break
        utilidades.escribirJson(listas_servicios)




