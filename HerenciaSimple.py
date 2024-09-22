import tkinter as tk
from tkinter import messagebox

class PopupBase:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        messagebox.showinfo("Información", self.mensaje)

class CustomPopup(PopupBase):
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def mostrar(self):
        messagebox.showinfo("Mensaje Personalizado", f"Este es un mensaje especial:\n{self.mensaje}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()


    popup = CustomPopup("Hola, este es un mensaje de prueba.")
    popup.mostrar()

    root.mainloop()
