import shutil
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def move_file(src, dest, ending):
    try:
        #check wenn wir hier sind ist alles super!
        files = [ os.path.join(src, f) for f in os.listdir(src) if os.path.isfile(os.path.join(src, f)) and f.endswith(ending)]
        
        if not files:
            messagebox.showerror(title="Fehler", message="Keine Dateien in dem Verzeichnis vorhanden!")
            return
        
        for f in files:
            shutil.move(f, dest)
        messagebox.showinfo(title="Verschieben einer Datei", message="Verschieben der Datei hat funktioniert!")
    except Exception as e:
        messagebox.showerror(title="Fehler", message="Das Verschieben ist fehlgeschlagen")
        
def delete_download_path():
    try:
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        download_files = [ os.path.join(download_path, f) for f in os.listdir(download_path)]
        for file_path in download_files:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        messagebox.showinfo("Erfolg", "Alle Dateien im Downloads-Ordner wurden gelöscht.")
    except Exception as e:
        messagebox.showinfo("Error", f"Fehler beim Löschen { e }")
                    
def openSourceFile():
    source = filedialog.askdirectory(title="Directory")
    return source

def openDestinationPath():
    destination = filedialog.askdirectory(title="Directory auswählen!")
    return destination
def on_select():
    selected_option = option.get()
    
    if selected_option == 1:
        source_path = openSourceFile()
        destination = openDestinationPath()
        move_file(source_path, destination, '.exe')
    else:
        delete_download_path()
     
if __name__ == "__main__":  
    root = tk.Tk()
    root.title("Dateimanager")
    option = tk.IntVar()
    tk.Radiobutton(root, text="Files verschieben", variable=option, value=1).pack(anchor='w')
    tk.Radiobutton(root, text="Download Ordner leeren", variable=option, value=2).pack(anchor='w')
    tk.Button(root, text="Ausführen", command=on_select).pack()

        
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')


    root.resizable(False, False)
    
    root.mainloop()
    

   
   

    