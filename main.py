import tkinter as tk
import PyPDF2
from tkinter.filedialog import askopenfile

from PIL import Image, ImageTk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.Image = logo
logo_label.grid(column=1, row=0)

# Label
instructions = tk.Label(root, text="Click the browse button to extract from PDF", font="Arial")
instructions.grid(columnspan=3, row=1, column=0)


def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a file", filetypes=[('PDF File', '*.pdf')])
    if file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        page = pdf_reader.getPage(0)
        page_content = page.extractText()

        pdf_textbox = tk.Text(root, height = 10, width = 50, padx = 20, pady = 20)
        pdf_textbox.insert(1.0, page_content)
        pdf_textbox.tag_configure("center", justify= "center")
        pdf_textbox.tag_add("center", 1.0, "end")
        pdf_textbox.grid(column = 1, row= 3)
        browse_text.set("Browse")


# Browse Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Arial", bg="#20bebe",
                       fg="#fff", width=15, height=2)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)
root.mainloop()
