# Importacion de libreria;

from random import randint;

# Comienzo de programa;

# Comienzo de Ciclo

for i in range (1):

  # Function para incluir una pista;

  def pista(a,b):

    # Retorna un valor multiplicado;

    return a * b; 

  # Mensaje de bienvenida;
  
  print("\n*****Bienvenido/a*****")

  # Intenta, creacion de menu;
  
  try:
    
    print("1. Jugar");  
    print("2. Salir"); 

    # Creacion de variable opcion;
    
    opcion = int(input("\nSeleccione una opcion: ")); 

    # Si opcion 1; 
    
    if opcion == 1:

      # Creacion de variables numericas;
      
      n1 = int(input("\nDigite un numero entero: "));  
      n2 = int(input("Digite un numero entero mayor al anterior: ")); 

      # Creacion de numero random; 
      
      numeroRandom = randint(n1,n2);  

      # Si n2 es mayor a n1;
    
      if n2 > n1: 

        # Creacion de variable vidas;
        
        vidasPrincipal = 3; 

        # Aviso de cantidad de vidas;
        
        vidasAviso = (print(f"\nTienes: {vidasPrincipal} vidas")); 

        # Intento 1;
        
        numeroIntento = int(input("\nAdivina el numero: ")); 

        # Comienzo ciclo de intentos;
        
        for i in range(1):

          # Si la eleccion es correcta;
        
          if numeroIntento == numeroRandom:

            # Mensaje de felicitaciones;
          
            print(f"\nFelicidades el numero: {numeroRandom} es el correcto"); 

          # Si no; 
              
          else:

            # Perdida de vidas;
              
            vidasPrincipal = vidasPrincipal - 1;  

            # Aviso de perdida de vidas; 
            
            print(f"\nRespuesta incorrecta te quedan: {vidasPrincipal} vidas");

            # Mensaje de pista; 

            print(f"\n***** PISTA: El numero multiplicado por 5 da: {pista(numeroRandom, 5)} *****"); 

            # Intento 2; 
            
            numeroIntento = int(input("\nAdivina el numero: ")); 
            
            # Si la eleccion es correcta;
            
            if numeroIntento == numeroRandom:

              # Mensaje de felicitaciones;
          
              print(f"\nFelicidades el numero: {numeroRandom} es el correcto");  
              
            # Si no;

            else:

              # Perdida de vidas;
              
              vidasPrincipal = vidasPrincipal - 1;  

              # Aviso de perdida de vidas; 
            
              print(f"\nRespuesta incorrecta te queda: {vidasPrincipal} oportunidad"); 

              # Ultimo intento; 

              numeroIntento = int(input("\nAdivina el numero: ")); 

              # Si la eleccion es correcta;
              
              if numeroIntento == numeroRandom:

                # Mensaje de felicitaciones;
          
                print(f"\nFelicidades el numero: {numeroRandom} es el correcto"); 

              # Si no; 

              else:

                # Perdida de vida restante;
              
                vidasPrincipal = vidasPrincipal - 1;  

                # Aviso de finalizacion de intentos;
            
                print(f"\nRespuesta incorrecta te quedan: {vidasPrincipal} vidas"); 

                # Mensaje de derrota;
            
                print("\n¡Perdiste!"); 

                # Mensaje con el numero correcto; 

                print(f"\nEl numero era: {numeroRandom}"); 

                # Termino de ciclo;
              
                break; 

    # Si opcion 2; 

    elif opcion == 2: 

      # Mensaje de salida de programa;

      print("\nSaliendo del programa...."); 

  # except Exception para entrada de datos no validos;
                
  except Exception:

    # Mensaje de error;
    
    print("\n¡ERROR!, seleccione una opcion valida"); 
  
  # Finalmente;

  finally:

    # Mensaje de agradecimiento;

    print("\nMuchas gracias por participar"); 

    # Aviso de finalizacion de programa;

    print("*****Programa finalizado*****"); 