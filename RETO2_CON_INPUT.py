def cliente(informacion:dict)-> dict:
   
  # Uso de variables
    id_cliente= informacion['id_cliente']
    nombre= informacion['nombre']
    edad= informacion['edad']
    primer_ingreso  = informacion['primer_ingreso']
     
    if edad >18 and primer_ingreso == 1:
        diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'X-Treme','apto':True, 'primer_ingreso':primer_ingreso, 'total_boleta': round(float(20000*0.95),1)}
    elif edad < 18:
        diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'N/A','apto':False, 'primer_ingreso':primer_ingreso, 'total_boleta':'N/A'}
    elif edad > 18 and primer_ingreso == 0:
        diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'X-Treme','apto':True, 'primer_ingreso':primer_ingreso , 'total_boleta':20000}
    elif edad >= 15 and edad <= 18 and primer_ingreso == 1:
        diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'Carros chocones','apto':True, 'primer_ingreso':primer_ingreso, 'total_boleta': round(float(5000*0.93),1)}
    elif edad <15 or edad > 18 and primer_ingreso == 1:
         diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'N/A','apto':False, 'primer_ingreso':primer_ingreso, 'total_boleta':'N/A'}
    elif edad >= 15 and edad <= 18 and primer_ingreso == 0:
        diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'Carros chocones','apto':True, 'primer_ingreso':primer_ingreso, 'total_boleta':5000}      
    elif  edad >= 7 and edad <15 and primer_ingreso == 1 :
        diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'Sillas voladoras','apto':True, 'primer_ingreso':primer_ingreso, 'total_boleta': round(float(10000*0.95),1)}
    elif edad <7 or edad >=15 and primer_ingreso == 1:
        diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'N/A','apto':False, 'primer_ingreso':primer_ingreso, 'total_boleta':'N/A'}
    elif edad >= 7 and edad <15 and primer_ingreso == 0:
        diccionario_respuesta = {'nombre':nombre, 'edad': edad, 'atraccion':'Sillas voladoras','apto':True, 'primer_ingreso':primer_ingreso, 'total_boleta':10000}  
    else: 
      print(" Datos mal ingresados, intenta nuevamente._.")
      
    return diccionario_respuesta

informacion = {'id_cliente':str(input("Ingresa ID: ")), 'nombre':str(input("Igresa su nombre completo: ")), 'edad':int(input("Ingresa su edad (2-18): ")), 'primer_ingreso':int(input("Igresa 1 si es primer ingreso, 0 si no es primer ingreso: "))}

 

cliente(informacion)
