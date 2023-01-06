## DICTIONARIES ###

my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Dariana", "Apellido":"Parada", "edad":22, 1:"Python"}

my_dict = {
    "Nombre":"Dariana",
    "Apellido":"Parada",
    "edad":22,
    "lenguajes":{"Python", "swift", "kotlin"},
    1:1.77
}
print(my_other_dict)
print(my_dict)

print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict["lenguajes"])

my_dict["Nombre"]= "Pedro"
print(my_dict["Nombre"])
print(my_dict[1])

my_dict["Calle"] = "Calle DariDev"
print(my_dict)

del my_dict["Calle"]  # Manera de eliminar un elemnto del diccionario
print(my_dict)

print("Nombre" in my_dict) # True
print("Pedro" in my_dict) # False - busca el elmento no el valor del elemento

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

print("Pedro" in my_dict.values()) # True

print(my_dict.fromkeys(("Nombre", 1))) # se crea un diccionario nuevo sin valores

my_new_dict = dict.fromkeys(("Name", "Apellido", 2, "piso")) #para crearla de esta manera se utiliza la palabra reservada "dict"
print(my_new_dict)
