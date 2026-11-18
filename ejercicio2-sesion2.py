"""
Módulo: Generación de Números Pseudoaleatorios
Ejercicio 2: Algoritmo Congruencial Mixto (Lineal)
Formula: Xn+1 = (a * Xn + c) mod m
        rn = Xn / m
Descripción: Genera números pseudoaleatroios uniformemente distribuidos en (0,1) mediante relaciones de 
recurrencia modular.
"""

from typing import Any


def _formatear_tabla(historial: list[dict[str, Any]]) -> str:
    """Devuelve una vista tabular simple sin depender de pandas."""
    if not historial:
        return "No se generaron valores."

    columnas = ["Iteración", "X_i", "r_i (0,1)"]
    filas = [[str(registro[col]) for col in columnas] for registro in historial]

    anchos = []
    for idx, columna in enumerate(columnas):
        ancho = max(len(columna), *(len(fila[idx]) for fila in filas))
        anchos.append(ancho)

    linea = "-+-".join("-" * ancho for ancho in anchos)
    cabecera = " | ".join(f"{columna:<{anchos[i]}}" for i, columna in enumerate(columnas))
    cuerpo = [
        " | ".join(f"{valor:<{anchos[i]}}" for i, valor in enumerate(fila))
        for fila in filas
    ]
    return "\n".join([cabecera, linea, *cuerpo])


def generador_congruencia_mixto(XO: int, a: int, c: int, m: int) -> list[dict[str, Any]]:
    """
    Genera una secuencia de números pseudoaleatorios usando el método congruencial mixto.
    Parametros:
    -----------
    XO: int -> Semilla inicial (debe ser > 0)
    a: int -> Multiplicador (debe ser > 0)
    c: int -> Constante aditiva o incremento (debe ser > 0)
    m: int -> Módulo de la operación (m > XO, a, c)

    Retorna:
    --------
    list[dict] -> Tabla con los valores de Xn y los pseudoaleatorios rn
    """

    Xi = XO  # Asignamos el valor actual de la semilla
    historial: list[dict[str, Any]] = []  # Lista para guardar los registros en cada paso

    # El periodo máximo posible de este generador es 'm'
    for i in range(m):
        # 1. Aplicamos la fórmula congruencial: xn+1 = (a * Xn + c) mod m
        Xi_siguiente = (a * Xi + c) % m

        # 2. Normalizamos el entero obtenido para llevarlo al intervalo (0,1)
        ri = Xi_siguiente / m

        # 3. Guardamos los resultados de la iteración actual
        historial.append({
            "Iteración": i + 1,
            "X_i": Xi_siguiente,
            "r_i (0,1)": ri,
        })

        # 4. Actualizamos el valor de Xi para la siguiente iteración
        Xi = Xi_siguiente

        # Si volvemos a obtener el número de la semilla inicial, el ciclo se repite
        if Xi == XO:
            break

    return historial


# ---Bloque principal de ejecución---
if __name__ == "__main__":
    # Parámetros probados en clase XO = 4, a = 5, c = 7, m = 8
    semilla = 4
    multiplicador = 5
    constante_c = 7
    modulo = 8

    print(f"Generador secuencia con XO = {semilla}, a = {multiplicador}, c = {constante_c}, m = {modulo}\n")
    historial_numeros = generador_congruencia_mixto(semilla, multiplicador, constante_c, modulo)

    # Imprimimos la tabla formateada
    print(_formatear_tabla(historial_numeros))
    print(f"\nPeriodo alcanzado: {len(historial_numeros)} numeros generados antes de repetirse.")