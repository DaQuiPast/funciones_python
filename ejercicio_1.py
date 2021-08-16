# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor en pantalla
    numero = max(numero_1, numero_2)
    print('el numero mayor es:', numero)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Complete la función "imprimir_mayor"
    numero_1 = int(input('Ingrese el primer valor:\n'))
    numero_2 = int(input('Ingrese el segundo valor:\n'))
    
    imprimir_mayor(numero_1, numero_2)

    print("terminamos")