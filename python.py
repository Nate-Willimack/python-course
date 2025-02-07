import PyPDF2
import os

merge = PyPDF2.PdfMerger()

for file in os.listdir(os.getcwd()):
    if file.endswith(".pdf"):
        merge.append(file)

merge.write("combinedPDF.pdf")