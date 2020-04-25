import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import os

import mainWindow

class window(tk.Tk):

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.programFiles = {"database" : "\\88sdi.db",\
                            "mainWindowScript" : "\\mainWindow.py"}
        self.createRootWindow()

    def __del__(self):
        self.window.destroy()
        print("ending root")

    def createRootWindow(self):
        self.window = tk.Tk()
        self.window.title("Υπηρεσίες Στρατιωτών")
        self.window.geometry("256x128")

        self.rootFrame = tk.Frame(self.window)

        self.checkFilesLoadingBar = ttk.Progressbar(self.rootFrame, orient = "horizontal", length = 100, mode = "determinate")
        self.checkFilesLoadingBar.pack()

        self.checkFilesLoadingBarProgress = 100 / len(self.programFiles)

        self.checkFilesLabel = tk.Label(self.rootFrame)
        self.checkFilesLabel.pack()

        self.checkFiles()

        if self.flagCheckFiles:
            mainWindow.mainWindow(self,self.path)

        self.window.mainloop()




    def checkFiles(self):

        self.flagCheckFiles = True
        for file in self.programFiles:

            self.checkFilesLabel.text = file
            self.checkFilesLoadingBar["value"] = self.checkFilesLoadingBar["value"] + self.checkFilesLoadingBarProgress
            self.rootFrame.update_idletasks()
            if os.path.isfile(self.path + self.programFiles[file]):
                pass
            else:
                errorMessageBox = messagebox.showerror("Error will initiating files", "Could not find " + file)
                self.flagCheckFiles = False
