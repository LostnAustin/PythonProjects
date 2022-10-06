import PyPDF2
import sys
import os

#merge two pdf's

#grab file from current directory 
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger = PyPDF2.PdfFileMerger()
        merger.append(file)
    merger.write("combinedDocs.pdf")
  