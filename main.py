from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from window import AppWindow
from dataAccess import DBClient





funclib = {
    "create": DBClient.Create,
    "read": DBClient.Read,
    "update": DBClient.Update,
    "delete": DBClient.Delete
}



def main():

    root = tk.Tk();
    AppWindow(root, process_function=funclib);

    root.mainloop();

if __name__ == "__main__":
    main();
