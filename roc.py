import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

# *****************MODELO********************
operadores = []	# Lista de operadores - sin esto, no carga la lista de operadores

def agregar_operador_modelo(registro, nombre, categoria, direccion, telefono, email, fecha_alta, fecha_baja, situacion, comentarios):
    if registro and nombre and categoria and direccion and telefono and email and fecha_alta and situacion:
        operadores.append({
            "Registro": registro,
            "Nombre": nombre,
            "Categoría": categoria,
            "Dirección": direccion,
            "Teléfono": telefono,
            "Email": email,
            "Fecha Alta": fecha_alta,
            "Fecha Baja": fecha_baja,
            "Situación": situacion,
            "Comentarios": comentarios
        })
        return True
    else:
        return False

def eliminar_operador_modelo(indice):
    if 0 <= indice < len(operadores):
        operadores.pop(indice)
        return True
    return False

def actualizar_operador_modelo(indice, registro, nombre, categoria, direccion, telefono, email, fecha_alta, fecha_baja, situacion, comentarios):
    if 0 <= indice < len(operadores):
        operadores[indice] = {
            "Registro": registro,
            "Nombre": nombre,
            "Categoría": categoria,
            "Dirección": direccion,
            "Teléfono": telefono,
            "Email": email,
            "Fecha Alta": fecha_alta,
            "Fecha Baja": fecha_baja,
            "Situación": situacion,
            "Comentarios": comentarios
        }
        return True
    return False

# **********************CONTROLADOR******************************
def agregar_operador():
    registro = entry_registro.get()
    nombre = entry_nombre.get()
    categoria = combo_categoria.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    fecha_alta = entry_fecha_alta.get()
    fecha_baja = entry_fecha_baja.get()
    situacion = combo_situacion.get()
    comentarios = entry_comentarios.get()

    if agregar_operador_modelo(registro, nombre, categoria, direccion, telefono, email, fecha_alta, fecha_baja, situacion, comentarios):
        actualizar_lista()
        limpiar_campos()
        messagebox.showinfo("Éxito", "Operador agregado exitosamente")
    else:
        messagebox.showerror("Error", "Todos los campos requeridos deben ser llenados")

def eliminar_operador():
    seleccion = lista_operadores.selection()
    if seleccion:
        indice = int(lista_operadores.item(seleccion[0], "values")[0]) - 1
        if eliminar_operador_modelo(indice):
            actualizar_lista()
            limpiar_campos()
            messagebox.showinfo("Éxito", "Operador eliminado exitosamente")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el operador")
    else:
        messagebox.showerror("Error", "Seleccione un operador para eliminar")

def actualizar_operador():
    seleccion = lista_operadores.selection()
    if seleccion:
        indice = int(lista_operadores.item(seleccion[0], "values")[0]) - 1
        registro = entry_registro.get()
        nombre = entry_nombre.get()
        categoria = combo_categoria.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        fecha_alta = entry_fecha_alta.get()
        fecha_baja = entry_fecha_baja.get()
        situacion = combo_situacion.get()
        comentarios = entry_comentarios.get()

        if actualizar_operador_modelo(indice, registro, nombre, categoria, direccion, telefono, email, fecha_alta, fecha_baja, situacion, comentarios):
            actualizar_lista()
            limpiar_campos()
            messagebox.showinfo("Éxito", "Operador actualizado exitosamente")
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos")
    else:
        messagebox.showerror("Error", "Seleccione un operador para actualizar")

def seleccionar_operador(event):
    seleccion = lista_operadores.selection()
    if seleccion:
        indice = int(lista_operadores.item(seleccion[0], "values")[0]) - 1
        operador = operadores[indice]
        entry_registro.delete(0, tk.END)
        entry_registro.insert(0, operador["Registro"])
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, operador["Nombre"])
        combo_categoria.set(operador["Categoría"])
        entry_direccion.delete(0, tk.END)
        entry_direccion.insert(0, operador["Dirección"])
        entry_telefono.delete(0, tk.END)
        entry_telefono.insert(0, operador["Teléfono"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, operador["Email"])
        entry_fecha_alta.set_date(operador["Fecha Alta"])
        entry_fecha_baja.set_date(operador["Fecha Baja"])
        combo_situacion.set(operador["Situación"])
        entry_comentarios.delete(0, tk.END)
        entry_comentarios.insert(0, operador["Comentarios"])

# *********************************VISTA**************************************
def limpiar_campos():
    entry_registro.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    combo_categoria.set("")
    entry_direccion.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_fecha_alta.set_date("")  
    entry_fecha_baja.set_date("")  
    combo_situacion.set("")
    entry_comentarios.delete(0, tk.END)

def actualizar_lista():
    lista_operadores.delete(*lista_operadores.get_children())
    for idx, operador in enumerate(operadores):
        lista_operadores.insert("", "end", values=(
            idx + 1, operador["Registro"], operador["Nombre"], operador["Categoría"], operador["Dirección"], operador["Teléfono"],
            operador["Email"], operador["Fecha Alta"], operador["Fecha Baja"], operador["Situación"], operador["Comentarios"]
        ))

    
    lista_operadores.column("#", width=30)
    lista_operadores.column("Registro", width=80)
    lista_operadores.column("Nombre", width=120)
    lista_operadores.column("Categoría", width=80)
    lista_operadores.column("Dirección", width=150)
    lista_operadores.column("Teléfono", width=100)
    lista_operadores.column("Email", width=150)
    lista_operadores.column("Fecha Alta", width=80)
    lista_operadores.column("Fecha Baja", width=80)
    lista_operadores.column("Situación", width=100)
    lista_operadores.column("Comentarios", width=150)

# *********Salir de la aplicación*********
def salir(event):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Registro de Operadores de Cambio")

# Establecer color de fondo y tamaño de ventana
root.configure(bg="lightblue") # Color de fondo
root.geometry("1200x700")  # Ancho x Alto 

# Asignar la tecla 'ESC' para salir
root.bind('<Escape>', salir) # Salir con la tecla 'ESC'

# Configurar el diseño de la grilla con 3 columnas para el formulario
frame_formulario = tk.Frame(root, bg="lightblue")
frame_formulario.pack(pady=10) # Espacio entre los elementos

# Primera columna
tk.Label(frame_formulario, text="Registro", bg="lightblue").grid(row=0, column=0, padx=10, pady=5)
entry_registro = tk.Entry(frame_formulario)
entry_registro.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_formulario, text="Nombre", bg="lightblue").grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(frame_formulario)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_formulario, text="Categoría", bg="lightblue").grid(row=2, column=0, padx=10, pady=5)
combo_categoria = ttk.Combobox(frame_formulario, values=["Casa", "Agencia"])
combo_categoria.grid(row=2, column=1, padx=10, pady=5)

