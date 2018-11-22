import PyPDF2

pdfFileObj = open("/Users/xihe/Desktop/aa.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(type(pageObj))

pdfFileObj.close()