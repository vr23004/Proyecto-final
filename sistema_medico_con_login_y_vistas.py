import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

def guardar_csv(nombre_archivo, datos, encabezado):
    existe = os.path.exists(nombre_archivo)
    with open(nombre_archivo, 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        if not existe:
            writer.writerow(encabezado)
        writer.writerow(datos)

def mostrar_registros(archivo, titulo):
    if not os.path.exists(archivo):
        messagebox.showerror("Error", f"No existe el archivo {archivo}")
        return

    ventana = tk.Toplevel()
    ventana.title(titulo)
    tabla = ttk.Treeview(ventana)
    tabla.pack(fill="both", expand=True)

    with open(archivo, newline='') as f:
        reader = csv.reader(f)
        columnas = next(reader)
        tabla["columns"] = columnas
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=100)
        for fila in reader:
            tabla.insert("", "end", values=fila)

def ventana_registrar_paciente():
    ventana = tk.Toplevel()
    ventana.title("Registrar Paciente")

    tk.Label(ventana, text="ID").pack()
    id_entry = tk.Entry(ventana)
    id_entry.pack()

    tk.Label(ventana, text="Nombre").pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    tk.Label(ventana, text="Edad").pack()
    edad_entry = tk.Entry(ventana)
    edad_entry.pack()

    tk.Label(ventana, text="Género").pack()
    genero_entry = tk.Entry(ventana)
    genero_entry.pack()

    def guardar():
        datos = [id_entry.get(), nombre_entry.get(), edad_entry.get(), genero_entry.get()]
        guardar_csv("pacientes.csv", datos, ['ID', 'Nombre', 'Edad', 'Género'])
        messagebox.showinfo("Registro", "✅ Paciente registrado correctamente")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).pack()

def ventana_registrar_medico():
    ventana = tk.Toplevel()
    ventana.title("Registrar Médico")

    tk.Label(ventana, text="ID").pack()
    id_entry = tk.Entry(ventana)
    id_entry.pack()

    tk.Label(ventana, text="Nombre").pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    tk.Label(ventana, text="Especialidad").pack()
    especialidad_entry = tk.Entry(ventana)
    especialidad_entry.pack()

    def guardar():
        datos = [id_entry.get(), nombre_entry.get(), especialidad_entry.get()]
        guardar_csv("medicos.csv", datos, ['ID', 'Nombre', 'Especialidad'])
        messagebox.showinfo("Registro", "✅ Médico registrado correctamente")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).pack()

def ventana_agendar_cita():
    ventana = tk.Toplevel()
    ventana.title("Agendar Cita")

    tk.Label(ventana, text="ID Cita").pack()
    id_cita = tk.Entry(ventana)
    id_cita.pack()

    tk.Label(ventana, text="ID Paciente").pack()
    id_paciente = tk.Entry(ventana)
    id_paciente.pack()

    tk.Label(ventana, text="ID Médico").pack()
    id_medico = tk.Entry(ventana)
    id_medico.pack()

    tk.Label(ventana, text="Fecha (YYYY-MM-DD)").pack()
    fecha = tk.Entry(ventana)
    fecha.pack()

    tk.Label(ventana, text="Hora (HH:MM)").pack()
    hora = tk.Entry(ventana)
    hora.pack()

    def guardar():
        datos = [id_cita.get(), id_paciente.get(), id_medico.get(), fecha.get(), hora.get()]
        guardar_csv("citas.csv", datos, ['ID Cita', 'ID Paciente', 'ID Médico', 'Fecha', 'Hora'])
        messagebox.showinfo("Registro", "✅ Cita agendada correctamente")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).pack()

def ventana_agregar_historial():
    ventana = tk.Toplevel()
    ventana.title("Agregar Historial Clínico")

    tk.Label(ventana, text="ID Paciente").pack()
    id_paciente = tk.Entry(ventana)
    id_paciente.pack()

    tk.Label(ventana, text="Nota Clínica").pack()
    nota = tk.Entry(ventana)
    nota.pack()

    def guardar():
        datos = [id_paciente.get(), nota.get()]
        guardar_csv("historial.csv", datos, ['ID Paciente', 'Nota Clínica'])
        messagebox.showinfo("Registro", "📝 Historial guardado correctamente")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).pack()

def mostrar_sistema():
    ventana = tk.Tk()
    ventana.title("Sistema de Consultas Médicas")
    ventana.geometry("400x500")

    tk.Label(ventana, text="Sistema de Gestión Médica", font=("Arial", 16)).pack(pady=10)

    tk.Button(ventana, text="Registrar Paciente", width=35, command=ventana_registrar_paciente).pack(pady=5)
    tk.Button(ventana, text="Registrar Médico", width=35, command=ventana_registrar_medico).pack(pady=5)
    tk.Button(ventana, text="Agendar Cita", width=35, command=ventana_agendar_cita).pack(pady=5)
    tk.Button(ventana, text="Agregar Historial Clínico", width=35, command=ventana_agregar_historial).pack(pady=5)

    # Botones para ver registros
    tk.Label(ventana, text="📂 Ver Registros", font=("Arial", 12)).pack(pady=10)
    tk.Button(ventana, text="Ver Pacientes", width=35, command=lambda: mostrar_registros("pacientes.csv", "Pacientes")).pack(pady=2)
    tk.Button(ventana, text="Ver Médicos", width=35, command=lambda: mostrar_registros("medicos.csv", "Médicos")).pack(pady=2)
    tk.Button(ventana, text="Ver Citas", width=35, command=lambda: mostrar_registros("citas.csv", "Citas")).pack(pady=2)
    tk.Button(ventana, text="Ver Historial", width=35, command=lambda: mostrar_registros("historial.csv", "Historial Clínico")).pack(pady=2)

    ventana.mainloop()

def verificar_login(usuario, contrasena):
    if not os.path.exists("usuarios.csv"):
        with open("usuarios.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['usuario', 'contrasena'])
            writer.writerow(['admin', '1234'])
    with open("usuarios.csv", "r") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila['usuario'] == usuario and fila['contrasena'] == contrasena:
                return True
    return False

def login():
    ventana_login = tk.Tk()
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry("300x200")

    tk.Label(ventana_login, text="Usuario:").pack()
    usuario_entry = tk.Entry(ventana_login)
    usuario_entry.pack()

    tk.Label(ventana_login, text="Contraseña:").pack()
    contrasena_entry = tk.Entry(ventana_login, show="*")
    contrasena_entry.pack()

    def iniciar():
        user = usuario_entry.get()
        pwd = contrasena_entry.get()
        if verificar_login(user, pwd):
            messagebox.showinfo("Acceso", "✅ Acceso concedido")
            ventana_login.destroy()
            mostrar_sistema()
        else:
            messagebox.showerror("Error", "❌ Usuario o contraseña incorrectos")

    tk.Button(ventana_login, text="Iniciar sesión", command=iniciar).pack(pady=10)

    ventana_login.mainloop()

# Iniciar sistema
login()
