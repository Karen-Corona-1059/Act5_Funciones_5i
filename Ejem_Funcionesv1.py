print("\nManjeo de funciones v1")

def funcion():
 print("Hola, aqui estoy dentro de la funcion")
 
def fun2(msj):
 print(msj + "Hola") 
 
def name(nom,ape):
 print(nom + " " + ape)
 print(f"Tu nombre completo es {nom} {ape}")
 #Llamando a la funcion
funcion()

fun2("\nCarlos dice: ")#llama a fun2 con 1 parametro
fun2("Jose dice: ")
print("\n")
name("Karen", "Corona")#Llama a name con 2 paranetros
print("\n")

print("Funciones que regresan valores")
def suma(a,b):
 s=a+b
 #r=f"la suma de {a}+{b} es:{s}"
 return f"la suma de {a}+{b} es:{s}"

print(suma(5,5))
print(suma(3,5))

