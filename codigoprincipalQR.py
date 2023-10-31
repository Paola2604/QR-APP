import smtplib
from tkinter import *
from tkcalendar import Calendar
colorframe = "#C6D166"
colorLabel = "#C6D166"
colorrooot = "#000000"
letra = "#0F1B07"
botonFondo = "#5C821A"
labelfecha="#FFFFFF"
from tkinter import messagebox
import generadorQR
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from PIL import Image, ImageTk 
from tkinter.ttk import Combobox
fecha_seleccionada_label = None  # Variable global para almacenar la etiqueta de la fecha seleccionada

class fecha:

        def seleccionar_fecha():
            global fecha_seleccionada_label  # Declarar como global la variable
            root2 = Toplevel()
            root2.title("Seleccionar Fecha")
            root2.iconbitmap('icono.ico')
            root2.config(bg=colorframe)
            def obtener_fecha():
                fecha_seleccionada = cal.get_date()
                fecha_seleccionada_label.config(text=f"fecha:{fecha_seleccionada}")
                print("Fecha seleccionada:", fecha_seleccionada)
                root2.destroy()
    
            cal = Calendar(root2, selectmode="day", year=23, month=10, day=15, date_pattern="dd/mm/y")
            cal.pack(padx=20, pady=30)
    
            boton = Button(root2, text="Aceptar", command=obtener_fecha,widt=20,bg=botonFondo,fg="white")
            boton.pack(pady=10)

