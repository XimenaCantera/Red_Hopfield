def funcion_activacion(valor, estado_anterior):
    if valor > 0:
        return 1
    elif valor < 0:
        return -1
    else:
        return estado_anterior

"""
    Multiplicar un vector fila (1xN) por una matriz cuadrada (NxN).
    Equivale a la operación U(t) * T
    """
def multiplicar_vector_matriz(vector, matriz):
    
    n = len(vector)
    resultado = []
    
    for j in range(n):
        suma = 0
        for i in range(n):
            suma += vector[i] * matriz[i][j]
        resultado.append(suma)
        
    return resultado

# Matriz de pesos T proporcionada en la imagen
def red_hopfield():
    print("=== Resolviendo Red Hopfield ===")
    
    T = [
        [ 0,  2,  2, -2],
        [ 2,  0,  2, -2],
        [ 2,  2,  0, -2],
        [-2, -2, -2,  0]
    ]
    
    # Patrón inicial A que vamos a evaluar U(0)
    U = [-1, -1, -1, -1]
    
    print(f"Patrón inicial U(0): {U}\n")
    
    iteracion = 0
    while True: # Iteraremos hasta que la red converja (FIN!)
        
        # 1. Multiplicar vector por matriz: U(t) * T
        producto = multiplicar_vector_matriz(U, T)
        print(f"U({iteracion}) * T = {producto}")
        
        # 2. Aplicar función de activación F para obtener U(t+1)
        U_siguiente = []
        for i in range(len(producto)):
            # Pasamos el valor calculado y el estado actual de esa neurona
            nuevo_estado = funcion_activacion(producto[i], U[i])
            U_siguiente.append(nuevo_estado)
            
        print(f"U({iteracion + 1}) = F(U({iteracion}) * T) = {U_siguiente}")
        
        # 3. ¿Es U(t+1) igual a U(t)?
        convergio = True
        for i in range(len(U)):
            if U_siguiente[i] != U[i]:
                convergio = False
                break
                
        if convergio:
            print(f"\nU({iteracion + 1}) = U({iteracion}) => FIN!")
            print(f"El patrón más parecido a A es: {U_siguiente}")
            break
            
        # Si no, actualizamos U para la siguiente vuelta
        U = []
        for val in U_siguiente:
            U.append(val)
            
        iteracion += 1
        print("---")

if __name__ == "__main__":
    red_hopfield()
