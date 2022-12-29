### STRINGS ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))
print(my_string +" - "+ my_other_string)

my_new_line_String = "Este es un string\ncon salto de linea"
print(my_new_line_String)

my_tab_String = "\tEste es un string con tabulacion"
print(my_tab_String)

my_scape_String = "\tEste es un string\nescapado"
print(my_scape_String)

# FORMATEO

name, surname, age = "Dariana", "Parada", 22

print("Mi nombre es {} {} y mi edad es {}".format(name, surname,age))
print("Mi nombre es %s %s y mi edad es de %d" %(name, surname,age)) # Manera correcta %s->string %d->enteros %f->flotante
print(f"Mi nombre es {name} {surname} y  tengo {age} años de edad")

# DESEMPAQUETADO DE CARACTERES
language = "python"
a, b, c, d, e, f= language
print(a)
print(e)
print(f)

# DIVISION

language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[-2]
print(language_slice)
language_slice = language[1:2:4]
print(language_slice)

# REVERSE
reverse_language = language[::-1]
print(reverse_language)

# FUNCIONES DEL SISTEMA
print(language.capitalize()) #primer letra en mayuscula
print(language.upper()) # todo mayuscula
print(language.count("t")) #contar letras tiene
print(language.isnumeric()) #pregunta si es un numero (false - true)
print(language.lower()) # todas minusculas
print(language.upper().isupper()) #pasar a mayuscula y con comprobacion (false - true)
print(language.startswith("py")) #preguntar si la palabra tiene las letras que se le indiquen
