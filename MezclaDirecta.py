def merge_sort(arr):
    # Mostrar estado inicial
    print(f"\n--- INICIO: {arr}")
    
    # Caso base: si la lista tiene 1 o menos elementos, ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    print(f"Dividiendo en: {left_half} | {right_half}")
    
    # Recursivamente ordenar ambas mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combinar las mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    resultado = []
    i = j = 0
    
    print(f"\nCombinando: {left} + {right}")
    
    # Comparar y combinar elementos de ambas listas
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    
    # Agregar elementos restantes
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    
    print(f"Resultado parcial: {resultado}")
    
    return resultado

def main():
    print("PROGRAMA DE ORDENAMIENTO MERGE SORT")
    
    # Solicitar cantidad de elementos
    while True:
        try:
            num_elementos = int(input("Cuántos números desea ordenar? "))
            break
        except ValueError:
            print("Por favor, introduzca un número válido")
    
    # Solicitar tipo de entrada
    while True:
        tipo_entrada = input("Desea introducir números (M)anualmente o (A)leatorios? ").upper()
        if tipo_entrada in ['M', 'A']:
            break
        print("Respuesta inválida. Escriba M o A")
    
    # Generar la lista
    if tipo_entrada == 'M':
        lista = []
        for i in range(num_elementos):
            while True:
                try:
                    num = int(input(f"Introduzca el número {i+1}: "))
                    lista.append(num)
                    break
                except ValueError:
                    print("Número inválido. Intente de nuevo.")
    else:
        import random
        lista = [random.randint(1, 1000) for _ in range(num_elementos)]
    
    print("\n--- PROCESO DE ORDENAMIENTO ---")
    lista_ordenada = merge_sort(lista)
    
    print("\n--- RESULTADO FINAL ---")
    print(f"Lista original:  {lista}")
    print(f"Lista ordenada:  {lista_ordenada}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()