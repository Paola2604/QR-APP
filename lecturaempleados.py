import os
import sys
from PyQt5.QtWidgets import QApplication
import datetime



from tkinter import messagebox
def lectura():
    with open("novedad.txt","r",encoding="utf-8") as empleado:
        linea=empleado.readline()
        
        if linea!="":
            lista1=linea.strip().split(",")
            
            dni1=lista1[2]
            fecha1=lista1[4]
            print(dni1)
            
    app = QApplication(sys.argv)
    with open("maestroempleados.txt","r",encoding="utf-8") as empleados:
        linea1=empleados.readline()
        while linea1!="":
            lista2=linea1.strip().split(",")
            dni2=lista2[2]
            if dni1==dni2:
                nombre=lista2[0]
        
                    
                fecha1=str(fecha1)
                fecha_actual = datetime.date.today()
                fecha_actual_str = fecha_actual.strftime("%d/%m/%y")
                print("fecha actual "+fecha_actual_str)
                print(fecha1)
                if fecha_actual_str != fecha1:
                    messagebox.showinfo("Bienvenido/a","Bienvenido/a " + nombre +" lamento informarle que\nla fecha de su turno es el día "+fecha1 )
                    return(0)
                    sys.exit(app.exec_())
                    break
                
                messagebox.showinfo("Bienvenido/a","Bienvenido/a " + nombre + " aguarde y será atentido" )
                return(0)
                sys.exit(app.exec_())
                break
            linea1=empleados.readline()
        else:
            messagebox.showinfo("usuario inexistente")
        


