# XML Parsing

To parse and extract data, firstly the TXT file (compiler.txt) provided is converted to an XML file (compiler.xml) by changing the extension of the file. Then for parsing, the module ‘xml.etree.ElementTree’ is used. Along with the module ‘openpyxl’ to create a new Excel file and write the extracted data to it. 

The ET.parse( ) function is used to parse the XML file (D:/compiler.xml) from the directory where it is saved. The function then creates an ‘ElementTree’ object, which represents the structure of the XML document as a tree of elements. The getroot( ) method of the ElementTree object is used to get the root element of the tree, which is the top-level element in the XML document.

The openpyxl.Workbook( ) function is used to create a new workbook object, which represents a new, empty excel file. The active property of the workbook object is used to get the active worksheet in the workbook.

After all the data has been written to the worksheet, the save( ) method of the workbook object is then used to save the Excel file, named ‘data.xlsx’.

## Output in Excel File
![image](https://user-images.githubusercontent.com/73712563/211166123-367e3ee7-ffe4-4d99-b411-f0b6aaa3ddb2.png)
