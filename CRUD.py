#Aplicación CRUD -  Información de empleados
#############################################

#Información personal (desde el código)

Empleados= {
    '1053244': { 
            'Nombre':'Miguel',
            'Apellido' : 'Puerto',
            'Edad' : 60,
            'Correo' : 'Puerto.Miguel@gmail.com',
            'Telefono' : '3209867534', 
            'Dirección' : 'KR 39 #12-45 Bogotá. ', 
            'Cargo' : 'Contador'},
    '104577': { 
            'Nombre':'Fabio',
            'Apellido' : 'Rodriguez',
            'Edad' : 24,
            'Correo' : 'Fabio.rodriguez23445@gmail.com',
            'Telefono' : '3202747534', 
            'Dirección' : 'KR 23 #125-45 Bogotá. ', 
            'Cargo' : 'Analista'},
    '23456': { 
        'Nombre':'Nataly',
        'Apellido' : 'Pacheco',
        'Edad' : 29,
         'Correo' : 'Nataly.p23@gmail.com',
         'Telefono' : '31039867534', 
         'Dirección' : 'KR 234 #12-45 Bogotá. ', 
         'Cargo' : 'Axiliar contable'}}
mainloop = True
while mainloop:
  print(" ")
  print("-- Aplicación CRUD TareasPendientes ---")
  print("1. Adicionar Empleado")
  print("2. Consultar Lista Empleados")
  print("3. Actualizar información del empleado")
  print("4. Eliminar Empleado")
  print("5. Salir")
  opcion = int(input("Ingrese una opción: "))

  if opcion == 1:
    def create(Empleados,id,informacion):
      print()
      print("->Adicionando Empleado")
      id = int(input("Ingrese el ID del empleado: "))
      Nombre = str(input("Ingrese el nombre del empleado: "))
      Apellido = str(input("Ingrese el apellido del empleado: "))
      Edad = int(input("Ingrese la edad del empleado: "))
      Correo = str(input("Ingrese el correo del empleado: "))
      Telefono = int(input("Ingrese el telefono del empleado: "))
      Dirección = str(input("Ingrese la dirección del empleado: "))
      Cargo = str(input("Ingrese el cargo del empleado: "))


    
        
      informacion = {
            'Nombre':Nombre,
            'Apellido' :Apellido,
            'Edad' : Edad,
            'Correo' : Correo,
            'Telefono' : Telefono, 
            'Dirección' :Dirección, 
            'Cargo' : Cargo    
                    }
        
        #Adicionar la tarea
 
      Empleados[id] = informacion
      return Empleados
    create(Empleados,id,informacion)



#Funcionalidades (Procedimientos o rutinas -> backend)
#-----------------------------------------------------
  if opcion == 2:
    def read(Empleados):
      #Read
    
      print()
      print("->Listado de empleados")
      print()

      for id, empleado in Empleados.items():
        print(id,' - ',end='')
        for nombre_atributo, atributo in empleado.items():
          print(atributo, ', ', end='')
        print() 

        #Lectura de tareas
        
    read(Empleados)


#Funcionalidades (Procedimientos o rutinas -> backend)
#-----------------------------------------------------

  if opcion == 3:
    def estaElemento(id, Empleados):
 
    #Update

      print()
      print("->Actualizar Empleado")
      print()

     
        
        #Solicitar al usuario el identificador
      id = int(input("Ingrese ID del empleado para modificar: "))        
                    

        #Revisar si se encuentra el elemento solicitado        
      conjuntoIdentificadores = set(Empleados.keys())
      #Revisar si se encuentra el elemento solicitado        
      if id in conjuntoIdentificadores:
        nuevoNombre = str(input('Nuevo Nombre: '))
        if nuevoNombre:
          Empleados[id]['Nombre'] = nuevoNombre
      
        nuevoApellido = str(input('Nuevo apellido: '))
        if nuevoApellido:
          Empleados[id]['Apellido'] = nuevoApellido

        nuevaEdad = int(input('Nueva Edad: '))
        if nuevaEdad:
          Empleados[id]['Edad'] = nuevaEdad
            
        nuevoCorreo = str(input('Nuevo Correo: '))
        if nuevoCorreo:
          Empleados[id]['Correo'] = nuevoCorreo
            
        nuevoTelefono = int(input('Nuevo Telefono: '))
        if nuevoTelefono:
          Empleados[id]['Telefono'] = nuevoTelefono
          
        nuevaDirección = str(input('Nueva Dirección: '))
        if nuevaDirección:
          Empleados[id]['Dirección'] = nuevaDirección

        nuevoCargo = str(input('Nuevo Cargo: '))
        if nuevoCargo:
          Empleados[id]['Cargo'] = nuevoCargo
      else:
        print("No ha sido encontrado el empleado!")     

    estaElemento(id, Empleados)           


#Funcionalidades (Procedimientos o rutinas -> backend)
#-----------------------------------------------------      
    #Delete
  if opcion == 4:
    def update():


      print()
      print("->Eliminar ")
      print()
        
         #Solicitar al usuario el identificador

        
        #Extraer de la base de datos (contenedor) los identificadores  

    id = str(input("Ingrese ID del empleado para eliminar: "))

    conjuntoIdentificadores = set(Empleados.keys())
        
        #Revisar si se encuentra el elemento solicitado        
    if id in conjuntoIdentificadores:
                  #Proceder a eliminar
            #------------------- 
      Empleados.pop(id)  
      print("El usuario ha sido eliminado exitosamente eliminar!")
              

      
        
        #Revisar si se encuentra el elemento solicitado        
      
                  #Proceder a eliminar
            #------------------- 

             
            
    else:
        print("No ha sido encontrado el empleado para eliminar!")
      
    update()  


#Funcionalidades (Procedimientos o rutinas -> backend)
#-----------------------------------------------------
        
  if opcion == 5:
    print("Ha salido exitosamente.")
    mainloop = False
