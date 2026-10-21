"""
Módulo de Pruebas Unitarias: Caja Blanca
Asignatura: Testing & Quality Assurance (TQA)
Examen Práctico Hito 3

Este archivo contiene la suite de pruebas automatizadas basada en las técnicas
de diseño de Caja Blanca para la función `validar_compra`.
Se implementan con unittest (estándar de Python) y son totalmente compatibles con pytest.
"""

import unittest
import sys
import os

# Asegurar que el directorio raíz del proyecto esté en el path para importar src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.validar_compra import validar_compra


class TestCajaBlancaExamen(unittest.TestCase):
    """
    Suite con los 3 casos de prueba requeridos explícitamente en la Diapositiva 8
    del Examen Práctico Hito 3.
    """

    def test_cb_01_menor_de_edad(self):
        """
        Caso CB-01 (Diseño obligatorio 1):
        - Entrada: edad=16, cuenta_activa=True, saldo=500.0, monto=100.0
        - Decisión/Condición cubierta: D1 (edad < 18) evalúa a True.
        - Resultado Esperado: 'Compra no permitida: edad'
        """
        resultado = validar_compra(edad=16, cuenta_activa=True, saldo=500.0, monto=100.0)
        self.assertEqual(resultado, "Compra no permitida: edad")

    def test_cb_02_cuenta_inactiva(self):
        """
        Caso CB-02 (Diseño obligatorio 2):
        - Entrada: edad=20, cuenta_activa=False, saldo=500.0, monto=100.0
        - Decisión/Condición cubierta: D1 evalúa a False, D2 (not cuenta_activa) evalúa a True.
        - Resultado Esperado: 'Compra no permitida: cuenta'
        """
        resultado = validar_compra(edad=20, cuenta_activa=False, saldo=500.0, monto=100.0)
        self.assertEqual(resultado, "Compra no permitida: cuenta")

    def test_cb_03_compra_aprobada(self):
        """
        Caso CB-03 (Diseño obligatorio 3):
        - Entrada: edad=25, cuenta_activa=True, saldo=300.0, monto=150.0
        - Decisión/Condición cubierta: D1 False, D2 False, D3 (saldo >= monto AND monto > 0) True.
        - Resultado Esperado: 'Compra aprobada'
        """
        resultado = validar_compra(edad=25, cuenta_activa=True, saldo=300.0, monto=150.0)
        self.assertEqual(resultado, "Compra aprobada")


class TestCajaBlancaCoberturaCompleta(unittest.TestCase):
    """
    Casos complementarios requeridos para alcanzar el 100% de Cobertura
    de Sentencias, Decisiones y Condiciones (Justificación solicitada en Diapositivas 8 y 9).
    """

    def test_cb_04_compra_rechazada_saldo_insuficiente(self):
        """
        Caso CB-04 (Ajuste para cobertura total de sentencias y rama False de D3):
        - Entrada: edad=30, cuenta_activa=True, saldo=50.0, monto=100.0
        - Decisión/Condición cubierta: D1 False, D2 False, Condición (saldo >= monto) es False.
        - Resultado Esperado: 'Compra rechazada'
        - Ejecuta la última sentencia 'return \"Compra rechazada\"' que los 3 casos base no alcanzaban.
        """
        resultado = validar_compra(edad=30, cuenta_activa=True, saldo=50.0, monto=100.0)
        self.assertEqual(resultado, "Compra rechazada")

    def test_cb_05_compra_rechazada_monto_cero_o_negativo(self):
        """
        Caso CB-05 (Ajuste para cobertura completa de la condición simple monto > 0 a False):
        - Entrada: edad=25, cuenta_activa=True, saldo=500.0, monto=0.0
        - Decisión/Condición cubierta: saldo >= monto es True, pero (monto > 0) es False.
        - Resultado Esperado: 'Compra rechazada'
        """
        resultado = validar_compra(edad=25, cuenta_activa=True, saldo=500.0, monto=0.0)
        self.assertEqual(resultado, "Compra rechazada")


class TestCajaBlancaValoresLimite(unittest.TestCase):
    """
    Pruebas adicionales de valores de frontera / límites (Boundary Value Analysis).
    """

    def test_limite_edad_exacta_18(self):
        """Frontera de edad: edad=18 debe permitir continuar (D1 False)."""
        resultado = validar_compra(edad=18, cuenta_activa=True, saldo=100.0, monto=50.0)
        self.assertEqual(resultado, "Compra aprobada")

    def test_limite_edad_exacta_17(self):
        """Frontera de edad: edad=17 debe bloquearse (D1 True)."""
        resultado = validar_compra(edad=17, cuenta_activa=True, saldo=100.0, monto=50.0)
        self.assertEqual(resultado, "Compra no permitida: edad")

    def test_limite_saldo_igual_a_monto(self):
        """Frontera de saldo: saldo == monto debe ser aprobada (saldo >= monto)."""
        resultado = validar_compra(edad=21, cuenta_activa=True, saldo=100.0, monto=100.0)
        self.assertEqual(resultado, "Compra aprobada")

    def test_limite_saldo_menor_por_un_centavo(self):
        """Frontera de saldo: saldo = 99.99, monto = 100.00 -> rechazada."""
        resultado = validar_compra(edad=21, cuenta_activa=True, saldo=99.99, monto=100.0)
        self.assertEqual(resultado, "Compra rechazada")


if __name__ == "__main__":
    unittest.main(verbosity=2)
