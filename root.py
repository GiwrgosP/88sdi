import tkinter as tk
import is

class window(tk.Tk):
      def __init__(self):
            self.path = os.path.dirname(os.path.abspath(__file__))
#search for database, excel, word files
            self.createWindow()

      def createWindow(self):
        self.window = tk.Tk()
        self.window.title("Temp name")
        self.window.geometry("1024x512")



def main():
    root = window()

main()
