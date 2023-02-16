import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Frame, Canvas, Scrollbar, Button
import pandas as pd
import numpy as np

def open_file():
    filepath = filedialog.askopenfilename()
    global byte_array
    with open(filepath, "rb") as f:
        byte_array = f.read()
    if len(byte_array) > (0xEBC0B+17):
        if byte_array[0xEBC0B] == 89 and byte_array[0xEBC0C] == 86: # 89 to ASCII dla Y, 86 to ASCII dla V
            print("Plik jest prawidłowy")
            vin_string = byte_array[0xEBC0B:0xEBC0B+17].decode()
            print(f'Numer VIN: {vin_string}')
            messagebox.showinfo("FILE OK", vin_string)
            create_gui()
        else:  
            messagebox.showerror("Wrong File!")
            return
    else:
            messagebox.showerror("Wrong File!")
            return        

    create_gui()

def create_gui():
    root = tk.Tk()   
    
    root.title("File Analyzer   VIN: ")
    root.config(width=600, height=400)
    open_file_button = tk.Button(root, text="Open File", command=open_file)
    open_file_button.grid(row=0, column=1, sticky="w")
    
    global byte_array
    vin = byte_array[0xEBC0B:0xEBC0B+17].decode()
    save_button = tk.Button(root, text= "Save:  " + vin, command=lambda: save_options(selected_options))
    save_button.grid(row=0, column=0, sticky="w")
    excel_file = pd.read_excel("CarConfig.xlsx")
    excel_file = excel_file[excel_file["Text Data"] != "Undefined value"]
    excel_file = excel_file[excel_file["Text Data"] != "Parameter error"]

    excel_file["value"] = excel_file["value"].apply(lambda x: str(x)[2:])

    ids = excel_file["id"].unique()
    selected_options = {}

    canvas = tk.Canvas(root)
    #canvas.config(scrollregion=canvas.bbox("all") )
    canvas.config(width=600, height=400)
    canvas.config(scrollregion=(0,0,600,15000))
    #canvas.grid(row=0, column=0)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)
   
    canvas.grid(row=1, column=0, sticky="w")    
    
    
    

    column_count=0
    frame_count = 0
    frame_row_count = 0
    frame_column_count = 0
    idx = 0
    row_value = 0
    for idx in ids:
        frame = tk.Frame(canvas, borderwidth=1,)
        canvas.create_window((0, frame_count*150), window=frame, anchor="nw")        
        frame.grid(row=frame_row_count, column=frame_column_count, sticky="nw")

        parameter_label = tk.Label(frame,  bg="gray", text = excel_file[excel_file['id'] == idx]['Parameter name'].values[0])
        parameter_label.grid(row=0, column=0, pady=10)
        options = excel_file[excel_file["id"] == idx]["Text Data"].unique()
        selected_options[idx] = tk.StringVar(value=options[0])
        #buffer_value = buffer[idx - 331676]
        #selected_options[idx].set(excel_file[(excel_file['id'] == idx) & (excel_file['value'].eq(buffer_value))]['Text Data'].values[0] if excel_file[(excel_file['id'] == idx) & (excel_file['value'] == buffer_value)]['Text Data'].values.any() else 'N/A')
        
        buffer_address = hex(965890 + (idx-331676))
        buffer_raw = (byte_array[965890 + (idx-331676)])
        buffer_value = buffer_raw
        row_no = excel_file[excel_file["id"] == idx]                   
        row_value = row_no["value"] # pobieramy wartość z param_df
        
        
        if type(row_no["value"]) == str:  # jeśli wartość jest stringiem, to konwertujemy ją na int
            row_value = int(row_no["value"], 16)
        else:
            row_value = row_no["value"]
        
       
        #selected_options[idx].set(excel_file[(excel_file['id'] == idx) & (excel_file['value'].eq(buffer_value))]['Text Data'].values[0] if excel_file[(excel_file['id'] == idx) & (excel_file['value'] == buffer_value)]['Text Data'].values.any() else 'N/A')
        print(buffer_address, buffer_value, row_value )
        row_count = 1
        for option in options:
            radio_button = tk.Radiobutton(frame, text=option, variable=selected_options[idx], value=option, )
            radio_button.grid(row=row_count, column=column_count, padx=10,sticky="nw" )
            row_count += 1
            
        frame_count += 1
        frame_column_count += 1
       
        #print("column count:", frame_column_count)
        if frame_column_count == 4:
            frame_column_count=0
            frame_row_count += 1


    
    root.mainloop()

        
            

def save_options(options):

#code to save the selected options

    pass
def option_changed(idx):

#   code to handle when a user changes the selected option for a given ID
    pass
open_file()



















