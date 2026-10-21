# Escenarios BDD con Sintaxis Gherkin

**Asignatura:** Testing & Quality Assurance (TQA)  
**Evaluación:** Examen Práctico Hito 3  
**Actividad:** 05 · Actividad Adicional - BDD / Gherkin  
**Aplicación:** SauceDemo (`https://www.saucedemo.com/`)  

---

## Introducción
Gherkin es un lenguaje estructurado en lenguaje natural que permite describir el comportamiento esperado de una funcionalidad mediante el enfoque BDD (*Behavior-Driven Development*), facilitando la comunicación entre el equipo de desarrollo, QA y el negocio.

A continuación se definen los escenarios solicitados (exitoso y alternativo/error) cumpliendo con la estructura estándar: `Feature`, `Scenario`, `Given`, `When`, `Then`, `And`, `But`.

---

## Funcionalidad 1: Autenticación de Usuarios

```gherkin
# language: es
Característica: Inicio de sesión en SauceDemo
  Como usuario de la tienda virtual Swag Labs (SauceDemo)
  Quiero autenticarme con mis credenciales
  Para poder acceder al catálogo de productos y realizar compras

  Antecedentes:
    Dado que el usuario se encuentra en la página de login "https://www.saucedemo.com/"

  @exitoso @smoke
  Escenario: Acceso exitoso con credenciales válidas
    Cuando el usuario ingresa el nombre de usuario "standard_user"
    Y el usuario ingresa la contraseña "secret_sauce"
    Y hace clic en el botón "Login"
    Entonces el usuario debería ser redirigido a la página de inventario "/inventory.html"
    Y debería visualizarse el título "Products" en el encabezado
    Y el ícono del carrito de compras debería estar visible

  @error @seguridad
  Escenario: Intento de acceso con usuario bloqueado
    Cuando el usuario ingresa el nombre de usuario "locked_out_user"
    Y el usuario ingresa la contraseña "secret_sauce"
    Y hace clic en el botón "Login"
    Entonces el usuario debería permanecer en la página de login
    Y debería mostrarse el mensaje de error "Epic sadface: Sorry, this user has been locked out."
    Pero no debería tener acceso a la vista de productos

  @error @validacion
  Escenario: Intento de acceso con contraseña incorrecta
    Cuando el usuario ingresa el nombre de usuario "standard_user"
    Y el usuario ingresa la contraseña "clave_invalida_123"
    Y hace clic en el botón "Login"
    Entonces el sistema debe impedir el acceso
    Y debe mostrar el mensaje de error "Epic sadface: Username and password do not match any user in this service"
```

---

## Funcionalidad 2: Carrito de Compras y Checkout

```gherkin
# language: es
Característica: Flujo de Compra y Carrito en SauceDemo
  Como cliente autenticado
  Quiero agregar artículos a mi carrito de compras
  Para proceder con la orden de compra

  Antecedentes:
    Dado que el usuario ha iniciado sesión como "standard_user"
    Y se encuentra en el catálogo de productos

  @exitoso @carrito
  Escenario: Agregar un producto al carrito de compras
    Cuando el usuario hace clic en el botón "Add to cart" del producto "Sauce Labs Backpack"
    Entonces el botón del producto debe cambiar su estado a "Remove"
    Y la insignia del carrito de compras debe mostrar el número "1"

  @error @checkout
  Escenario: Intento de continuar el checkout sin ingresar datos obligatorios
    Dado que el usuario tiene productos en el carrito y está en la página de checkout "/checkout-step-one.html"
    Cuando deja vacíos los campos "First Name", "Last Name" y "Zip/Postal Code"
    Y hace clic en el botón "Continue"
    Entonces el sistema debe impedir avanzar al resumen del pedido
    Y debe mostrarse el mensaje de advertencia "Error: First Name is required"
```

---

## Formato en Inglés Estándar (Cucumber / Behave Compatible)

```gherkin
Feature: User Authentication on SauceDemo

  Scenario: Successful login with standard user
    Given the user is on the SauceDemo login page
    When the user enters username "standard_user" and password "secret_sauce"
    And clicks the login button
    Then the user should be redirected to the product inventory page
    And the product catalog should be displayed

  Scenario: Failed login with locked out user
    Given the user is on the SauceDemo login page
    When the user enters username "locked_out_user" and password "secret_sauce"
    And clicks the login button
    Then the user should see an error message "Epic sadface: Sorry, this user has been locked out."
    And the user should remain on the login page
```
