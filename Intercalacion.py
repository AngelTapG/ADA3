def pedir_lista(numero_lista):
    """
    Solicita al usuario introducir los elementos de una lista.
    
    Args:
    numero_lista (int): Número de la lista (1 o 2)
    
    Returns:
    list: Lista de números introducidos por el usuario
    """
    while True:
        try:
            
            n = int(input(f"Introduce la cantidad de elementos para la lista {numero_lista}: "))
            
            
            lista = []
            
            
            print(f"Introduce los {n} elementos de la lista {numero_lista} en orden:")
            for i in range(n):
                elemento = int(input(f"Elemento {i+1}: "))
                lista.append(elemento)
            
            
            if lista != sorted(lista):
                print(f"ATENCIÓN: La lista {numero_lista} no está ordenada. Se ordenará automáticamente.")
                lista.sort()
            
            return lista
        
        except ValueError:
            print("Error: Introduce un número válido.")

def intercalacion_con_pasos(lista1, lista2):
    """
    Método de intercalación con muestra de pasos.
    
    Args:
    lista1 (list): Primera lista ordenada
    lista2 (list): Segunda lista ordenada
    
    Returns:
    list: Lista combinada y ordenada
    """
    resultado = []
    i, j = 0, 0
    paso = 1
    
    print("\n--- PROCESO DE INTERCALACIÓN ---")
    print(f"Lista 1 inicial: {lista1}")
    print(f"Lista 2 inicial: {lista2}")
    
    while i < len(lista1) and j < len(lista2):
        print(f"\nPaso {paso}:")
        print(f"Comparando: {lista1[i]} de lista 1 vs {lista2[j]} de lista 2")
        
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            print(f"Se agrega {lista1[i]} de lista 1")
            i += 1
        else:
            resultado.append(lista2[j])
            print(f"Se agrega {lista2[j]} de lista 2")
            j += 1
        
        print(f"Estado actual de resultado: {resultado}")
        paso += 1
    
    
    while i < len(lista1):
        print(f"\nPaso {paso}: Agregando resto de lista 1")
        resultado.append(lista1[i])
        print(f"Se agrega {lista1[i]} de lista 1")
        print(f"Estado actual de resultado: {resultado}")
        i += 1
        paso += 1
    
    
    while j < len(lista2):
        print(f"\nPaso {paso}: Agregando resto de lista 2")
        resultado.append(lista2[j])
        print(f"Se agrega {lista2[j]} de lista 2")
        print(f"Estado actual de resultado: {resultado}")
        j += 1
        paso += 1
    
    print("\n--- RESULTADO FINAL ---")
    print(f"Lista intercalada: {resultado}")
    
    return resultado

def main():
    print("PROGRAMA DE INTERCALACIÓN DE LISTAS")
    
    
    lista_1 = pedir_lista(1)
    lista_2 = pedir_lista(2)
    
    
    intercalacion_con_pasos(lista_1, lista_2)


if __name__ == "__main__":
    main()