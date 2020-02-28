from collections import deque
cola = deque (["Tesla","Honda","Toyota"])
print ("Carros en espera en Carwash")
print ("Turno 1: ",cola[0])
print ("Turno 2: ",cola[1])
print ("Turno 3: ",cola[2])
cola.append("Ford")
print("Nuevo turno ",cola[3])
cola.popleft()
#Recursividad y funcion que permita agregar y quitar indices
