from PyPDF2 import PdfFileReader, PdfFileWriter

input_file = PdfFileReader('Introduction Python.pdf')

print( input_file.numPages)

output_file = PdfFileWriter()

for i in range(input_file.numPages):
    #Copy Page from input pdf
    page = input_file.getPage(i)
    # Paste Page to output file
    output_file.addPage(page)

password = "fv$321"

output_file.encrypt(password)

with open("Encypted File.pdf", "wb") as filename:
     output_file.write(filename)


