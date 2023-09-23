#THIS FILE IS FOR WORKING WITH PDF

from PyPDF2 import PdfReader, PdfWriter

def pdf_runner(file_txt_path: str = "", pdf_file_path: str = ""):#RUNNING PDF LOGIC
    reader = PdfReader(pdf_file_path)#PASS THE PDF FILE PATH TO THE CONSTRUCTOR
    number_of_pages = len(reader.pages)#LENGTH OF PAGES
    page = reader.pages[4]#PAGE NO 3 OF THE PDF
    text = page.extract_text()#GET THE TEXTS OF THE READER.PAGES[4]
    print(page)
    print(number_of_pages)
    meta = reader.metadata #GET METADATA OF THE PDF FILE
    # All of the following could be None!
    print(meta.author)
    print(meta.creator)
    print(meta.producer)
    print(meta.subject)
    print(meta.title)
    if file_txt_path == "":
        return

    with open(file_txt_path, "w") as F:# WRITE THE TEXT OF THE PARTICULAR PDF PAGE TO A TEXT file
        F.write(text)
    F.close()

def decrypt_pdf(encrypted_pdf: str, password: str, encrypt_file_pdf_name: str = ""):
    try:
        reader = PdfReader(encrypted_pdf)
        writer = PdfWriter()

        if reader.is_encrypted:
            reader.decrypt(password)

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Save the new PDF to a file
        if encrypt_file_pdf_name == "":
            return

        with open(encrypt_file_pdf_name, "wb") as f:
            writer.write(f)
    except Exception as error:
        print(error)


def encrypt_pdf(filename: str,  password: str, encrypt_file_pdf_name: str = ""):
    try:
        reader = PdfReader(filename)
        writer = PdfWriter()

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Add a password to the new PDF
        writer.encrypt(password)

        if encrypt_file_pdf_name == "":
            return

        # Save the new PDF to a file
        with open(encrypt_file_pdf_name, "wb") as f:
            writer.write(f)

    except Exception as error:
        print(error)
