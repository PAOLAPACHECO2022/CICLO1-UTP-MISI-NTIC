x = ("._.CALCULADORA MATEMÁTICA ._.\n")
print(x)

for i in range(4):
  p = int(input("Que operación desea realizar, inserta 1 para suma, 2 para resta, 3 para multiplicación, 4 división y -1 para finalizar: "))
  if p==1:
    n = int(input(" Cantidad de #n a + : "))
    TOTAL = 0
    y=0
    while y < n:
      n1= int(input("n{}: ".format(y+1)))
      TOTAL= TOTAL + n1
      y +=1  
    else:
      print("Suma: ", TOTAL)
  if p==2:
    n = int(input(" Cantidad de #n a Restar : "))
    n1= int(input("n1: "))
    y=1
    while y < n:
      n2= int(input("n{}: ".format(y+1)))
      n1 = n1- n2
      y +=1  
    else:
      print("Resta: ", n1)
      
  if p==3:
    n = int(input(" Cantidad de #n a * : "))
    TOTAL = 1
    y=0
    while y < n:
      n1= int(input("n{}: ".format(y+1)))
      TOTAL= TOTAL * n1
      y +=1  
    else:
      print("Multiplicación: ", TOTAL)

  if p==4:
    n = int(input(" Cantidad de #n a Dividir : "))
    n1= int(input("n1: "))
    y=1
    while y < n:
      n2= int(input("n{}: ".format(y+1)))
      n1 = n1/n2
      y +=1  
    else:
      print("División: ", n1)
  if p ==-1:
    break
print("FIN DEL PROGRAMA")

###########################################################################
CALCULADORA MATEMATICA CON  LAMNDA
# Calculadora matemática-Con lambda
n1=float(input("Inserte el primer número: "))
n2=float(input("Inserte el segundo número: "))
p = int(input("Que operación desea realizar, inserta 1 para suma, 2(resta), 3(multiplicación),4(división): "))
if p==1:
  suma = lambda x, y :x+y
  print(suma(n1,n2))
if p==2:
  resta = lambda x, y :x-y
  print(resta(n1,n2))
if p==3:
  multiplicación = lambda x, y :x*y
  print(multiplicación(n1,n2))
if p==4:
  división = lambda x,y :x/y
  print(división(n1,n2))
  
