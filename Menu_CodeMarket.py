# Mensaje de bienvenida;

print("\n*****Bienvenido/a a CodeMarket*****"); 

# Definimos las variables que se acumularan; 

cantidad = 0; 

espadas = 0; 

arcos = 0; 

bastones = 0; 

subtotal = 0; 

# Inicio de ciclo;

while True:
    
    # Solicitud de ingreso de datos;
    
    print("\nPara comprar necesitamos los siguientes datos:");  

    userRut = input("\nDigita los 8 primeros digitos de tu rut: "); 

    # Se ocupa len y isdigit para filtrar que el rut cumpla con los parametros solicitados;
 
    userRutFiltro = len(userRut); 

    # Si;

    if userRutFiltro == 8 and userRut.isdigit():

      # Solicitud de nombre;

      userName = str(input("Digita tu nombre: ")); 
  
    # Creacion de menu

    # Intenta;
    
      try:
          
          # Definimos los valores de los productos;

          valorEspada = int(5000); 

          valorArco = int(7000); 

          valorBaston = int(9000); 

          # Functions para cada producto para sacar el resultado de total por cantidad;

          def cantidadEspada(a, b):
             
             return a * b
          
          def cantidadArco(a, b):
             
             return a * b
          
          def cantidadBaston(a, b):
             
             return a * b
          
          # Function cantidad total de productos;
          
          def cantidadTotal(a, b, c):
             
             return a + b + c
          
          # Function de calculo de iva;
          
          def iva(a, b):
             
             return a * b
          
          # Menu de opciones;
        
          print("\n*****Articulos disponibles*****");  
         
          print("1. Espada"); 
          print("2. Arco"); 
          print("3. Baston"); 

          print("\n*****Otros*****")
        
          print("0. Salir"); 

          # Solicitud de opcion;
        
          opcion = int(input("\nPor favor, digite una opcion: ")); 

          # Si es 1; 
        
          if opcion == 1:

            # Mensaje informativo;

            mensajeValorEspada = print(f"\nLa espada tiene un valor de: {valorEspada}"); 

            # Solicitud de cantidad; 

            cantidad = int(input("¿Cuantas espadas deseas llevar?: ")); 

            # Si cantidad es 0;

            if cantidad == 0:

              # Mensaje informativo;

              print("\nNo se han agregado espadas a tu compra"); 
            
            # Si no;
            
            else:

              # Se acumula la cantidad y valor

              espadas += cantidad; 

              subtotal += cantidadEspada(cantidad, valorEspada); 
            
          elif opcion == 2:
            
            mensajeValorArco = print(f"\nEl arco tiene un valor de: {valorArco}"); 
            
            cantidad = int(input("¿Cuantos arcos deseas llevar?: ")); 

            if cantidad == 0:

              print("\nNo se han agregado arcos a tu compra"); 
            
            else:
          
              arcos += cantidad; 

              subtotal += cantidadArco(cantidad, valorArco); 
        
          elif opcion == 3:
            
            mensajeValorBaston = print(f"\nEl Baston tiene un valor de: {valorBaston}"); 
            
            cantidad = int(input("¿Cuantos bastones deseas llevar?: ")); 

            if cantidad == 0:

              print("\nNo se han agregado bastones a tu compra"); 

            else: 
          
              bastones += cantidad; 

              subtotal += cantidadBaston(cantidad, valorBaston); 
          
          # Si opcion 0;
            
          elif opcion == 0:

            # Si cantidad es mayor a 0 imprime la boleta y termina el programa;
                
            if cantidadTotal(espadas, arcos, bastones) > 0:
              print("\n*****Boleta*****"); 
              print(f"\nNombre: {userName}"); 
              print(f"Rut: {userRut}"); 
              print(f"La cantidad de productos es: {cantidadTotal(espadas, arcos, bastones)}"); 
              print(f"El subtotal es: {subtotal}"); 
              print(f"El total es: {iva(subtotal, 1.19)}"); 

              break; 
            
            # Si no, mensaje informativo;
           
            else:
              
              print("\nEn esta ocasion no se imprimira boleta"); 

      # except Excpetion para manejar errores con los tipos de datos solicitdados; 
                   
      except Exception:

        # Mensaje de error;
        
        print("\n¡ERROR!, digite una opcion valida"); 
      
      # Finalmente;
        
      finally:

        # Imprime el mensaje de agradecimiento y aviso de finalizacion de programa;
        
        print("\n¡Muchas gracias, vuelva pronto!"); 

        print("\n*****Finalizando programa*****"); 
    
    # Si el rut no cumple con el filtro;
    
    else:

      # Mensaje de error y termino de programa;
   
      print("\n¡ERROR!, el rut debe tener 8 digitos numericos"); 

      break;   