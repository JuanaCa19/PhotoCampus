import utilidades


def crear():
    lista =[]
    codigo = utilidades.validarEntero("Digite el codigo del servicio: ")
    nombre = utilidades.validarStr("Ingrese el nombre del servicio: ")
    duracion = utilidades.validarEntero("Ingrese la duracion en horas: ")
    precio = utilidades.validarFloat("Ingrese el precio: ")
    evento = utilidades.validarTipoEvento("Ingrese el tipo de evnto: ")

    servicio = dict(
        codigo = codigo,
        nombre = nombre,
        duracion = duracion,
        precio = precio,
        evento = evento
    )
    
    lista=utilidades.leerJson()

    lista.append(servicio)

    utilidades.escribirJson(lista)



