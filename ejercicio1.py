#Soy un comentario
'''valorA = 1
valorB = 2
saludo = "Hola mundo"

suma = valorA + valorB
print (saludo, suma)
nombre = "José Alejandro"
resultado = valorB * nombre
print (resultado)

#Entrada de Datos
print("Ingrese el precio de el presupuesto")
presupuesto = int(input())
print("Ingrese el precio de el paquete de frutas")
frutas = int(input())
print("Ingrese el precio de el paquete de verduras")
verduras = int(input())
print("Ingrese el precio de el paquete de granos")
granos = int(input())
print(frutas, verduras, granos)
#x-3 + y-2 + z-5 <= presupuesto
resultadoecuacion = (frutas + verduras + granos)

if resultadoecuacion <= presupuesto:
    print ("Tu gasto es", resultadoecuacion, "y es menor a tu presupuesto")
else:
    print("no te alcanza bb")'''
    
#Funciones
print("Ingrese el precio de el presupuesto")
presupuesto = int(input())
print("Ingrese el precio de el paquete de frutas")
frutas = int(input())
print("Ingrese el precio de el paquete de verduras")
verduras = int(input())
print("Ingrese el precio de el paquete de granos")
granos = int(input())
def funcion(x, y, z):
    valor = (x-3 + y-2 + z-5)
    if(valor<presupuesto):
        print("Usted es un buen comprador")
    elif(valor==presupuesto):
        print("Cuidado bb")
    elif(valor>presupuesto):
        print("Usted no aprende verdad")
        
funcion(frutas,verduras,granos)