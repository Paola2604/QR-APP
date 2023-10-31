def seleccionar_fecha():
    fecha_seleccionada = cal.get_date()
    label_fecha.config(text="Fecha seleccionada: " + fecha_seleccionada)
import tkinter as tk
from tkcalendar import Calendar

# Crea una ventana
ventana = tk.Tk()
ventana.title("Calendario de selección de fecha")

# Crea un widget Calendar
cal = Calendar(ventana, selectmode="day", year=2023, month=10, day=15)
cal.pack(pady=20)

# Crea un botón para mostrar la fecha seleccionada
boton = tk.Button(ventana, text="Seleccionar fecha", command=seleccionar_fecha)
boton.pack()

# Crea una etiqueta para mostrar la fecha seleccionada
label_fecha = tk.Label(ventana, text="")
label_fecha.pack()

ventana.mainloop()