print("\n")
print("Funciones creadas por el usuario")

# Funciones
def mi_lis():
    print("Listas")
    amix=["Hugo","Filomeno","Pancracio"]
    for corona in amix:
     print(corona)

def mi_tupla():
   perros=("Hershey","Frida","Frijol")
   print("Tuplas")
   for mascotas in perros:
      print(mascotas)

def mi_conjun():
   print("Conjuntos")
   postres={"helado","pastel","flan"}
   for dulces in postres:
       print(dulces)

def mi_dic():
   print("Diccionarios")
   nombres = {
      "Jesus": " Montes",
      "Maria": " De los angeles",
      "Jose" : "Gutierrez"
   }
   for name,apellido in nombres.items ():
      print(name,apellido)

#llamadas a funciones
mi_lis()
print("\n")
mi_tupla()
print("\n")
mi_conjun()
print("\n")
mi_dic()
print("\n")