# Inicio de programa;

# Inicio de bucle;

for i in range (1):
  
  # Creacion de function;
  
  def pagoTarjeta(a,b):

    # Valor a retornar;
    
      return a + b; 
    
    # Intenta;
   
  try:

    # Mensaje de bienvenida;

    print ("\n*****Bienvenido*****"); 
    
    # Solicitud de ingreso de KMS 
    
    distancia = float(input("Por favor digite los KMS a recorrer: "));  
    
    # Definimos los valores de descuento y valor mensual 
    
    valorMensual = 95000; 
    descuentoVeinte =  95000 * 0.20; 
    descuentoCatorce = 95000 * 0.14; 
    
    # Intenta; 
    
    try: 
      
      # Menu categorias;
      
      print("\n*****Categorias*****");  
     
      print("\n1."); 
      print("2."); 
      print("3.");  
      print("4."); 
      
      # Definicion de categoria;
      
      categoria = int(input("\n Por favor digite su categoria: ")); 
      
      # Si;
    
      if distancia >= 400 and categoria == 1 or categoria == 2:
        
        # Mensaje de aviso de descuento;
      
        print("\nUsted a obtenido 20 % de descuento"); 
        
        # Intenta;
        
        try:
          
          # Menu tarjeta;
          
          print("\n*****Pago con tarjeta*****"); 
          print("\n1. Si"); 
          print("2. No"); 
          
           # Definicion de pago con tarjeta;
          
          opcionTarjeta = int(input("\nSeleccione una opcion: "));  
          
          # Si;  
          
          if opcionTarjeta == 1:
            
            # Definimos valores finales e imprimimos boleta;
            
            ValorFinalTarjeta = pagoTarjeta(valorMensual, 5000); 
            
            precioFinal = ValorFinalTarjeta - descuentoVeinte;  
            
            print("\n*****Boleta*****"); 
            print(f"Su distancia es: $", distancia); 
            print(f"Su categoria es: $", categoria); 
            print(f"El valor neto es: $", valorMensual);  
            print(f"El valor con tarjeta es: $", ValorFinalTarjeta); 
            print(f"El descuento es de: $", descuentoVeinte); 
            print(f"El valor final es de: $", precioFinal); 
            
          # Si opcion 2;
            
          elif opcionTarjeta == 2:
            
            # Definimos valores finales e imprimimos boleta;
            
            precioFinal = valorMensual - descuentoVeinte;  
            
            print("\n*****Boleta*****"); 
            print(f"Su distancia es: $", distancia); 
            print(f"Su categoria es: $", categoria); 
            print(f"El valor neto es: $", valorMensual); 
            print(f"El descuento es de: $", descuentoVeinte); 
            print(f"El valor final es de: $", precioFinal); 

        # Añadimos excepciones;
            
        except Exception: 
    
          print("\n¡ERROR!, digite un valor valido"); 
          
        # Si;
        
      elif distancia >= 1 or distancia <= 400 and categoria == 3 or categoria == 4:
        
        # Mensaje aviso de descuento;
      
        print("\nUsted a obtenido 14 % de descuento"); 
        
        # Intenta; 
        
        try:
          
          # Menu tarjeta;
          
          print("\n*****Pago con tarjeta*****"); 
          print("\n1. Si"); 
          print("2. No"); 
          
          opcionTarjeta = int(input("\nSeleccione una opcion: ")); 
          
          # Si; 
          
          if opcionTarjeta == 1:
            
            # Impresion de boleta;
            
            ValorFinalTarjeta = pagoTarjeta(valorMensual, 5000); 
            
            precioFinal = ValorFinalTarjeta - descuentoCatorce;  
            
            print("\n*****Boleta*****"); 
            print(f"Su distancia es: $", distancia); 
            print(f"Su categoria es: $", categoria); 
            print(f"El valor neto es: $", valorMensual);  
            print(f"El valor con tarjeta es: $", ValorFinalTarjeta); 
            print(f"El descuento es de: $", descuentoCatorce); 
            print(f"El valor final es de: $", precioFinal); 
            
          # Si opcion 2; 
            
          elif opcionTarjeta == 2:
            
            precioFinal = valorMensual - descuentoCatorce;  
            
            print("\n*****Boleta*****"); 
            print(f"Su distancia es: $", distancia); 
            print(f"Su categoria es: $", categoria); 
            print(f"El valor neto es: $", valorMensual); 
            print(f"El descuento es de: $", descuentoCatorce); 
            print(f"El valor final es de: $", precioFinal); 
            
        # Añadimos excepciones; 
            
        except Exception: 
    
          print("\n¡ERROR!, digite un valor valido");  
          
      # Error manual para opciones invalidas;
        
      else:
        
        print("\n¡ERROR!, digite una opcion valida"); 
        
    # Añadimos excepciones;  
        
    except Exception: 
    
      print("\n¡ERROR!, digite un valor valido");  
    
  # Añadimos excepciones;
  
  except Exception: 
    
    print("\n¡ERROR!, digite un valor valido"); 
    
  # Finalmente, mensaje de despedida y termino de programa;
    
  finally:
    
    print("\n¡Muchas gracias por preferirnos!"); 
    print("\nVuelva pronto"); 
    print("\n*****Finalizando programa*****"); 