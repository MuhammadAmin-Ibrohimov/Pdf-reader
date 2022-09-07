import PyPDF2
def main():
    pdffile = "matematika.pdf"
    pdfRead = PyPDF2.PdfFileReader(pdffile)
    
    for i in range(pdfRead.getNumPages()):
        page = pdfRead.getPage(i)
        print("page no: " + str(1 + pdfRead.getPageNumber(page)))
        pageContent = page.extractText()
        print(pageContent)

if __name__ == "__main__":
    main()