def principal():
        fecha()
    
        def enviar_correo(nombre2, mail2):
            try:
                # Configurar el servidor SMTP
                servidor_smtp = "smtp.gmail.com"
                puerto_smtp = 587
                correo_emisor = "pythonprueba8@gmail.com"
                contrasena = "xwjyfuijtuwiudns"
                servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
                servidor.starttls()
                servidor.login(correo_emisor, contrasena)
                mensaje = MIMEMultipart()
                mensaje["From"] = correo_emisor
                mensaje["To"] = mail2
                mensaje["Subject"] = "QR generado"
                mensaje_texto = "Tu QR ha sido generado con éxito."
                mensaje.attach(MIMEText(mensaje_texto, "plain"))
                archivo_imagen = nombre2 + ".png"
                with open(archivo_imagen, "rb") as imagen:
                    imagen_adjunta = MIMEImage(imagen.read())
                    imagen_adjunta.add_header("Content-Disposition", f"attachment; filename= {archivo_imagen}")
                    mensaje.attach(imagen_adjunta)
                servidor.sendmail(correo_emisor, mail2, mensaje.as_string())
                servidor.quit()
    
                if os.path.exists(archivo_imagen):
                    os.remove(archivo_imagen)
                    print(f"El archivo {archivo_imagen} ha sido eliminado después de enviarlo por correo.")
                else:
                    print(f"El archivo {archivo_imagen} no existe o ya ha sido eliminado.")
            except Exception as e:
                print("Error", f"Error al enviar el correo electrónico: {str(e)}")

    
        def fcaca():
            global fecha_seleccionada_label
            fecha = fecha_seleccionada_label.cget("text").split(":")[1]  #fecha de la etiqueta
            print(fecha)
            nombre1 = nombre.get()
            apellido1 = apellido.get()
            dni1 = dni.get()
            mail1 = mail.get()
            combobo = combobox.get()
            print("combobox", combobo)
            if (nombre1 and apellido1 and dni1 and mail1 and fecha != ""):
                with open("maestroempleados.txt", "a", encoding="utf-8") as empleados:
                    contenido = f"{nombre1},{apellido1},{dni1},{mail1},{fecha},{combobo}\n"
                    empleados.write(contenido)
                    generadorQR.generarQR(contenido, nombre1)

                enviar_correo(nombre1, mail1)

                limpiar()

                return messagebox.showinfo("Aviso", "Felicitaciones!!\nSu código QR ha sido enviado al correo indicado!!")

            else:
                 messagebox.showwarning("Advertencia", "Los campos son obligatorios")


        def limpiar():
            nombre.set("")
            apellido.set("")
            dni.set("")
            mail.set("")

        root = Tk()
        root.title("Solicitud turno")
        root.iconbitmap('icono.ico')
        root.config(bg=colorframe)
        root.resizable(0,0)
        # Configura el tamaño deseado
        ancho_ventana = 800
        alto_ventana = 400

        # Creamos el primer Frame con un fondo azul
        frame1 = Frame(root, bg=colorframe, width=ancho_ventana // 2.5, height=alto_ventana)
        frame1.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")  # Columna 0

        # Hacer que el Frame1 se expanda para llenar el espacio disponible


        # Creamos el segundo Frame con un fondo rojo
        frame2 = Frame(root, bg=colorframe, width=ancho_ventana // 1, height=alto_ventana)
        frame2.grid(row=0, column=1, padx=0, pady=5,sticky="nsew")  # Columna 1

        # Centra los Frames en la ventana principal

        frame2.grid_columnconfigure(0, weight=1)

        # Cargar una imagen
        imagen = Image.open("icono.ico")  # Reemplaza "ruta_de_la_imagen.png" con la ubicación de tu imagen
        imagen = imagen.resize((200, 200))  # Ajusta el tamaño de la imagen si es necesario

        imagen_tk = ImageTk.PhotoImage(imagen)
        label_imagen = Label(frame1, image=imagen_tk, bg=colorframe)
        label_imagen.image = imagen_tk  # Evita que la imagen sea recolectada por el recolector de basura
        nombre = StringVar()
        apellido = StringVar()
        dni = StringVar()
        mail = StringVar()
        # Centra la imagen en el Frame
        label_imagen.pack(pady=(alto_ventana - 300) / 2)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        labeltitulo=Label(frame2, text="Solicitar nuevo turno",font=('arial',18))
        labeltitulo.grid(pady=10,row=0,column=0,sticky="w")
        labeltitulo.config(bg=colorframe)
        label1=Label(frame2, text="Nombre:",font=('arial',14))
        label1.grid(padx=0, pady=0, row=2, column=0, sticky="w")
        label1.config(bg=colorLabel, fg=letra)
        entry1 = Entry(frame2, textvariable=nombre,bg=labelfecha,width=50)
        entry1.grid(padx=0, pady=0, row=3, column=0,sticky="w")
        label2 = Label(frame2, text="Apellido:",font=('arial',14))
        label2.grid(padx=0, pady=0, row=4, column=0, sticky="w")
        label2.config(bg=colorLabel, fg=letra)
        entry2 = Entry(frame2, textvariable=apellido,bg=labelfecha,width=50)
        entry2.grid(padx=0, pady=0, row=5, column=0,sticky="w")
        label3 = Label(frame2, text="DNI:",font=('arial',14))
        label3.grid(padx=0, pady=0, row=6, column=0, sticky="w")
        label3.config(bg=colorLabel, fg=letra)
        entry3 = Entry(frame2, textvariable=dni,bg=labelfecha,width=50)
        entry3.grid(padx=0, pady=0, row=7, column=0,sticky="w")
        label4 = Label(frame2, text="e-mail:",font=('arial',14))
        label4.grid(padx=0, pady=0, row=8, column=0, sticky="w")

        entry4 = Entry(frame2, textvariable=mail,bg=labelfecha,width=50)
        entry4.grid(padx=0, pady=0, row=9, column=0,sticky="w")
        label4.config(bg=colorLabel, fg=letra)



        frame3=Frame(frame2,bg=colorframe)
        frame3.grid(row=10, column=0, padx=0, pady=5,sticky="nsew")
        labelcbo = Label(frame3, text="Seleccione motivo:",font=('arial',14))
        labelcbo.grid(padx=0, pady=0, row=0, column=0, sticky="w")
        labelcbo.config(bg=colorLabel, fg=letra)
        elementos = ['Consultas','Reclamos','Trámites','Tesoreria','otros...']  # Lista del 1 al 10
        combobox = Combobox(frame3, values=elementos, width=8,font=('arial',12))
        combobox.set(elementos)  # primer elemento como predeterminados
        combobox.grid(padx=0, pady=0, row=0, column=1,sticky="w")
        global fecha_seleccionada_label  #  variable
        fecha_seleccionada_label = Label(frame3, text="",bg=labelfecha,fg=letra,border=2,width=14,font=('arial',12))
        fecha_seleccionada_label.grid(row=1, column=1,sticky="w")

        boton_fecha = Button(frame3, text="Seleccionar Fecha", width=14, command=fecha.seleccionar_fecha)
        boton_fecha.grid(padx=0, pady=14, row=1, column=0)
        boton_fecha.config(bg=botonFondo, fg="#FFFFFF")

        boton3 = Button(frame3, text="Obtener turno", width=14,command=lambda: (fcaca(), root.destroy()))
        boton3.grid(padx=0, pady=14, row=2, column=0,columnspan=6)
        boton3.config(bg=botonFondo,fg="#FFFFFF")

        root.geometry("600x230")
        root.geometry(f"{ancho_ventana}x{alto_ventana}")
        root.mainloop()

if __name__ == "__main__":
            principal()
