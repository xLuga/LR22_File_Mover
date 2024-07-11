import shutil
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def move_file(src, dest, ending):
    try:
        #checken ob grundsätzlich das Destinationsfile existiert.
        if os.path.isdir(dest):
            print("Dictionary ist vorhanden!")
        else:
            os.makedirs(dest)
            print("Neuer Ordner wurde erstellt!")
        
        #check wenn wir hier sind ist alles super!
        files = [ os.path.join(src, f) for f in os.listdir(src) if os.path.isfile(os.path.join(src, f)) and f.endswith(ending)]
        for f in files:
            shutil.move(f, dest)
        messagebox.showinfo(title="Verschieben einer Datei", message="Verschieben der Datei hat funktioniert!")
    except Exception as e:
        messagebox.showerror(title="Verschieben einer Datei", message="Das Verschieben ist fehlgeschlagen")
        
def openSourceFile():
    source = filedialog.askdirectory(title="Directory")
    return source

def openDestinationPath():
    destination = filedialog.askdirectory(title="Directory auswählen!")
    return destination
    
if __name__ == "__main__":  
    root = tk.Tk()
    root.withdraw()
    file_endings = input("Welchen Dateityp möchtest du moven: ")
    
    
    source_path = openSourceFile()
    destination = openDestinationPath()
    move_file(source_path, destination, file_endings)
   
   

    