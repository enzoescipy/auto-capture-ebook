#-*- coding:utf-8 -*-

from pdf2image import convert_from_path
from tkinter import filedialog

file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("PPTX files", "*.pptx"),
                                          ("all files", "*.*")))

pages = convert_from_path("./source/" + file_name)

for i, page in enumerate(pages):
	page.save("./source/"+file_name+str(i)+".jpg", "JPEG")



