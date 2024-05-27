# python3
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import textwrap
# imput parameters
def convert_data(input_file, output_file, header, fasta_width):
    try:
        # main
        df = pd.read_csv(input_file,header=None)
        sangerseq = ''.join(df.values.tolist()[0])
        # export to fasta
        with open(output_file, "w") as f:
            f.write(f'>{header}\n{textwrap.fill(sangerseq, width=fasta_width)}\n')

        messagebox.showinfo("Data conversion finished", "The FASTA sequence is saved to {}".format(output_file))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_input_file():
    try:
        input_file = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        entry_input_file.delete(0, tk.END)
        entry_input_file.insert(0, input_file)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_output_file():
    try:
        output_file = filedialog.asksaveasfilename(defaultextension=".fasta", filetypes=[("FASTA files", "*.fasta")])
        entry_output_file.delete(0, tk.END)
        entry_output_file.insert(0, output_file)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_analysis():
    try:
        input_file = entry_input_file.get()
        output_file = entry_output_file.get()
        header = str(entry_header.get())
        fasta_width = fasta_width_var.get()

        if not input_file:
            raise ValueError("Please select input file.")
        if not output_file:
            raise ValueError("Please select output file.")
        if header == "":
            raise ValueError("Please insert FASTA header.")
        convert_data(input_file, output_file, header, fasta_width)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI
root = tk.Tk()
root.title("sangeranalyseR Consesus CSV to FASTA Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_input_file = tk.Label(frame, text="Input CSV File:")
label_input_file.grid(row=0, column=0, sticky="w")

entry_input_file = tk.Entry(frame, width=40)
entry_input_file.grid(row=0, column=1, padx=5, pady=5)

button_browse_input = tk.Button(frame, text="Browse", command=browse_input_file)
button_browse_input.grid(row=0, column=2, padx=5, pady=5)

label_output_file = tk.Label(frame, text="Output FASTA File:")
label_output_file.grid(row=1, column=0, sticky="w")

entry_output_file = tk.Entry(frame, width=40)
entry_output_file.grid(row=1, column=1, padx=5, pady=5)

button_browse_output = tk.Button(frame, text="Browse", command=browse_output_file)
button_browse_output.grid(row=1, column=2, padx=5, pady=5)

label_header = tk.Label(frame, text="FASTA Header:")
label_header.grid(row=2, column=0, sticky="w")

entry_header = tk.Entry(frame, width=100)
entry_header.grid(row=2, column=1, padx=5, pady=5)

fasta_width = tk.Label(frame, text="FASTA width:")
fasta_width.grid(row=3, column=0, sticky="w")

fasta_width_var = tk.IntVar()
fasta_width_var.set(60)  # Default selection
fasta_width_options = [60,70,80,100,120]
fasta_width_menu = tk.OptionMenu(frame, fasta_width_var, *fasta_width_options)
fasta_width_menu.grid(row=3, column=1, padx=5, pady=5)

button_run = tk.Button(frame, text="Convert Data", command=run_analysis)
button_run.grid(row=4, column=1, pady=10)

root.mainloop()
