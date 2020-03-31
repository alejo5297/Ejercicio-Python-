print("Simulación de colas\n\n")
l = float(input("Ingrese la tasa de llegada de los obreros: "))
m = float(input("\nIngrese la capacidad de atención en ventanilla: "))
ofi = float(input("\nCual es el costo de inactividad del oficinista: "))
obr = float(input("\nCual es el costo de inactividad de los obreros: "))
of = 1 - (l/m)
lq = (l**2/(m*(m-l)))
wq = (l/(m*(m-l)))
po = 0.411
p1 = 0.34
lq2 = po * 2.459
of2 = 2*po + p1
costoOf = of * ofi
costoOb = lq * obr
costoOf2 = of2 * ofi
costoOb2 = lq2 * obr
tot1 = costoOf+costoOb
tot2 = costoOf2 + costoOb2
print("\n_____________________________________________________")
print("\n\nLos valores y costos con una ventanilla son: ")
print("\nCon una ventanilla hay "+str(round(lq,3))+" Obreros en cola")
print("\nCon una ventanilla cada obrero espera "+str(round(wq,2))+" minutos en cola")
print("\nEl costo por inactividad del oficinista es: "+str(round(costoOf,2)))
print("\nEl costo por inactividad de los obreros es: "+str(round(costoOb,2)))
print("\nEl costo total para la empresa teniendo UNA ventanilla es: "+str(round(tot1,2)))
print("\n_____________________________________________________")
print("\n\n\nLos valores si hubieran dos ventanillas son: ")
print("\nCon dos ventanillas hay "+str(round(lq2,3))+" Obreros en cola")
print("\nEl costo por inactividad del oficinista es: "+str(round(costoOf2,2)))
print("\nEl costo por inactividad de los obreros es: "+str(round(costoOb2,2)))
print("\nEl costo total para la empresa teniendo DOS ventanillas es: "+str(round(tot2,2)))
if(tot1>tot2):
    print("\n\n\n\nEl costo con una ventanilla es: "+str(round(tot1,2))+", mientras que con dos ventanillas es: "+str(round(tot2,2)))
    print("\nPOR LO QUE ES RECOMENDABLE IMPLEMENTAR OTRA VENTANILLA")

