import json


def validarStr(mensaje):
    while True:
        texto = str(input(mensaje))
        if not texto.strip():
            print("No se permiten valores vacios!!!")
            continue
        elif len(texto) > 100:
            print("El texto digitado no puede ser tan grande")
            continue
        else:
            return texto

def validarFloat(mensaje):
    while True:

        try:
            numero = float(input(mensaje))

            if numero <= 0:
                print("Digite un precio positivo")
                continue
            else:
                return numero
        except (ValueError,TypeError):
            print("Digite un dato numerico!!!")
            continue

def validarEntero(mensaje):
    while True:

        try:
            numero = int(input(mensaje))

            if numero <= 0:
                print("Digite un codigo positivo")
                continue
            else:
                return numero
        except (ValueError,TypeError):
            print("Digite un dato numerico!!!")
            continue


def validarTipoEvento(mensaje):
    while True:
        evento = input(mensaje)

        if evento not in ("Boda","Retrato","Producto"):
            print("Seleccione un tipo de evento Valido!!!")
            continue
        else:
            return evento

def leerJson():
    with open("servicios.json","r") as file:
        lista = json.load(file)
        return lista


def escribirJson(lista):

    with open("servicios.json", "w") as file:
        json.dump(lista, file, indent=4)

def buscarServicio(codigoIngresado):
    lista = []
    lista = leerJson()
    for servicio in lista:
        if codigoIngresado == servicio["codigo"]:
            return True
    return False