import pyttsx3 as p
import PyPDF2 as pdf

book = open("D:/(1) AI and Python course Oxford (by Clevered)/Code Files/Space technique and My Speech.pdf", 'rb')

x = p.init()

reader = pdf.PdfFileReader(book)
num_pages = reader.numPages

print(f"The PDF contains {num_pages} page.")

page1 = reader.getPage(0)
text = page1.extractText()

print(reader)

x.say(text)
x.runAndWait()