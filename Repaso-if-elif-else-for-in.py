# Se define la Variable;

edad = int(input("Dime tu edad, por favor: ")); 

if edad >= 18:
  
  print("Es mayor");  


  """
  # Sintaxis de if elif else;
  
  if condicion:
    
    bloque = instruccion;
    
  elif otra condicion:
  
    bloque = instruccion;

  else condicion final:
  
    bloque = instruccion;
  
  """
  
  """
  # Sintaxis de ciclo for;
  
  for variable in sencuencia:
  
    instruccion;
    
    cierre de ciclo;
  
  """
  
  # Se crea ciclo for;
  
  for i in range(4,7):
    
    print(i); 
    
  # Se crea un acumulador;
  
  acumulador = 0
  
  for i in range (1, 6):
    
    acumulador = acumulador + 2; 
    
  print("Resultado", acumulador); 
  
  # Bucle for para letras;

  nombre = "Python";  
  
  for letras in nombre:
    
    print(letras);  
    