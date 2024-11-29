###Operadores aritméticos###
'''
print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print (10 % 2)
print (10 % 3)
print (10 // 3) #División aproximada a un número entero
print (2 ** 3)

print ("Hola" + "Python")
print ("Hola " + str(5))

###Operadores comparativos: Sólo nos sirve para decirnos si algo es verdadero o falso### 

print (3 > 4) #False
print (3 < 4) #Verdadero
print (3 >= 4) #Falso
print (3 <= 4) #Verdadero
print (3 != 4) #Verdadero


#Comparación de longitud de caracteres

print ("Hola" > "Python") #False
print ("Hola" < "Python") #Verdadero
print ("Hola" >= "Python") #Falso
print ("Hola" <= "Python") #Verdadero
print ("Hola" == "Python") #Falso
print ("Hola" != "Python") #Verdadero
print ("AAAA" >= "aaaa") #Falso - Ordenación alfabética por ASCII
print ("AAAA" <= "aaaa") #Verdadero - Ordenación alfabética por ASCII

'''
###Operadores lógicos###
print (3 > 4 and "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print (3 < 4 and "Hola" < "Python")
print (3 < 4 or "Hola" < "Python")
#print (3 > 4 not "Hola" > "Python")



'''
### Ejemplo de chat GPT###
# Operador AND
print("Operador AND:")
print(f"True AND True   = {True and True}")   # True
print(f"True AND False  = {True and False}")  # False
print(f"False AND True  = {False and True}")  # False
print(f"False AND False = {False and False}") # False

print("\nOperador OR:")
# Operador OR
print(f"True OR True   = {True or True}")    # True
print(f"True OR False  = {True or False}")   # True
print(f"False OR True  = {False or True}")   # True
print(f"False OR False = {False or False}")  # False

print("\nOperador NOT:")
# Operador NOT
print(f"NOT True  = {not True}")  # False
print(f"NOT False = {not False}") # True

print("\nCombinaciones más complejas:")
# Combinaciones
A = True
B = False
print(f"A = {A}, B = {B}")
print(f"(A AND B) OR (NOT A) = {(A and B) or (not A)}") # False
print(f"NOT (A OR B) AND (A AND B) = {not (A or B) and (A and B)}") # False
'''