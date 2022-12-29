### LISTAS ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [22, 35, 24, 62, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [22, 1.60, "Dariana", "Parada"]
print(my_other_list)
print(len(my_other_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)

my_other_list.append("Pizza") #insertar dato a la lista de ultimo
print(my_other_list)

my_other_list.insert(1, "azul") #insertar dato a la lista en la porsicion que prefiera y los demas datos se corren una posicion
print(my_other_list)

my_other_list.remove("azul") #eliminar
print(my_other_list)

my_list.pop() #quita el ultimo dato de la lista por defecto 
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)