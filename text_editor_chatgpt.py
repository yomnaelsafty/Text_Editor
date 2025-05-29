import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor with Buttons")
        self.root.geometry("800x600")

        # Create a frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=0, column=0, sticky="ew")

        # Open Button
        open_button = tk.Button(button_frame, text="Open", command=self.open_file, width=10)
        open_button.grid(row=0, column=0, padx=5, pady=5)

        # Save Button
        save_button = tk.Button(button_frame, text="Save", command=self.save_file, width=10)
        save_button.grid(row=0, column=1, padx=5, pady=5)

        # Text Area
        self.text_area = tk.Text(self.root, font=("Arial", 14))
        self.text_area.grid(row=1, column=0, sticky="nsew")

        # Make the text area expand
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def open_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            self.root.title(f"Simple Text Editor - {filepath}")

    def save_file(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Saved", f"File saved successfully: {filepath}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
