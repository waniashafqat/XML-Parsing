# Importing module for parsing XML data.
import xml.etree.ElementTree as ET

# Importing module to store the output in Excel file.
import openpyxl

# Parsing the XML file from the directory using Element Tree.
tree = ET.parse('D:/compiler.xml')

root = tree.getroot()

# Workbook object.
wb = openpyxl.Workbook()
ws = wb.active

# Adding the Header Row to be displayed in Excel file.
ws.append(['Book ID', 'Author Name', 'Title', 'Genre', 'Price', 'Publish Date', 'Description'])

for book in root:
    book_id = book.get('id')
    author_name = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    price = book.find('price').text
    publish_date = book.find('publish_date').text
    description = book.find('description').text

    # Adding the extracted data to the worksheet as a new row.
    ws.append([book_id, author_name, title, genre, price, publish_date, description])

# Excel file for the data extracted.
wb.save('data.xlsx')

