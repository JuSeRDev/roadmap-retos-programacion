# /*
#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
#  *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
#  *   interpolación, verificación...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas
#  */

string = 'Hola'
string_2 = 'Mundo'

print(string + ' ' + string_2) # Podemos utilizar el operador + para concatenar 2 o mas cadenas de texto
print(string * 3) # podemos utilizar * para multiplicar la cadena de texto
string_2 += ' de Python' # += para agregar texto
print(string_2)
string_3 = string + string_2
print(len(string_3)) # len para calcular obtener el numero de caracteres
print(string_3.find("Mundo")) #find para encontrar el indice de inicio de la subcadena
print(string.find("naruto")) # find devolvera -1 si no se encuentra la subcadena
print(string_3.lower()) # lower para convertir todas las letras a minusculas
print(string_3.upper()) #upper para convertir todas las letras a mayusculas
print(string_3.replace('Python','Java')) # replace para reemplazar un valor por otro
print(string_3[2:6]) # se puede crear subcadena utilizando corchetes con los indices desde el comienzo hasta el final
string_4 = 'Hola con \"Secuencia de escape"' # permite representar caracteres no imprimibles
print(string_4)
string_5 = 'Hola\t mundo' #se puede usar \t para una tabulacion
print(string_5)
string_6 = "Hola\nmundo" # y \n para un salto de linea
print(string_6)