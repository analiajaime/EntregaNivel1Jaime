# Registro de Operadores de Cambio

Esta es una aplicación de escritorio simple, construida con **Python** y **Tkinter**, que permite gestionar un registro de operadores de cambio. La aplicación soporta operaciones básicas de **CRUD** (Crear, Leer, Actualizar y Eliminar) sobre los registros de los operadores.

## Características

- **Agregar Operadores:** Puedes agregar un nuevo operador ingresando los datos solicitados en el formulario.
- **Visualización de Operadores:** Los operadores agregados se visualizan en una tabla con todos los campos.
- **Actualizar Operadores:** Puedes seleccionar un operador en la tabla y actualizar su información.
- **Eliminar Operadores:** Permite eliminar un operador seleccionado de la tabla.
- **Limpieza Automática:** Los campos del formulario se limpian automáticamente después de agregar o modificar un registro.
- **Salir de la Aplicación:** Puedes cerrar la aplicación presionando la tecla `ESC`.

## Campos del Formulario

El formulario permite ingresar los siguientes datos para cada operador:

- **Registro** (ID único)
- **Nombre**
- **Categoría** (Casa / Agencia)
- **Dirección**
- **Teléfono**
- **Email**
- **Fecha Alta** (Fecha en la que se dio de alta al operador)
- **Fecha Baja** (Fecha en la que se dio de baja al operador, si aplica)
- **Situación** (Activa, Suspendida, Revocada, Baja)
- **Comentarios** (Cualquier observación adicional)

## Requisitos

- Python 3.x
- Módulo **Tkinter** (viene preinstalado con Python)
- Módulo **tkcalendar** (instalable con `pip`)

