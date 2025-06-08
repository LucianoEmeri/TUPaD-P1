# Hola profe! En este programa aplicamos lo que aprendimos de algoritmos.La idea es mostrar como se ordena y se busca en listas de numeros.

# --- Algoritmos de Ordenamiento (para poner la lista en orden) ---

def bubble_sort(lista_para_ordenar):
    # Este es el Bubble Sort, o "metodo burbuja".
    # Compara un numero con el de al lado y, si estan al reves, los cambia.
    # Repite esto muchas veces hasta que todo queda ordenado.
    
    n = len(lista_para_ordenar)
    
    # Este bucle es para hacer varias "pasadas" por la lista
    for i in range(n):
        # Una bandera para saber si hubo algun cambio en esta pasada
        hubo_cambio = False 
        
        # Este bucle recorre la lista comparando elementos
        # El "- i - 1" es para no mirar los que ya estan ordenados al final
        for j in range(0, n - i - 1):
            # Si el numero de la izquierda es mas grande que el de la derecha...
            if lista_para_ordenar[j] > lista_para_ordenar[j + 1]:
                # ...entonces los cambio de lugar!
                lista_para_ordenar[j], lista_para_ordenar[j + 1] = lista_para_ordenar[j + 1], lista_para_ordenar[j]
                hubo_cambio = True # Si hubo un cambio, lo marco
        
        # Si no hubo ningun cambio en toda esta pasada, es que la lista ya esta ordenada.
        # Asi que puedo parar mas rapido!
        if not hubo_cambio:
            break
            
    return lista_para_ordenar # Devuelvo la lista que ahora esta ordenada

def insertion_sort(mi_lista_para_acomodar):
    # Este es el Insertion Sort, como cuando ordenas cartas en tu mano.
    # Tomas un numero y lo metes en el lugar correcto entre los que ya ordenaste.
    
    n = len(mi_lista_para_acomodar)
    
    # Empiezo desde el segundo elemento de la lista (el primero ya esta "ordenado" solo)
    for i in range(1, n):
        valor_actual = mi_lista_para_acomodar[i] # Guardo el numero que voy a insertar
        posicion_anterior = i - 1 # Empiezo a comparar con el numero de al lado izquierdo
        
        # Mientras no me salga de la lista y el numero de la izquierda sea mas grande...
        while posicion_anterior >= 0 and valor_actual < mi_lista_para_acomodar[posicion_anterior]:
            # Muevo el numero de la izquierda una posicion a la derecha
            mi_lista_para_acomodar[posicion_anterior + 1] = mi_lista_para_acomodar[posicion_anterior]
            posicion_anterior -= 1 # Y sigo comparando hacia la izquierda
            
        # Cuando encuentro el lugar, pongo mi numero ahi
        mi_lista_para_acomodar[posicion_anterior + 1] = valor_actual
        
    return mi_lista_para_acomodar # Devuelvo la lista ordenada

# --- Algoritmos de Busqueda (para encontrar cosas en la lista) ---

def busqueda_lineal(donde_quiero_buscar, lo_que_busco):
    # Esta es la Busqueda Lineal, la mas facil.
    # Revisa cada numero de la lista, uno por uno, hasta que lo encuentra.
    
    # Recorro la lista completa
    for indice in range(len(donde_quiero_buscar)):
        # Si el numero en esta posicion es el que estoy buscando...
        if donde_quiero_buscar[indice] == lo_que_busco:
            return indice # Lo encontre. Devuelvo su posicion
            
    return -1 # Si termine de revisar todo y no lo encontre, devuelvo -1

def busqueda_binaria(lista_que_ya_esta_ordenada, elemento_objetivo):
    # Esta es la Busqueda Binaria, es mas rapida.
    # Pero ATENCION: la lista TIENE que estar ordenada para que funcione bien.
    # Funciona como buscar en un diccionario: siempre vas a la mitad y descartas media parte.
    
    inicio = 0
    fin = len(lista_que_ya_esta_ordenada) - 1
    
    # Sigo buscando mientras el "inicio" no se pase del "fin"
    while inicio <= fin:
        medio = (inicio + fin) // 2 # Calculo el punto medio de la parte que estoy mirando
        
        # Si el numero del medio es el que busco, lo encontre!
        if lista_que_ya_esta_ordenada[medio] == elemento_objetivo:
            return medio 
        
        # Si el numero del medio es mas chico que el que busco,
        # entonces busco en la mitad DERECHA
        elif lista_que_ya_esta_ordenada[medio] < elemento_objetivo:
            inicio = medio + 1 
        
        # Si el numero del medio es mas grande que el que busco,
        # entonces busco en la mitad IZQUIERDA
        else:
            fin = medio - 1 
            
    return -1 # Si no lo encontre despues de buscar en todas las mitades

