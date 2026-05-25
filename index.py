# Mensaje de bienvenida;

print("\n*****Bienvenido/a a CodeMarket*****"); 

# Inicio de ciclo; 

while True:
    
    print("\nPara comprar necesitamos los siguientes datos:"); 

    userRut = int(input("\nDigita los 8 primeros digitos de tu rut: ")); 
    userName = str(input("Digita tu nombre: ")); 
    
    # Creacion de menu
    
    try:
        
        print("\n*****Articulos disponibles*****");  
         
        print("1. Espada"); 
        print("2. Arco"); 
        print("3. Baston"); 
        
        print("0. Salir"); 
        
        opcion = int(input("\nPor favor, digite una opcion: "));  
        
        if opcion == 1:
            
            valorEspada = int(print("La espada tiene un valor de:", 5000)); 
            
            cantidad = int(input("¿Cuantas espadas deseas llevar?: ")); 
            
        elif opcion == 2:
            
            valorEspada = int(print("El arco tiene un valor de:", 7000)); 
            
            cantidad = int(input("¿Cuantos arcos deseas llevar?: ")); 
        
        elif opcion == 3:
            
            valorEspada = int(print("El Baston tiene un valor de:", 9000)); 
            
            cantidad = int(input("¿Cuantos bastones deseas llevar?: ")); 
            
        elif opcion == 0:
            
            if cantidad <= 0:
                
                print("\nEn esta ocasion no se imprimira boleta"); 
                break; 
                
            else:
                
                print("\n*****Boleta*****"); 
                
                print(f"\nNombre:{userName}"); 
                print(f"Rut:{userRut}"); 
                print(f"Cantidad de articulos{cantidad}"); 
        else: 
            
            print("\n¡ERROR!, seleccione una opcion valida"); 
            
            
        
         
        
    except Exception:
        
        print("\n¡ERROR!, digite una opcion valida"); 
        
    finally:
        
        print("\n¡Muchas gracias, vuelva pronto!"); 
        print("\n*****Finalizando programa*****"); 
        