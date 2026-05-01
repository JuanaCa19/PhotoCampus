def menu():
    while True:
       print("1. Crear servicio fotográfico")
       print("2. Eliminar servicio fotográfico")
       print("3. Actualizar servicio fotográfico")
       print("4. Salir")

       opcion = input("Selecciona una opción (1-4): ")

       if opcion == "1":
           crear()
       elif opcion == "2":
           eliminar_servicio()
       elif opcion == "3":
           editar_servicio()
       elif opcion == "4":
           print("\n¡Hasta luego! Cerrando PhotoCampus...")
           break
       else:
           print("\n Opción inválida. Por favor elige entre 1 y 4.")


menu()