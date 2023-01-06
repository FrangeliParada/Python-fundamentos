### SETS ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicalmente es un dic = diccionario

my_other_set = {"Dariana", "Parada", 22} # Se agregan datos y se convierte en set
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("MoureDev")
print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("MoureDev")
print(my_other_set) # un set no admite repetidos

my_other_set.add("DariDev")
print(my_other_set) # un set se ordena por un "as" interno

# Realizar busquedad
print("Dariana" in my_other_set)
print("Dari" in my_other_set)

# eliminar
my_other_set.remove("Dariana")
print(my_other_set)

# vaciar set
my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set #no funciona

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # No es recomendable porque de igual manera no se va a reconocer el orden de la lista

my_other_set = {"manzana", "pera", "uva"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_set).union({"Caraotas","ensalada", "Dulces"}))

print(my_new_set.difference(my_set))