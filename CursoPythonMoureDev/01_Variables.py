#Variables

my_string_variable = "My string variable"
print (my_string_variable)

my_int_variable = 5
print (my_int_variable)

my_bool_variable = False
print (my_bool_variable)

#Concatenación de variables en un print
print (my_string_variable, my_int_variable, my_bool_variable)

#Algunas Funciones del sistema
print(len(my_string_variable))

#Variables en una sola línea
name, surname, alias, age = 'Guada', 'Peláez', 'Lupe', 39
print ("Me llamo: ", name, surname, "Mi alias es:", alias, ".Tengo ",age)

#Inputs
#name = input('What is your name: ')
#age = input('How old are you? ')

print(name)
print(age)

#Forzamos el tipo?
address: str = "Mi dirección"
address = 32
print(address)
print(type(address)) 