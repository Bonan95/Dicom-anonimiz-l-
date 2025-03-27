import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pydicom

def anonymize_dicom_file(input_file, output_file):
    # DICOM fájl beolvasása
    ds = pydicom.dcmread(input_file)
    
    # Private tag-ek eltávolítása
    ds.remove_private_tags()
    
    # Azok a tag-ek, melyeket anonimizálni szeretnénk
    tags_to_anonymize = [
        'PatientName',
        'PatientID',
        'PatientBirthDate',
        'PatientSex',
        'OtherPatientIDs',
        'OtherPatientNames',
        'PatientAddress',
        'PatientTelephoneNumbers',
        'StudyDate',
        'StudyTime',
        'AccessionNumber',
        'InstitutionName',
        'ReferringPhysicianName',
        # További tag-ek szükség szerint...
    ]
    
    # A megadott tag-ek módosítása
    for tag in tags_to_anonymize:
        if tag in ds:
            ds.data_element(tag).value = 'Anonymous'
    
    # Esetleg UID-k újragenerálása, ha szükséges:
    # ds.StudyInstanceUID = pydicom.uid.generate_uid()
    # ds.SeriesInstanceUID = pydicom.uid.generate_uid()
    
    # Anonimizált fájl mentése
    ds.save_as(output_file)

def process_files(input_files, output_folder):
    if not input_files:
        messagebox.showerror("Hiba", "Nincs kiválasztva bemeneti fájl!")
        return
    if not output_folder:
        messagebox.showerror("Hiba", "Nincs kiválasztva kimeneti mappa!")
        return

    error_files = []
    for file in input_files:
        try:
            basename = os.path.basename(file)
            output_file = os.path.join(output_folder, basename)
            anonymize_dicom_file(file, output_file)
        except Exception as e:
            error_files.append(file)
    
    if error_files:
        messagebox.showerror("Hiba", f"Az alábbi fájloknál hiba lépett fel:\n" + "\n".join(error_files))
    else:
        messagebox.showinfo("Siker", "Minden fájl sikeresen anonimizálva!")

def select_files():
    files = filedialog.askopenfilenames(
        title="Válassz DICOM fájlokat",
        filetypes=[("Minden fájl", "*.*")]
    )
    if files:
        global input_file_list, input_folder
        input_file_list = list(files)
        input_folder = ""  # Töröljük a mappa értékét, ha az előzőleg be volt állítva
        input_display.config(state='normal')
        input_display.delete(1.0, tk.END)
        input_display.insert(tk.END, "Kiválasztott fájlok:\n" + "\n".join(input_file_list))
        input_display.config(state='disabled')

def select_folder():
    folder = filedialog.askdirectory(title="Válassz mappát")
    if folder:
        global input_file_list, input_folder
        input_folder = folder
        # Most az összes fájlt érzékeli a mappában, függetlenül a kiterjesztéstől
        files = [os.path.join(folder, entry) for entry in os.listdir(folder)
                 if os.path.isfile(os.path.join(folder, entry))]
        input_file_list = files
        input_display.config(state='normal')
        input_display.delete(1.0, tk.END)
        input_display.insert(tk.END, f"Kiválasztott mappa: {folder}\n\nFájlok:\n" + "\n".join(input_file_list))
        input_display.config(state='disabled')

def select_output_folder():
    folder = filedialog.askdirectory(title="Válassz kimeneti mappát")
    if folder:
        global output_folder
        output_folder = folder
        output_entry.config(state='normal')
        output_entry.delete(0, tk.END)
        output_entry.insert(0, folder)
        output_entry.config(state='disabled')

def run_anonymization():
    global input_file_list, output_folder
    if not input_file_list:
        messagebox.showerror("Hiba", "Kérlek, válassz bemeneti fájlokat vagy mappát!")
        return
    if not output_folder:
        messagebox.showerror("Hiba", "Kérlek, válassz kimeneti mappát!")
        return
    process_files(input_file_list, output_folder)

# Tkinter GUI beállítása
root = tk.Tk()
root.title("DICOM Anonimizáló")

# Globális változók
input_file_list = []
input_folder = ""
output_folder = ""

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Bemeneti fájlok/mappa kijelzésére szolgáló szövegmező
input_label = tk.Label(frame, text="Bemeneti fájlok / mappa:")
input_label.grid(row=0, column=0, sticky="w")

input_display = tk.Text(frame, height=10, width=60, state='disabled')
input_display.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Gombok fájlok illetve mappa kiválasztásához
file_button = tk.Button(frame, text="Fájlok kiválasztása", command=select_files)
file_button.grid(row=2, column=0, padx=5, pady=5)

folder_button = tk.Button(frame, text="Mappa kiválasztása", command=select_folder)
folder_button.grid(row=2, column=1, padx=5, pady=5)

# Kimeneti mappa kiválasztása
output_label = tk.Label(frame, text="Kimeneti mappa:")
output_label.grid(row=3, column=0, sticky="w")
output_entry = tk.Entry(frame, width=50, state='disabled')
output_entry.grid(row=3, column=1, padx=5, pady=5)
output_button = tk.Button(frame, text="Kiválasztás", command=select_output_folder)
output_button.grid(row=3, column=2, padx=5, pady=5)

# Anonimizálás indítása
run_button = tk.Button(frame, text="Anonimizálás indítása", command=run_anonymization)
run_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
