import tkinter as tk
from tkinter import messagebox

class InfoPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        messagebox.showinfo("Información", self.mensaje)

class WarningPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        messagebox.showwarning("Advertencia", self.mensaje)

class CombinedPopup(InfoPopup, WarningPopup):
    def __init__(self, mensaje_info, mensaje_advertencia):
        InfoPopup.__init__(self, mensaje_info)
        WarningPopup.__init__(self, mensaje_advertencia)

    def mostrar_combined(self):
        self.mostrar()
        WarningPopup.mostrar(self)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()


    popup = CombinedPopup("Este es un mensaje informativo.", "¡Atención! Este es un mensaje de advertencia.")
    popup.mostrar_combined()  # Muestra ambos mensajes

    root.mainloop()
