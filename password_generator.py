import random
import string

def generate_password(lenght):
    letters = string.ascii_letters # Generamos el abecedario en mayusculas y minusculas
    digits = string.digits # Generamos los numeros del 0 al 9
    symbols = string.punctuation # Generamos simbolos y signos de puntuacion 

    all_characters = letters + digits + symbols # Incluimos todo en una variable

    password = [] # Vamos a almacenar el password dentro de una lista
    for i in range(lenght):
        password.append(random.choice(all_characters)) # Agregamos caracteres aleatorios segun la
                                                       # longitud del password ingresada
    
    random.shuffle(password)

    return ''.join(password)

# Ejemplo de uso
length = int(input('Ingrese la longitud del password: '))
new_password = generate_password(length)
print(f"\nPassword generado exitosamente: {new_password}")
if length >= 8:
    print("\nPassword de complejidad alta")
elif length < 8 and length > 5:
    print("Password de complejidad media")
else:
    print("Password de complejidad baja")