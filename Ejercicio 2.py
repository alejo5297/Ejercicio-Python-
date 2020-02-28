"""Colas: FIFO"""
#Cola de clientes en un banco
print("Clientes en el banco")
cola = ["Juan","María"]
#Llega nuevo cliente
cola.append("Luis")
#Imprimimos turnos
print("Turnos")
print(cola.index("Juan"),cola.index("María"),cola.index("Luis"))
print (cola)

for nombres in cola:
    print(nombres)
#se atiende un cliente
print("Turno numero: ", cola.index("Juan"))
print (cola[0]," fue atendido")
cola.pop(0)
print (cola)
