import tkinter as tk
from tkinter import messagebox

class ErrorPopup:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        messagebox.showerror("Error", self.mensaje)

class CustomErrorPopup(ErrorPopup):
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def mostrar(self):
        messagebox.showerror("Error Personalizado", f"Ocurrió un error:\n{self.mensaje}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  


    popup = CustomErrorPopup("Este es un mensaje de error de prueba.")
    popup.mostrar()

    root.mainloop()
