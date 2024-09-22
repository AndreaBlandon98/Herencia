import tkinter as tk
from tkinter import messagebox

class InfoPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        messagebox.showinfo("Información", self.mensaje)

class ErrorPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        messagebox.showerror("Error", self.mensaje)

class CustomPopup(InfoPopup, ErrorPopup):
    def __init__(self, mensaje_info, mensaje_error):
        InfoPopup.__init__(self, mensaje_info)
        ErrorPopup.__init__(self, mensaje_error)

    def mostrar_combined(self):
        InfoPopup.mostrar(self)
        ErrorPopup.mostrar(self)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()


    popup = CustomPopup("Este es un mensaje informativo.", "¡Atención! Ocurrió un error.")
    popup.mostrar_combined()  

    root.mainloop()