# Segunda columna
tk.Label(frame_formulario, text="Dirección", bg="lightblue").grid(row=0, column=2, padx=10, pady=5)
entry_direccion = tk.Entry(frame_formulario)
entry_direccion.grid(row=0, column=3, padx=10, pady=5)

tk.Label(frame_formulario, text="Teléfono", bg="lightblue").grid(row=1, column=2, padx=10, pady=5)
entry_telefono = tk.Entry(frame_formulario)
entry_telefono.grid(row=1, column=3, padx=10, pady=5)

tk.Label(frame_formulario, text="Email", bg="lightblue").grid(row=2, column=2, padx=10, pady=5)
entry_email = tk.Entry(frame_formulario)
entry_email.grid(row=2, column=3, padx=10, pady=5)

# Tercera columna
tk.Label(frame_formulario, text="Fecha Alta", bg="lightblue").grid(row=0, column=4, padx=10, pady=5)
entry_fecha_alta = DateEntry(frame_formulario, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha_alta.grid(row=0, column=5, padx=10, pady=5)

tk.Label(frame_formulario, text="Fecha Baja", bg="lightblue").grid(row=1, column=4, padx=10, pady=5)
entry_fecha_baja = DateEntry(frame_formulario, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha_baja.grid(row=1, column=5, padx=10, pady=5)

tk.Label(frame_formulario, text="Situación", bg="lightblue").grid(row=2, column=4, padx=10, pady=5)
combo_situacion = ttk.Combobox(frame_formulario, values=["Activa", "Suspendida", "Revocada", "Baja"])
combo_situacion.grid(row=2, column=5, padx=10, pady=5)

# Comentarios sobre cada operador
tk.Label(frame_formulario, text="Comentarios", bg="lightblue").grid(row=3, column=0, padx=10, pady=5)
entry_comentarios = tk.Entry(frame_formulario)
entry_comentarios.grid(row=3, column=1, columnspan=5, padx=10, pady=5, sticky="ew")

# Botones para las operaciones CRUD
frame_botones = tk.Frame(root, bg="lightblue")
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_operador)
btn_agregar.grid(row=0, column=0, padx=10)

btn_actualizar = tk.Button(frame_botones, text="Actualizar", command=actualizar_operador)
btn_actualizar.grid(row=0, column=1, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_operador)
btn_eliminar.grid(row=0, column=2, padx=10)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_campos)
btn_limpiar.grid(row=0, column=3, padx=10)

# Lista de operadores (Tabla)
frame_lista = tk.Frame(root, bg="lightblue")
frame_lista.pack(pady=20)

columnas = ("#", "Registro", "Nombre", "Categoría", "Dirección", "Teléfono", "Email", "Fecha Alta", "Fecha Baja", "Situación", "Comentarios")
lista_operadores = ttk.Treeview(frame_lista, columns=columnas, show="headings")
for col in columnas:
    lista_operadores.heading(col, text=col)

# Ajuste del ancho de las columnas para que todas se vean
lista_operadores.column("#", width=30)
lista_operadores.column("Registro", width=80)
lista_operadores.column("Nombre", width=120)
lista_operadores.column("Categoría", width=80)
lista_operadores.column("Dirección", width=150)
lista_operadores.column("Teléfono", width=100)
lista_operadores.column("Email", width=150)
lista_operadores.column("Fecha Alta", width=80)
lista_operadores.column("Fecha Baja", width=80)
lista_operadores.column("Situación", width=100)
lista_operadores.column("Comentarios", width=150)

lista_operadores.pack()

lista_operadores.bind("<<TreeviewSelect>>", seleccionar_operador)

# ***************Inicio de la aplicación***********************
root.mainloop()
