# Se importa la libreria;

from random import randint

# Inicio de programa;

for i in range (1):

  # Se declara la function;

  def resultadoMultiplicacion(a, b):

    return a * b; 

  # Intenta lo siguiente;

  try:

    # Menu

    print("\n*****Bienvenido/a*****");  
    print("\n1. Jugar"); 
    print("2. Salir");  

    # Seleccion de opciones;

    opcion = int(input("\nSelecciona una opcion: ")); 

    # Si opcion 1;

    if opcion == 1:

      n1 = int(input("Digita un numero: ")); 
      n2 = int(input("Digita un numero superior: ")); 

      # Si n2 es mayor a n1

      if n2 > n1:

        # Generacion de numero random;
        
        randomNumber = randint(n1,n2); 

        # Si numero random es mayor a 0;

        if randomNumber > 0: 

          # Intenta lo siguiente;

          try:

            # Menu opcional por si quieres usar decimales para multiplicar;

            print(("\n¿Deseas multiplicar tu numero random con un decimal?: "));  

            print("\n1. Si"); 
            print("2. No"); 

            # Solicitud de ingreso de opcion;

            opcion = int(input(("\nDigita una opcion: "))); 

            # Si opcion 1; 
          
            if opcion == 1:

              # Solicitud de numero decimal;

              SolicitarNumeroMultiplicacion = float(input("Elige un numero decimal para mutiplicar tu resultado: ")); 

              # Muestra de resultados;

              print("\nEl numero aleatorio esta vez fue:", randomNumber); 

              print("Tu resultado es:", resultadoMultiplicacion(randomNumber, SolicitarNumeroMultiplicacion)); 
            
            # Si opcion 2;

            elif opcion == 2:

              # Mensaje de aviso de retorno a la opcion de la linea 97;

              print("\n¡Volviendo al menu tradicional!"); 
            
            # Si la opcion no aparece;

            else:

              print("\n ¡ERROR!, se le llevara de vuelta al menu"); 
          
          # except exception para manejar errores;

          except Exception: print("\n ¡ERROR!, sigue las instrucciones anteriores");  

        # Vuelta a menu principal o continuacion de el primer menu 
          
        SolicitarNumeroMultiplicacion = int(input("\nElige un numero entero para mutiplicar tu resultado: ")); 
        
        # Muestra de resultados;

        print("\nEl numero aleatorio esta vez fue:", randomNumber); 

        print("Tu resultado es:", resultadoMultiplicacion(randomNumber, SolicitarNumeroMultiplicacion));

        # Cierre de ciclo;  

        break; 
      
      # Si opcion 2;

      elif opcion == 2:

        # Mensaje de despedida

        print("\n¡Hasta luego, vuelva pronto!"); 

        # Cierre de ciclo;

        break;  
      
      # Si no se cunplen las condiciones anteriores;

      else:

        print("\n ¡ERROR!, se le llevara de vuelta al menu"); 

  # except exception para manejo de errores en el try principal;  

  except Exception: print("\n ¡ERROR!, sigue las instrucciones anteriores");  

  # Al finalizar en ambos try termina con este mensaje;

  finally:

    print("\nMuchas gracias por participar"); 

    print("\n*****Finalizando programa*****");   