# Bienvenida;

print("\n*****Bienvenido/a*****"); 

pikachu_Roll = 4500;  
  
otaku_Roll = 5000;  
  
pulpo_Venenoso_Roll = 5200; 
  
anguila_Electrica_Roll = 4800;

def valorXCantidadAcum(a, b, c, d):
 
  return a + b + c + d; 
  
def valorXcantidad(a,b):
  
  return a * b; 

def descuento(a, b):

  return a / b; 

cantidadAcumPikachu = 0;  

cantidadAcumOtaku = 0;  

cantidadAcumPulpo_V = 0;  

cantidadAcumAnguila_E = 0; 

nombre_usuario = str(input("\nPor favor, digite su nombre: ")); 

codigo_Descuento = "soyotaku"; 
  
nombre_usuario_Len = len(nombre_usuario); 

while True: 
  
  if nombre_usuario.isalpha and nombre_usuario_Len >= 3:
  
    # Menu; 

    print("\nMenu:"); 
  
    print("\n1. Pikachu Roll"); 
    print("2. Otaku Roll"); 
    print("3. Pulpo Venenoso Roll"); 
    print("4. Anguila Electrica Roll"); 
    print("5. Salir"); 
  
  # Solicitud de opcion;
  
    try:
        
      menu_Opcion = int(input("\nDigite una opcion: ")); 
    
      if menu_Opcion == 1:
        
        print(f"\nPikachu Roll tiene un valor de: {pikachu_Roll}"); 
        
        cantidad = int(input("\nSeleccione la cantidad a llevar: ")); 
        
        if cantidad > 0:
          
          print(f"\nEl subtotal seria de: {valorXcantidad(cantidad, pikachu_Roll)}"); 
          
        else: 
        
          print("Seleccione una cantidad valida"); 
      
        cantidadAcumPikachu += cantidad; 
        
      elif menu_Opcion == 2:
        
        print(f"\nOtaku Roll tiene un valor de: {otaku_Roll}"); 
        
        cantidad = int(input("\nSeleccione la cantidad a llevar: ")); 
        
        if cantidad > 0:
          
          print(f"\nEl subtotal seria de: {valorXcantidad(cantidad, otaku_Roll)}"); 
          
        else: 
        
          print("Seleccione una cantidad valida"); 
      
        cantidadAcumOtaku += cantidad; 


      elif menu_Opcion == 3:
        
        print(f"\nPulpo Venenoso Roll tiene un valor de: {pulpo_Venenoso_Roll}"); 
        
        cantidad = int(input("\nSeleccione la cantidad a llevar: ")); 
        
        if cantidad > 0:
          
          print(f"\nEl subtotal seria de: {valorXcantidad(cantidad, pulpo_Venenoso_Roll)}"); 
          
        else: 
        
          print("Seleccione una cantidad valida"); 
      
        cantidadAcumPulpo_V += cantidad; 

      elif menu_Opcion == 4:
        
        print(f"\nAnguila Electrica Roll tiene un valor de: {anguila_Electrica_Roll}"); 
        
        cantidad = int(input("\nSeleccione la cantidad a llevar: ")); 
        
        if cantidad > 0:
          
          print(f"\nEl subtotal seria de: {valorXcantidad(cantidad, anguila_Electrica_Roll)}"); 
          
        else: 
        
          print("Seleccione una cantidad valida"); 
      
        cantidadAcumAnguila_E += cantidad; 
    
      elif menu_Opcion == 5:

        codigo_Pregunta = str(input("¿Posee codigo de descuento? : ")); 

        if codigo_Pregunta == "Si":

          Descuento_Solicitud = str(input("Digitelo a continuacion: "))

          if Descuento_Solicitud == codigo_Descuento:

            print("Se a aplicado un 10% de descuento al total"); 
        
            print("\n*****Boleta*****"); 

            print(f"\nNombre: {nombre_usuario}"); 

            print(f"La cantidad de Pikachu roll es de: {cantidadAcumPikachu}"); 

            print(f"La cantidad de Otaku roll es de: {cantidadAcumOtaku}"); 

            print(f"La cantidad de Pulpo Venenoso roll es de: {cantidadAcumPulpo_V}"); 

            print(f"La cantidad de Anguila Electrica roll es de: {cantidadAcumAnguila_E}"); 

            print(f"El total es de ${descuento(valorXCantidadAcum(valorXcantidad(cantidadAcumPikachu, pikachu_Roll), valorXcantidad(cantidadAcumOtaku, otaku_Roll), valorXcantidad(cantidadAcumPulpo_V, pulpo_Venenoso_Roll), valorXcantidad(cantidadAcumAnguila_E, anguila_Electrica_Roll)), 0.10)} CLP"); 

            break; 

        else:

          print("\n*****Boleta*****"); 

          print(f"\nNombre: {nombre_usuario}"); 

          print(f"La cantidad de Pikachu roll es de: {cantidadAcumPikachu}"); 

          print(f"La cantidad de Otaku roll es de: {cantidadAcumOtaku}"); 

          print(f"La cantidad de Pulpo Venenoso roll es de: {cantidadAcumPulpo_V}"); 

          print(f"La cantidad de Anguila Electrica roll es de: {cantidadAcumAnguila_E}"); 

          print(f"El total es de ${valorXCantidadAcum(valorXcantidad(cantidadAcumPikachu, pikachu_Roll), valorXcantidad(cantidadAcumOtaku, otaku_Roll), valorXcantidad(cantidadAcumPulpo_V, pulpo_Venenoso_Roll), valorXcantidad(cantidadAcumAnguila_E, anguila_Electrica_Roll))} CLP"); 

          break; 

    except Exception: print("\n¡ERROR!, seleccione una opcion valida"); 
    
    finally:
    
      print("\nFinalizando pedido"); 
    
      print("\n*****Muchas gracias, vuelva pronto*****"); 
    
  else: 
    
    print("\n¡ERROR!, el nombre debe tener 3 o mas caracteres"); 

    break; 