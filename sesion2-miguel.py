"""
Módulo: Generacion de numeros pseudoaleatorios
Ejercicio 2: Algoritmo secuencial mixto (Líneal)
Formula : X+1 = (a * Xn + c) mod m
    rn = xn / m
Descripcion: Genera números pesudoaleatorios uniformemente distribuidos en (0,1) mediante
relaciones de recurrencia modular

"""

from abc import ABC, abstractmethod
import pandas as pd
from typing import Any, Iterable


def generador_congruencia_mixto(X0: int, a: int, c: int, m: int, n: int) -> pd.DataFrame:
    """
    Genera números pseudoaleatorios uniformemente distribuidos en (0,1) mediante
    relaciones de recurrencia modular.

    Parámetros:
    -----------
    X0 : int Semilla inicial (>0).
    a : int Multiplicador -> (debe ser > 0)
    c : int Incremento (debe ser > 0)
    m : int Módulo.
    n : int Número de números pseudoaleatorios a generar.

    Retorna:
    --------
    pd.DataFrame -> Tabla con los valores de Xn y los pseudo rn
    """
    Xi = X0  # asignamos el valor actual de la semilla
    historial = []  # Lista para guardar los registros en cada paso

    # El periodo máximo posible de este generador es 'm'
    for i in range(n):
        # 1. Aplicamos la formula de congruencial: xn+1 = (a * Xn + c) mod m
        Xi_siguiente = (a * Xi + c) % m

        # 2. Normalizamos el entero obtenido para llevarlo al intervalo (0,1)
        ri = Xi_siguiente / m

        # 3. Guardamos los resultados de la iteracion actual
        historial.append({
            'Iteracion': i + 1,
            'X_i': Xi_siguiente,
            'r_i': ri
        })

        # 4. Actualizamos el valor de Xi para la siguiente iteracion
        Xi = Xi_siguiente

        # Si volvemos a obtener el número de la semilla inicial, el ciclo se repite
        if Xi == X0:
            break

    return pd.DataFrame(historial)

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    # Parámetros probados en clase x0 = 4, A= 5, C=7, M=8
    semilla = 4
    multiplicador = 5
    incremento = 7  
    modulo = 8
    n = 20  # CORRECCIÓN 1: Definir 'n' (la cantidad de iteraciones máximas)
    
    # CORRECCIÓN 2 y 3: Indentación correcta y agregar la 'f' al inicio del string
    print(f"Generador secuencia con X0 = {semilla}, a = {multiplicador}, c = {incremento}, m = {modulo}\n")
    
    # CORRECCIÓN 1 y 3: Agregar 'n' a los argumentos y corregir indentación
    df_numeros = generador_congruencia_mixto(semilla, multiplicador, incremento, modulo, n)

    # Imprimimos la tabla formateada
    print(df_numeros.to_string(index=False))
    
    # CORRECCIÓN 2 y 3: Agregar la 'f' al inicio y corregir indentación
    print(f"\nPeriodo alcanzado: {len(df_numeros)} numeros generados")