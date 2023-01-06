### TUPLES ###  Guardan datos inmutables
my_tuple = tuple()
my_other_tuple = (60,30,50)

my_tuple = (35, 1.77, "Brais", "Moure")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Brais")) #cantidad de catos iguale
print(my_tuple.index("Moure")) #indice

# my_tuple[1] = 1.80  no se puede asignar otro valor a ese espacio de memoria poruqe ya tiene un valor predeterminado
#print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #seleccionar elementos a buscar

# la tuple no puede ser mutable, la unica manera es que se convierta en lista
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "MoureDev"
my_tuple.insert(1, "Azul")
print(my_tuple)
print(type(my_tuple))

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined