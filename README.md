

**Estudiante:** Anderson Joel Pilachanga Caguana 



Primera etapa de transición de `restaurante_app` de una aplicación de
consola hacia una aplicación con **interfaz gráfica de usuario (GUI)**
construida con **Tkinter**. Siguiendo el mismo criterio de organización
del proyecto docente *Biblioteca App*, esta versión trabaja con una base
simplificada: únicamente los modelos `Producto` y `Usuario`.

La aplicación presenta primero una pantalla de acceso simulada
(`LoginView`). Con credenciales válidas, el usuario ingresa al panel
principal (`MainView`), donde puede consultar los productos y usuarios
cargados desde archivos JSON. La opción de **Ventas** se muestra en el
panel principal como funcionalidad pendiente, ya que se incorporará
gráficamente en semanas posteriores. Las demás funcionalidades
desarrolladas en la versión de consola (registro de productos, bebidas,
ventas con control de stock, etc.) se recuperarán progresivamente sobre
esta misma base gráfica.

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Responsabilidad de cada componente

| Componente | Responsabilidad |
|---|---|
| `modelos/producto.py` | Representa un producto (`codigo`, `nombre`, `categoria`, `precio`, `stock`) y su conversión desde diccionario. |
| `modelos/usuario.py` | Representa un usuario del sistema (`identificacion`, `nombre`, `nombre_usuario`, `contrasena`) usado para la simulación de acceso. |
| `servicios/archivo_servicio.py` | Única responsabilidad: leer `productos.json` y `usuarios.json` y convertirlos en listas de objetos, con manejo de excepciones. |
| `servicios/restaurante_servicio.py` | Recibe los datos cargados por `ArchivoServicio` y expone las operaciones que necesita la interfaz: validar acceso, listar usuarios, listar productos y consultar la cantidad (stock) de un producto. |
| `ui/login_view.py` | Pantalla de acceso: campos de usuario y contraseña, mensaje de error visual y botón de ingreso. Llama a `RestauranteServicio.validar_acceso()`, nunca lee los JSON directamente. |
| `ui/main_view.py` | Panel principal: botones para ver Productos, Usuarios y Ventas (pendiente), una lista donde se muestra la información y el botón de cerrar sesión. Llama a `RestauranteServicio` para obtener los datos a mostrar. |
| `main.py` | Crea la única ventana de Tkinter, instancia `RestauranteServicio`, crea `LoginView` y `MainView` sobre un mismo contenedor, y controla el cambio entre ambas vistas. |

## Flujo de la aplicación

```
Inicio de la aplicación
        ↓
main.py prepara Tkinter y RestauranteServicio
        ↓
LoginView (primera pantalla mostrada)
        ↓
Ingreso de usuario y contraseña
        ↓
RestauranteServicio.validar_acceso()
        ↓
   ¿Credenciales válidas?
   ├── No → mensaje de error, permanece en LoginView
   └── Sí → MainView
                ↓
        Productos | Usuarios | Ventas (pendiente)
                ↓
        Cerrar sesión → vuelve a LoginView
```

`LoginView` y `MainView` son dos `Frame` colocados sobre el mismo
contenedor dentro de la única ventana (`tk.Tk`) creada en `main.py`. El
cambio entre pantallas se realiza con `tkraise()`, sin abrir ventanas
nuevas ni crear más de un ciclo `mainloop()`.

## Simulación de acceso

El acceso se valida contra los usuarios cargados desde `usuarios.json`,
comparando `nombre_usuario` y `contrasena`. No se implementa
autenticación real (sin cifrado ni base de datos), ya que corresponde a
los fundamentos de la Semana 13 y no a un sistema de seguridad.

Usuarios de prueba incluidos en `datos/usuarios.json`:

| Usuario | Contraseña |
|---|---|
| `daniel` | `1234` |
| `dareck` | `1234` |
| `ariel` | `1234` |

## Manejo de excepciones

`ArchivoServicio` controla explícitamente:

- **FileNotFoundError**: si `productos.json` o `usuarios.json` no
  existen, se informa por consola y se continúa con una lista vacía.
- **json.JSONDecodeError**: si el archivo tiene contenido inválido, se
  informa por consola y se continúa con una lista vacía.
- **PermissionError**: si no hay permisos de lectura, se informa por
  consola sin detener la aplicación.
- **KeyError**: si un registro del JSON no tiene una clave esperada, ese
  registro se omite y se informa cuál clave falta.

## Cómo ejecutar el programa

1. Tener **Python 3** con Tkinter disponible (viene incluido en la
   instalación estándar de Python en Windows y macOS; en Linux puede
   requerir instalar el paquete `python3-tk`).
2. Ubicarse dentro de la carpeta `restaurante_app/`:
   ```bash
   cd restaurante_app
   ```
3. Ejecutar:
   ```bash
   python3 main.py
   ```
4. En la pantalla de acceso, ingresar un usuario y contraseña válidos
   (ver tabla anterior).
5. En el panel principal, usar los botones **Productos** y **Usuarios**
   para consultar la información cargada, o **Cerrar sesión** para
   volver a la pantalla de acceso.

## Comprobación de funcionamiento realizada

1. Se ejecutó `main.py` y la aplicación inició sin errores, mostrando
   primero `LoginView`.
2. Se verificó que los campos de usuario y contraseña permiten escribir.
3. Se probó dejar campos vacíos → apareció el mensaje "Ingrese usuario y
   contraseña." sin avanzar de pantalla.
4. Se probó una contraseña incorrecta → apareció el mensaje
   "Credenciales incorrectas." sin avanzar de pantalla.
5. Se ingresaron las credenciales válidas `daniel` / `1234` → la
   aplicación mostró `MainView`.
6. Se presionó **Productos** → se mostraron los cinco productos cargados
   desde `productos.json` (incluyendo Arroz marinero y Rodajas de
   sandía), con su stock.
7. Se presionó **Usuarios** → se mostraron los tres usuarios cargados
   desde `usuarios.json` (Daniel, Dareck y Ariel).
8. Se validó, revisando el código de las vistas, que `LoginView` y
   `MainView` obtienen la información únicamente a través de
   `RestauranteServicio` (`validar_acceso()`, `listar_productos()`,
   `listar_usuarios()`) y no leen los archivos JSON directamente.
9. Se presionó **Cerrar sesión** → la aplicación regresó a `LoginView`
   dentro de la misma ventana, con los campos de acceso limpios.
10. Se validó, sin la interfaz gráfica, el comportamiento de
    `RestauranteServicio` (listar productos, listar usuarios, acceso
    válido/ inválido y consulta de cantidad de un producto existente e
    inexistente), confirmando que la lógica de negocio funciona
    independientemente de la vista.

 
