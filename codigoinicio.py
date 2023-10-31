
import tkinter as tk
from tkinter import*
from tkinter import Button
from QRlector import lector
import codigoprincipalQR
import lecturaempleados 

colorLabel = "#000000"
letra = "#0F1B07"


class VentanaPrincipal:
    
    def __init__(self, root):
        self.root = root
        self.root.title("miTurno")
        self.root.geometry("400x200")
        root.config(bg="#C6D166")
        root.iconbitmap('./icono.ico')
        # Crear un marco para los botones
        frame = tk.Frame(root)
        frame.pack(expand=True)
        frame.config(bg="#C6D166")
        
        # Botón para "Pedir turno"
        label1 = Label(frame, text="Bienvenido, seleccione la acción que desea realizar:")
        label1.pack(pady=20)
        label1.config(bg="#C6D166", fg=letra)
        boton_pedir_turno = Button(frame, text="Solicitar turno", command=self.llamar_codigoprincipalQR,bg="#5C821A", fg="#FFFFFF")
        boton_pedir_turno.pack(pady=20)

        # Botón para "Ya tengo un turno"
        boton_tengo_turno = Button(frame, text="Ya tengo un turno", command=self.llamar_QRlector,bg="#5C821A", fg="#FFFFFF")
        boton_tengo_turno.pack(pady=20)

    def llamar_codigoprincipalQR(self):
        self.root.destroy()
        codigoprincipalQR.principal()
        root = tk.Tk()
        
        ventana = VentanaPrincipal(root)
        root.mainloop()
        
        
        

    def llamar_QRlector(self):
            self.root.destroy()
            lect=lector()
            if lect==0:
                    root = tk.Tk()
                    ventana = VentanaPrincipal(root)
                    root.mainloop()
            
            
        


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0,0)
    ventana = VentanaPrincipal(root)
    root.mainloop()
