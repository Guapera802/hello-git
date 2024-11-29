### Strings ###
'''
my_string = "Mi string"
my_other_string  = "Mi otro string "

print (len(my_string))
print (len(my_other_string))

print (my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de línea"
print (my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

'''

### Formateo ###

name, surname, age = "Guada", "Lupe", 39
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))#Se ponen llaves cuando se usa el format
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")#La f de adelante es para formatear (inferencia) y para que vaya infiriendo el valor de las variables en las llaves

### Desempaquetado de Caracteres ###
languaje = "Python"
