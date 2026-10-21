"""
Módulo: validar_compra
Asignatura: Testing & Quality Assurance (TQA)
Actividad: Examen Práctico Hito 3 - Análisis de Caja Blanca

Este módulo implementa la lógica de validación de compras sujeta
a análisis estructural (caja blanca), cálculo de complejidad ciclomática
y diseño de casos de prueba con criterios de cobertura.
"""

def validar_compra(edad: int, cuenta_activa: bool, saldo: float, monto: float) -> str:
    """
    Valida si una transacción de compra puede ser aprobada o no de acuerdo
    a la edad del usuario, el estado de la cuenta y los fondos disponibles.

    Parámetros:
        edad (int): Edad del usuario en años.
        cuenta_activa (bool): Estado de la cuenta (True si está activa, False si está suspendida/inactiva).
        saldo (float): Saldo monetario disponible en la cuenta.
        monto (float): Monto monetario de la compra que se desea procesar.

    Retorna:
        str: Cadena descriptiva del resultado de la validación:
            - "Compra no permitida: edad" : si el usuario es menor de 18 años.
            - "Compra no permitida: cuenta" : si la cuenta no se encuentra activa.
            - "Compra aprobada" : si la cuenta tiene saldo suficiente y el monto es positivo.
            - "Compra rechazada" : si no cumple las condiciones de saldo o monto.
    """
    if edad < 18:
        return "Compra no permitida: edad"
    if not cuenta_activa:
        return "Compra no permitida: cuenta"
    if saldo >= monto and monto > 0:
        return "Compra aprobada"
    return "Compra rechazada"


if __name__ == "__main__":
    print("=" * 60)
    print("  EJECUCIÓN DE PRUEBA: Función validar_compra")
    print("=" * 60)
    
    casos_demo = [
        {"desc": "Menor de edad", "edad": 17, "activa": True, "saldo": 1000.0, "monto": 100.0},
        {"desc": "Mayor de edad, cuenta inactiva", "edad": 25, "activa": False, "saldo": 1000.0, "monto": 100.0},
        {"desc": "Mayor de edad, cuenta activa, saldo suficiente", "edad": 30, "activa": True, "saldo": 500.0, "monto": 200.0},
        {"desc": "Mayor de edad, cuenta activa, saldo insuficiente", "edad": 22, "activa": True, "saldo": 50.0, "monto": 100.0},
        {"desc": "Mayor de edad, cuenta activa, monto no positivo (cero)", "edad": 22, "activa": True, "saldo": 500.0, "monto": 0.0},
    ]

    for i, c in enumerate(casos_demo, 1):
        resultado = validar_compra(c["edad"], c["activa"], c["saldo"], c["monto"])
        print(f"[{i}] {c['desc']}")
        print(f"    Entradas  : edad={c['edad']}, cuenta_activa={c['activa']}, saldo={c['saldo']}, monto={c['monto']}")
        print(f"    Resultado : '{resultado}'\n")
