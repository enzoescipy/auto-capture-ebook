import os
import img2pdf

with open("result.pdf", "wb") as f:
    img_list = []
    imglist = os.listdir("result")

    for file in imglist:
        if file.endswith(".png"):
            img_list.append(file)
    
    img_list.sort(key=lambda x : int(x.split(".")[0]) )

    dir_list = ["result/" + img for img in img_list]

    print(dir_list)
    pdf = img2pdf.convert(dir_list)
    f.write(pdf)