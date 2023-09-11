import tkinter as tk
from tkinter import filedialog
import PyPDF2
from docx import Document  # Import the Document class from the docx library

def convert_pdf_to_word():
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    if pdf_file_path:
        pdf_text = ""
        
        pdf_file = open(pdf_file_path, 'rb')  # Correct variable name
        
        pdf = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf.pages)):  # Use len(pdf.pages) to get the number of pages
            page = pdf.pages[page_num]  # Use pdf.pages to access pages
            pdf_text += page.extract_text()
            
        pdf_file.close()
            
        doc = Document()  # Create a new Document instance
            
        doc.add_paragraph(pdf_text)
            
        word_file = pdf_file_path.replace(".pdf", ".docx")  # Correct variable name
        doc.save(word_file)
            
        result_label.config(text=f"Conversion complete. Saved as {word_file}")
    else:
        result_label.config(text="Error during conversion.")

# Create the main window
root = tk.Tk()
root.title("PDF to Word Converter")
root.geometry("300x300")

# Create and place widgets
convert_button = tk.Button(root, text="Convert PDF to Word" ,bg='blue' ,fg='white', command=convert_pdf_to_word)
convert_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
