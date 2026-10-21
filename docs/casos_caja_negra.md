# Casos de Prueba de Caja Negra: SauceDemo

**Asignatura:** Testing & Quality Assurance (TQA)  
**Evaluación:** Examen Práctico Hito 3  
**Actividad:** 03 · Caja Negra  
**Aplicación Bajo Prueba (AUT):** [SauceDemo (Swag Labs)](https://www.saucedemo.com/)  

---

## Resumen de Casos Diseñados

| ID | Título del Caso | Funcionalidad | Usuario / Datos | Estado |
|---|---|---|---|:---:|
| **TC-CN-01** | Inicio de sesión exitoso con credenciales válidas | Autenticación | `standard_user` / `secret_sauce` | *[Por ejecutar]* |
| **TC-CN-02** | Inicio de sesión bloqueado con usuario inhabilitado | Autenticación | `locked_out_user` / `secret_sauce` | *[Por ejecutar]* |
| **TC-CN-03** | Agregar producto al carrito y verificar insignia | Catálogo y Carrito | `Sauce Labs Backpack` | *[Por ejecutar]* |
| **TC-CN-04** | Eliminar producto desde la página del carrito | Gestión de Carrito | `Sauce Labs Backpack` | *[Por ejecutar]* |
| **TC-CN-05** | Validación de campos obligatorios en el Checkout | Checkout / Formularios | Formulario vacío (First Name) | *[Por ejecutar]* |

---

### Caso de Prueba 1: TC-CN-01
* **ID:** `TC-CN-01`
* **Título:** Inicio de sesión exitoso con credenciales válidas
* **Objetivo:** Verificar que un usuario con credenciales correctas pueda autenticarse y ser redirigido al catálogo de productos.
* **Precondiciones:**
  1. Navegador web abierto con conexión a Internet.
  2. Página de login accesible en `https://www.saucedemo.com/`.
  3. No haber sesión iniciada previamente.
* **Datos de prueba:**
  * Usuario: `standard_user`
  * Contraseña: `secret_sauce`
* **Pasos de ejecución:**
  1. Ingresar a `https://www.saucedemo.com/`.
  2. En el campo de texto `Username`, escribir `standard_user`.
  3. En el campo de texto `Password`, escribir `secret_sauce`.
  4. Hacer clic en el botón `Login`.
* **Resultado esperado:**
  * El sistema autentica correctamente al usuario.
  * Se redirige a la URL `https://www.saucedemo.com/inventory.html`.
  * Se visualiza el catálogo de productos con el título "Products" y el ícono del carrito.
* **Resultado obtenido:**  
  *(Completar al ejecutar: p. ej., "El usuario ingresó exitosamente al catálogo de productos inventory.html")*
* **Estado:** `[ Passed / Failed ]`
* **Evidencia:**  
  `evidencias/capturas/TC-CN-01.png`

---

### Caso de Prueba 2: TC-CN-02
* **ID:** `TC-CN-02`
* **Título:** Bloqueo de acceso al intentar iniciar sesión con usuario inhabilitado
* **Objetivo:** Verificar que el sistema impida el acceso y muestre un mensaje de error adecuado cuando se intenta acceder con un usuario bloqueado.
* **Precondiciones:**
  1. Página de login abierta en `https://www.saucedemo.com/`.
* **Datos de prueba:**
  * Usuario: `locked_out_user`
  * Contraseña: `secret_sauce`
* **Pasos de ejecución:**
  1. Ingresar a `https://www.saucedemo.com/`.
  2. En el campo `Username`, escribir `locked_out_user`.
  3. En el campo `Password`, escribir `secret_sauce`.
  4. Hacer clic en el botón `Login`.
* **Resultado esperado:**
  * El sistema no permite el ingreso a la aplicación.
  * Permanece en la página de inicio.
  * Se despliega un contenedor de error en color rojo con el texto:  
    `Epic sadface: Sorry, this user has been locked out.`
* **Resultado obtenido:**  
  *(Completar al ejecutar)*
* **Estado:** `[ Passed / Failed ]`
* **Evidencia:**  
  `evidencias/capturas/TC-CN-02.png`

---

### Caso de Prueba 3: TC-CN-03
* **ID:** `TC-CN-03`
* **Título:** Agregar producto al carrito y verificar actualización del contador
* **Objetivo:** Confirmar que al presionar el botón "Add to cart" de un producto, este se añade y el badge numérico del carrito refleja el incremento.
* **Precondiciones:**
  1. Sesión iniciada con `standard_user`.
  2. Estar situado en el catálogo (`inventory.html`).
  3. Carrito de compras inicialmente vacío (sin badge numérico).
* **Datos de prueba:**
  * Producto: `Sauce Labs Backpack` ($29.99)
* **Pasos de ejecución:**
  1. Localizar el artículo `Sauce Labs Backpack` en el catálogo.
  2. Hacer clic en el botón `Add to cart` asociado al producto.
* **Resultado esperado:**
  * El botón cambia su texto a `Remove`.
  * El ícono del carrito en la esquina superior derecha muestra una insignia con el número `1`.
* **Resultado obtenido:**  
  *(Completar al ejecutar)*
* **Estado:** `[ Passed / Failed ]`
* **Evidencia:**  
  `evidencias/capturas/TC-CN-03.png`

---

### Caso de Prueba 4: TC-CN-04
* **ID:** `TC-CN-04`
* **Título:** Eliminar un producto desde la vista detallada del carrito de compras
* **Objetivo:** Verificar que el usuario pueda remover un artículo directamente desde la vista del carrito y el contador se actualice en consecuencia.
* **Precondiciones:**
  1. Sesión iniciada con `standard_user`.
  2. Carrito con al menos un artículo agregado (`Sauce Labs Backpack`).
* **Datos de prueba:**
  * Producto a eliminar: `Sauce Labs Backpack`
* **Pasos de ejecución:**
  1. Hacer clic sobre el ícono del carrito de compras para navegar a `https://www.saucedemo.com/cart.html`.
  2. Verificar que el producto `Sauce Labs Backpack` esté listado.
  3. Hacer clic en el botón `Remove` del producto.
* **Resultado esperado:**
  * El elemento desaparece de la lista del carrito.
  * La insignia numérica del carrito desaparece (o queda en 0 items).
* **Resultado obtenido:**  
  *(Completar al ejecutar)*
* **Estado:** `[ Passed / Failed ]`
* **Evidencia:**  
  `evidencias/capturas/TC-CN-04.png`

---

### Caso de Prueba 5: TC-CN-05
* **ID:** `TC-CN-05`
* **Título:** Validación de campos obligatorios en el formulario de información de Checkout
* **Objetivo:** Validar que el flujo de compra bloquee el avance si no se completan los campos obligatorios del comprador (nombre, apellido, código postal).
* **Precondiciones:**
  1. Sesión iniciada con `standard_user`.
  2. Al menos un producto agregado en el carrito.
  3. Estar en la página de información de Checkout: `https://www.saucedemo.com/checkout-step-one.html`.
* **Datos de prueba:**
  * First Name: `[vacío]`
  * Last Name: `[vacío]`
  * Postal Code: `[vacío]`
* **Pasos de ejecución:**
  1. Desde la página del carrito (`cart.html`), hacer clic en el botón `Checkout`.
  2. Dejar todos los campos del formulario (`First Name`, `Last Name`, `Zip/Postal Code`) en blanco.
  3. Hacer clic en el botón `Continue`.
* **Resultado esperado:**
  * El sistema impide avanzar a `checkout-step-two.html`.
  * Se muestran los campos resaltados con íconos de advertencia.
  * Se visualiza el mensaje de error:  
    `Error: First Name is required`
* **Resultado obtenido:**  
  *(Completar al ejecutar)*
* **Estado:** `[ Passed / Failed ]`
* **Evidencia:**  
  `evidencias/capturas/TC-CN-05.png`
