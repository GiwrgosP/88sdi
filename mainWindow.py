import tkinter as tk

class mainWindow(tk.Tk):

    def __init__(self,master,path):
        self.window = tk.Tk()
        self.window.title("Υπηρεσίες Στρατιωτών")
        self.window.geometry("2048x1024")

        self.window.mainloop()
