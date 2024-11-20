def balanced_merge_sort(arr, paso=0):
    """
    Implementación de Mezcla Equilibrada con impresión de pasos.
    
    Args:
    arr (list): Lista a ordenar
    paso (int): Nivel de recursividad para formateo de impresión
    
    Returns:
    list: Lista ordenada
    """
    
    espaciado = "  " * paso
    print(f"{espaciado}Procesando: {arr}")
    
    
    if len(arr) <= 1:
        print(f"{espaciado}Resultado base: {arr}")
        return arr
    
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    print(f"{espaciado}Dividiendo en: {left_half} | {right_half}")
    
    
    left_sorted = balanced_merge_sort(left_half, paso + 1)
    right_sorted = balanced_merge_sort(right_half, paso + 1)
    
    
    resultado_mezclado = merge(left_sorted, right_sorted, paso)
    
    print(f"{espaciado}Resultado mezclado: {resultado_mezclado}")
    return resultado_mezclado

def merge(left, right, paso):
    """
    Función auxiliar para mezclar dos arreglos ordenados.
    
    Args:
    left (list): Primera lista ordenada
    right (list): Segunda lista ordenada
    paso (int): Nivel de recursividad para formateo de impresión
    
    Returns:
    list: Lista mezclada y ordenada
    """
    espaciado = "  " * paso
    print(f"{espaciado}Mezclando: {left} + {right}")
    
    result = []
    i, j = 0, 0
    
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def main():
    
    while True:
        try:
            
            num_elementos = int(input("Introduce el número de elementos a ordenar: "))
            
            
            digito_min = int(input("Introduce el valor mínimo de los dígitos: "))
            digito_max = int(input("Introduce el valor máximo de los dígitos: "))
            
            
            if num_elementos <= 0 or digito_min > digito_max:
                print("Entrada inválida. Intenta de nuevo.")
                continue
            
            break
        except ValueError:
            print("Por favor, introduce números válidos.")
    
    
    import random
    array_desordenado = [random.randint(digito_min, digito_max) for _ in range(num_elementos)]
    
    print("\n--- PROCESO DE ORDENAMIENTO ---")
    print("Array original:", array_desordenado)
    
    
    array_ordenado = balanced_merge_sort(array_desordenado)
    
    print("\n--- RESULTADO FINAL ---")
    print("Array ordenado:", array_ordenado)


if __name__ == "__main__":
    main()