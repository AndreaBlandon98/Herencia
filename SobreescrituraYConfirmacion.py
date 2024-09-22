import tkinter as tk
from tkinter import messagebox


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")


        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        respuesta = messagebox.askyesno("Cerrar", "¿Desea cerrar la ventana?")
        if respuesta:
            self.root.destroy()


class CustomWindow(MainWindow):
    def on_close(self):
        respuesta = messagebox.askquestion("Confirmación", "¿Está seguro que desea salir?")
        if respuesta == 'yes':
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    ventana = CustomWindow(root)
    root.mainloop()
