edades_familiares=[17,15,19,42,45]
print("Las edades de el familiar son:",edades_familiares)

# Consulta de una edad en especifico
print(f"La edad de mi hermana es:{edades_familiares[2]} años")
 
 #modificar edad 
edades_familiares= [1]= 17
print(f"la edad de mi hermana ahora es:{edades_familiares[2]}años")

edades_familiares.append(17)# Añadir una nueva edad al final de la lista
edades_familiares.insert(0, 20) # Insertar una nueva red edad el inicio de la lista
print (edades_familiares)

edades_familiares.remove(45)# Eliminar una edad especifica 
print(edades_familiares)

edades_familiares.sort() # ordenar de las edades de menor a mayor
print(edades_familiares)

edades_familiares.sort()# ordenar de las edades menor o mayor
print(edades_familiares)

edades_familiares.reverse()# invertir   el orden  de las edadee
print(edades_familiares)

print(f"la lista tiene {len (edades_familiares)}edades registradas")