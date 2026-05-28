
espacios_Disponibles = 60

espacios_DisponiblesAcum = espacios_Disponibles

espacios_ocupados = 0

while True:

  print("\n¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")

  try:

    print("""\n=== MENÚ PRINCIPAL ===

    1. Espacios disponibles

    2. Ocupar espacio

    3. Liberar espacio

    4. Espacios actualmente ocupados

    5. Salir"""); 

    opcion = int(input("\nSelecciona una opcion: "))

    if opcion == 1:

      print(f"\nEspacios disponibles actualmente: {espacios_Disponibles}")

    elif opcion == 2:

      ocupar_Espacio = int(input("\n Digite la cantidad de espacios que desea ocupar: "))

      if ocupar_Espacio < 1 and ocupar_Espacio > espacios_Disponibles:

        print("\n¡ERROR!, digite una opcion valida")

      else:

        espacios_Disponibles -= ocupar_Espacio

        espacios_DisponiblesAcum = espacios_Disponibles

        espacios_ocupados += ocupar_Espacio

        print("\n¡Espacio ocupado de forma exitosa!")


    elif opcion == 3:

      desocupar_Espacio = int(input("\n Digite la cantidad de espacios que desea liberar: "))

      if desocupar_Espacio < 1 and desocupar_Espacio > espacios_Disponibles:

        print("\n¡ERROR!, digite una opcion valida")

      else:

        print("\n¡Espacio desocupado de forma exitosa!")

        cantidad_Restante = desocupar_Espacio + espacios_DisponiblesAcum
        
        espacios_DisponiblesAcum = cantidad_Restante

        print(f"\nQuedan {cantidad_Restante} espacios")


    elif opcion == 4:

      print(f"\nEspacios actualmente ocupados: {espacios_ocupados}")

    elif opcion == 5:

      print("\nGracias por utilizar nuestro software, hasta la próxima.")

      break; 

  except Exception:

    print("¡ERROR!, digite una opcion valida")

  finally:

    print("\n*****Finalizando programa*****")