# --- La parte principal del programa para mostrar todo en accion! ---
# Esto es lo que va a correr cuando ejecute el archivo.

if __name__ == "__main__":
    print("--- Algoritmos de Busqueda y Ordenamiento en Python ---")

    # Primero, probemos el Bubble Sort
    mis_numeros_para_bubble = [64, 34, 25, 12, 22, 11, 90, 5, 88, 30]
    print(f"\nMi lista para Bubble Sort es: {mis_numeros_para_bubble}")
    print("Vamos a ordenarla con el metodo Bubble Sort...")
    # Uso .copy() para que si la necesito despues, la lista no este cambiada
    lista_ordenada_por_bubble = bubble_sort(mis_numeros_para_bubble.copy()) 
    print(f"Lista ordenada con Bubble Sort: {lista_ordenada_por_bubble}")

    # Ahora, probemos el Insertion Sort
    mis_numeros_para_insertion = [50, 10, 40, 20, 30, 70, 60]
    print(f"\nMi otra lista para Insertion Sort: {mis_numeros_para_insertion}")
    print("A ver como la ordena el Insertion Sort...")
    lista_ordenada_por_insertion = insertion_sort(mis_numeros_para_insertion.copy())
    print(f"Lista ordenada con Insertion Sort: {lista_ordenada_por_insertion}")

    # Pasemos a las busquedas! Primero la Lineal.
    # Esta puede buscar en cualquier lista, ordenada o no.
    numero_a_buscar_con_lineal = 22
    print(f"\nVoy a buscar el numero {numero_a_buscar_con_lineal} en mi lista (la de Bubble): {mis_numeros_para_bubble}")
    posicion_lineal_encontrada = busqueda_lineal(mis_numeros_para_bubble, numero_a_buscar_con_lineal)
    if posicion_lineal_encontrada != -1:
        print(f"El numero {numero_a_buscar_con_lineal} esta en la posicion {posicion_lineal_encontrada} (Busqueda Lineal).")
    else:
        print(f"El numero {numero_a_buscar_con_lineal} no esta en la lista (Busqueda Lineal).")

    # Probemos con un numero que se que NO esta
    numero_que_no_esta_lineal = 100
    print(f"Ahora busco el {numero_que_no_esta_lineal} en la misma lista (Busqueda Lineal): {mis_numeros_para_bubble}")
    posicion_lineal_no_encontrado = busqueda_lineal(mis_numeros_para_bubble, numero_que_no_esta_lineal)
    if posicion_lineal_no_encontrado != -1:
        print(f"El numero {numero_que_no_esta_lineal} esta en la posicion {posicion_lineal_no_encontrado} (Busqueda Lineal).")
    else:
        print(f"El numero {numero_que_no_esta_lineal} no esta en la lista (Busqueda Lineal).")


    # Y por ultimo, la Busqueda Binaria.
    # Aca es clave que la lista este ORDENADA. Voy a usar la que ordeno Bubble Sort.
    numero_a_buscar_con_binaria = 25
    print(f"\nVoy a buscar el {numero_a_buscar_con_binaria} en mi lista YA ORDENADA (Busqueda Binaria): {lista_ordenada_por_bubble}")
    posicion_binaria_encontrada = busqueda_binaria(lista_ordenada_por_bubble, numero_a_buscar_con_binaria)
    if posicion_binaria_encontrada != -1:
        print(f"El numero {numero_a_buscar_con_binaria} esta en la posicion {posicion_binaria_encontrada} (Busqueda Binaria).")
    else:
        print(f"El numero {numero_a_buscar_con_binaria} no esta en la lista (Busqueda Binaria).")

    # Y un numero que se que tampoco esta en la lista ordenada
    numero_que_no_esta_binaria = 77
    print(f"Buscando el {numero_que_no_esta_binaria} en la lista ordenada (Busqueda Binaria): {lista_ordenada_por_bubble}")
    posicion_binaria_no_encontrado = busqueda_binaria(lista_ordenada_por_bubble, numero_que_no_esta_binaria)
    if posicion_binaria_no_encontrado != -1:
        print(f"El numero {numero_que_no_esta_binaria} esta en la posicion {posicion_binaria_no_encontrado} (Busqueda Binaria).")
    else:
        print(f"El numero {numero_que_no_esta_binaria} no esta en la lista (Busqueda Binaria).")

    print("\n--- Demostracion Terminada, asi comprobamos como se pueden usar algoritmos de busqueda y ordenamiento en Python ---")