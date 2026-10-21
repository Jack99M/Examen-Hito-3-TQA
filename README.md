# Examen Práctico - Hito 3 | Testing & Quality Assurance (TQA)

Repositorio individual para el desarrollo y entrega del Examen Práctico del Hito 3 en la materia **Testing & Quality Assurance**.

---

## 1. Propósito del Proyecto y Aplicación Bajo Prueba

Este proyecto consolida la aplicación práctica de metodologías y técnicas de aseguramiento de calidad de software:
* **Pruebas Funcionales de Caja Negra** sobre una aplicación web real de demostración.
* **Análisis Estructural de Caja Blanca** sobre código Python (cálculo de complejidad ciclomática, identificación de condiciones y cobertura de sentencias/decisiones).
* **Especificación BDD con Gherkin** para documentación de comportamiento.
* **Gestión de Defectos (Bugs)** y control de versiones profesional con **Git, GitHub y GitHub Projects**.

### Aplicación Bajo Prueba (AUT)
* **Plataforma:** [SauceDemo (Swag Labs)](https://www.saucedemo.com/)
* **URL:** `https://www.saucedemo.com/`
* **Credenciales de prueba base:**
  * Usuario estándar: `standard_user`
  * Contraseña: `secret_sauce`

---

## 2. Estructura del Repositorio

El proyecto sigue rigurosamente la arquitectura de carpetas y nomenclatura recomendada en la diapositiva 13, integrando además el código fuente y las pruebas unitarias automatizadas:

```text
Examen-Hito-3-TQA/
├── .gitignore                      # Exclusión de archivos temporales y cachés
├── README.md                       # Documentación general del proyecto y guía de entrega
├── src/                            # Código fuente bajo prueba (Caja Blanca)
│   ├── __init__.py
│   └── validar_compra.py          # Implementación de la función a analizar
├── tests/                          # Suite de pruebas unitarias automatizadas
│   ├── __init__.py
│   └── test_caja_blanca.py        # Pruebas de caja blanca (unittest / pytest)
├── docs/                           # Documentación de casos de prueba y análisis
│   ├── casos_caja_negra.md        # 5 casos funcionales diseñados para SauceDemo
│   ├── analisis_caja_blanca.md    # Análisis de código, decisiones, CFG y cobertura
│   └── escenarios_gherkin.md      # Escenarios BDD Given / When / Then
├── bugs/                           # Registro y seguimiento de anomalías encontradas
│   └── bugs_encontrados.md        # Plantilla y formato de reporte de defectos
├── evidencias/                     # Evidencias gráficas de la ejecución
│   └── capturas/                  # Capturas de pantalla (TC-CN-XX.png, BUG-XX.png)
└── entregable/                     # Documentación final de entrega
    └── informe_hito3.pdf          # Informe consolidado final en formato PDF
```

---

## 3. Código Fuente y Ejecución de Pruebas Unitarias

La función bajo análisis estructural [`src/validar_compra.py`](src/validar_compra.py) valida compras con base en edad, estado de cuenta, saldo y monto:

```python
def validar_compra(edad, cuenta_activa, saldo, monto):
    if edad < 18:
        return "Compra no permitida: edad"
    if not cuenta_activa:
        return "Compra no permitida: cuenta"
    if saldo >= monto and monto > 0:
        return "Compra aprobada"
    return "Compra rechazada"
```

### Ejecutar las Pruebas de Caja Blanca
Las pruebas unitarias están implementadas con la biblioteca estándar `unittest` de Python (no requiere instalaciones adicionales):

```bash
# Ejecutar todas las pruebas unitarias con reporte detallado
python -m unittest tests/test_caja_blanca.py -v
```

Si dispones de `pytest`:
```bash
pytest -v
```

---

## 4. Resumen de Actividades del Examen

| Módulo | Documento / Ruta | Descripción |
|---|---|---|
| **03 · Caja Negra** | [`docs/casos_caja_negra.md`](docs/casos_caja_negra.md) | 5 casos funcionales (Login, Bloqueo, Carrito, Eliminar, Validaciones). |
| **04 · Caja Blanca** | [`docs/analisis_caja_blanca.md`](docs/analisis_caja_blanca.md) | Análisis de decisiones/condiciones, CFG, cobertura y los 3 casos solicitados. |
| **05 · Gherkin BDD** | [`docs/escenarios_gherkin.md`](docs/escenarios_gherkin.md) | Escenarios Given / When / Then (caminos exitoso y alternativo). |
| **06 · Reporte de Bugs**| [`bugs/bugs_encontrados.md`](bugs/bugs_encontrados.md) | Plantilla estandarizada de defectos reproducibles con evidencia. |
| **08 · Entregable** | [`entregable/informe_hito3.pdf`](entregable/) | Informe consolidado final. |

---

## 5. Gestión del Proyecto con GitHub (Slide 14)

### Tablero de Tareas sugerido (GitHub Projects)
Organiza tus tareas en el board de GitHub con las columnas `To Do`, `In Progress`, `In Review` y `Done`:

- [ ] **Diseñar casos:** Redactar los 5 casos de caja negra en `docs/casos_caja_negra.md`.
- [ ] **Analizar código:** Realizar el análisis de decisiones, grafo y cobertura en `docs/analisis_caja_blanca.md`.
- [ ] **Redactar Gherkin:** Escribir los escenarios en `docs/escenarios_gherkin.md`.
- [ ] **Ejecutar pruebas:** Ejecutar los 5 casos en SauceDemo.
- [ ] **Registrar resultados:** Marcar `Passed` o `Failed` y completar resultados obtenidos.
- [ ] **Documentar bugs:** Registrar en `bugs/bugs_encontrados.md` cualquier defecto encontrado.
- [ ] **Revisar evidencias:** Guardar las capturas en `evidencias/capturas/`.
- [ ] **Revisar informe:** Consolidar resultados y conclusiones.
- [ ] **Preparar PDF:** Generar `entregable/informe_hito3.pdf`.
- [ ] **Actualizar README:** Revisar datos finales antes de la entrega.

---

## 6. Comandos Git para Subir el Repositorio a GitHub

Una vez que hayas creado tu repositorio vacío en GitHub (por ejemplo, con el nombre `Examen-Hito-3-TQA`), ejecuta los siguientes comandos desde la terminal en esta carpeta:

```bash
# 1. Inicializar el repositorio Git local
git init -b main

# 2. Agregar todos los archivos preparados
git add .

# 3. Realizar el commit inicial
git commit -m "feat: estructura inicial completa del examen practico hito 3"

# 4. Vincular el repositorio remoto de GitHub
git remote add origin https://github.com/Jack99M/Examen-Hito-3-TQA.git

# 5. Subir los cambios a la rama principal
git push -u origin main
```

> [!IMPORTANT]
> Recuerda invitar al docente como colaborador en GitHub utilizando el correo institucional indicado en clase (con los permisos requeridos).
