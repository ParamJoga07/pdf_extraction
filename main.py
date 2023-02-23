import PyPDF3
import tabula
import pandas as pd
import csv


# Open the encrypted PDF
pdf_reader = PyPDF3.PdfFileReader(open('/Users/apple/Documents/GitHub/pdf_extraction/assets/Account Statement.pdf', 'rb'))

# Decrypt the PDF with the password
if pdf_reader.isEncrypted:
    pdf_reader.decrypt('0501@2865')

# Get the number of pages in the PDF
num_pages = pdf_reader.getNumPages()
# num_pages = 3
# Extract tables from all pages using tabula-py
for page_num in range(1, num_pages+1):
    tables = tabula.read_pdf('/Users/apple/Documents/GitHub/pdf_extraction/assets/Account Statement.pdf', pages=page_num, password='0501@2865',area=all, relative_area=True, stream=True, lattice=True, pandas_options={'header': None}, guess=False)
    

    print(f"Tables on page {page_num}:")
    for i, table in enumerate(tables):
        with open(f'table_{i+2}.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            print(table)
            for row in table.values:
                writer.writerow(row)
