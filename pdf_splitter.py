###############################################
#         Simple PDF Splitter CL Tool
#               Using PyPDF2
# Splits a PDF into a new one given a range
# of pages or a comma separated list of pages
#
#          Developed by Bradley
##############################################

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

def init_pdf_reader():
    pdf_location = input("Location of PDF file > ")
    pdf_reader = PdfFileReader(pdf_location)
    return pdf_reader

def display_pdf_metadata(pdf_reader):
    document_information = pdf_reader.getDocumentInfo()
    print("Author:", document_information.author)
    print("Title:", document_information.title)
    print("Number of pages:", str(pdf_reader.getNumPages()))

def get_pages_list(pdf_reader):

    page_numbers= input("Pages to extract seperated with commas > ").split(",")
    page_numbers = [int(i) - 1 for i in page_numbers] #convert str to ints and get index of selected pages

    page_objects = []

    for page_number in page_numbers:
        a_page = pdf_reader.getPage(page_number)
        page_objects.append(a_page)

    return page_objects

def get_pages_range(pdf_reader):
    range_of_pages = input("Range of pages to extract (Seperate with a '-') > ").split("-")

    range_of_pages[0] = int(range_of_pages[0]) - 1 # i.e. if page 1, index 0
    range_of_pages[1] = int(range_of_pages[1]) - 1 # i.e. if page 5/5 index 4

    page_objects = []

    for page_number in range(range_of_pages[0], range_of_pages[1] + 1):  # i.e. range 0 --> 5  = indexes 0-4
        a_page = pdf_reader.getPage(page_number)
        page_objects.append(a_page)

    return page_objects

def create_new_pdf(pages):
    new_pdf_location = input("Directory location for new PDF including file name & extension > ")
    new_pdf = open(new_pdf_location, "wb")
    pdf_writer = PdfFileWriter()
    for page in pages:
        pdf_writer.addPage(page)
    pdf_writer.write(new_pdf)
    new_pdf.close()
    print("New PDF created")



pdf_reader = init_pdf_reader()
display_pdf_metadata(pdf_reader)

choice = input("Enter r to get a contiguous range of pages or l to select each page > ")
choice = choice.lower()

if choice == "r":
    selected_pages = get_pages_range(pdf_reader)
else:
    selected_pages = get_pages_list(pdf_reader)


create_new_pdf(selected_pages)