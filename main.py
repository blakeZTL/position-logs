import os
import pdfplumber
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser

class PositionLogExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("Position Log Extractor")
        self.root.geometry("400x200")
        
        self.label = tk.Label(root, text="Select PDF Files", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Select PDFs", command=self.select_files)
        self.select_button.pack(pady=5)
        
        self.extract_button = tk.Button(root, text="Extract", command=self.extract_data, state=tk.DISABLED)
        self.extract_button.pack(pady=5)
        
        self.pdf_paths = []

    def select_files(self):
        self.pdf_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
        if self.pdf_paths:
            self.label.config(text=f"Selected {len(self.pdf_paths)} files")
            self.extract_button.config(state=tk.NORMAL)
    
    def extract_data(self):
        if not self.pdf_paths:
            messagebox.showerror("Error", "Please select PDF files first.")
            return
        
        all_distinct_initials = set()
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        
        for pdf_path in self.pdf_paths:
            data = []
            date = None
            
            with pdfplumber.open(pdf_path) as pdf:
                should_log_data = False
                should_get_date = False
                for page in pdf.pages:
                    tables = page.extract_tables()
                    for table in tables:
                        for row in table:
                            if row[0] == "(1) FACILITY ID" and date is None:
                                should_get_date = True
                                continue
                            if should_get_date:
                                date = row[6].replace("/", "-")
                                should_get_date = False
                                continue
                            if row[0] == "(5)\nTIME ON":
                                should_log_data = True
                                continue
                            if should_log_data:
                                time_on = row[0]
                                initials = row[2]
                                time_off = row[3]
                                data.append([time_on, initials, time_off])
            
            df = pd.DataFrame(data, columns=["TIME ON", "INITIALS", "TIME OFF"])
            df = df.dropna()
            df = df[df["INITIALS"] != ""]
            
            all_distinct_initials.update(df["INITIALS"].unique())
        
        output_file = os.path.join(downloads_path, f"Distinct_Initials_Combined_{date}.csv")
        
        init_df = pd.DataFrame(list(all_distinct_initials), columns=["Initials"])
        init_df = init_df.sort_values("Initials")
        init_df.to_csv(output_file, index=False, header=False)
        
        messagebox.showinfo("Success", "Distinct initials saved!\nClick OK to open the file.")
        webbrowser.open(f"file://{output_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PositionLogExtractor(root)
    root.mainloop()