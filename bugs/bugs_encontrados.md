# Registro de Defectos y Reporte de Bugs

**Asignatura:** Testing & Quality Assurance (TQA)  
**Evaluación:** Examen Práctico Hito 3  
**Actividad:** 06 · Registro de Defectos  
**Aplicación:** SauceDemo (`https://www.saucedemo.com/`)  

---

## 1. Lineamientos para el Reporte de Defectos (Slide 11)
* **Si la prueba pasa:** Registra `Passed` en el caso de prueba correspondiente. *No se debe inventar un bug si el sistema se comporta según la especificación.*
* **Si la prueba falla o se detecta un comportamiento anómalo:** Registra lo observado y documenta el defecto de forma **reproducible**, adjuntando la captura de evidencia correspondiente en `evidencias/capturas/`.

---

## 2. Resumen de Defectos Registrados

| ID Defecto | Título Descriptivo | Severidad | Prioridad | Caso Asociado | Estado |
|---|---|:---:|:---:|:---:|:---:|
| `BUG-01` | *[Título breve del defecto]* | Alta / Media / Baja | P1 / P2 / P3 | TC-CN-XX | Abierto / En Revisión |
| `BUG-02` | *[Título breve del defecto]* | Alta / Media / Baja | P1 / P2 / P3 | TC-CN-XX | Abierto / En Revisión |

---

## 3. Plantilla de Reporte de Defecto

*(Duplica esta plantilla por cada bug reproducible que encuentres durante tus pruebas)*

### Reporte de Defecto: BUG-01
* **ID:** `BUG-01`
* **Título Descriptivo:** *[Ejemplo: Error al renderizar imágenes de productos con problem_user / Imposibilidad de remover producto]*
* **Severidad:** `[ Crítica | Alta | Media | Baja ]`
  * *Crítica:* Bloquea el flujo principal sin alternativa.
  * *Alta:* Afecta una funcionalidad clave.
  * *Media:* Comportamiento anómalo pero existe alternativa de uso.
  * *Baja:* Detalle cosmético o visual.
* **Prioridad:** `[ P1 (Urgente) | P2 (Alta) | P3 (Normal) | P4 (Baja) ]`
* **Entorno de Pruebas:**
  * **URL:** `https://www.saucedemo.com/`
  * **Navegador:** Chrome / Firefox / Edge (versión)
  * **Sistema Operativo:** Windows 10/11
* **Precondiciones:**
  1. *[Estado inicial necesario]*
* **Datos de Prueba:**
  * Usuario: *[Ej: problem_user / standard_user]*
  * Contraseña: `secret_sauce`
* **Pasos para Reproducir el Defecto (Step-by-Step):**
  1. *Paso 1...*
  2. *Paso 2...*
  3. *Paso 3...*
* **Resultado Esperado:**
  * *[Lo que el sistema debería hacer según la especificación]*
* **Resultado Actual / Obtenido:**
  * *[Lo que realmente ocurrió y el comportamiento erróneo observado]*
* **Evidencia (Captura / Log):**
  * `evidencias/capturas/BUG-01.png`
* **Notas Adicionales:**
  * *[Información relevante, consola del navegador, etc.]*

---

> [!TIP]
> **Usuarios con defectos conocidos en SauceDemo para pruebas adicionales:**
> SauceDemo incluye usuarios intencionales para entrenamiento de QA:
> * `problem_user`: Produce imágenes rotas en el catálogo e impide editar el campo 'Last Name' en el checkout.
> * `error_user`: Falla con mensaje de error inesperado al hacer clic en 'Finish' en el checkout.
> * `visual_user`: Presenta fallos de alineación visual y botones desfasados en la interfaz.
> Si deseas documentar bugs adicionales reales de la plataforma de prueba, puedes reproducirlos con dichos perfiles.
