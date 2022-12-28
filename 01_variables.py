# Variables

#las variables se escriben toda la palabra en minuscula o se utiliza el piso "_" para separar
my_variable = "My string variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en print
print("Hola, tenemos", my_int_variable, "años trabajando en", my_variable)

# Algunas funciones del sistema
print(len(my_variable))

# Variables en una sola linea
name, surname, alias, age ="Brais", "Moure", "MoureDev", 35
print("me llamo", name,"Mis amigos me dicen",alias, "porque mi apellido es",surname,"y tengo", age,"años")

# Input
#name = input('Cual es tu nombre?')
#age = input('cuantos años tienes?')
print(name)
print(age)

# Forzamos el tipo de valor de la varianle?
address: str= "Mi direccion"
address = 32
address = 'chocolate'
address = 12.5
#se queda con el ultimo valor
print(address)
