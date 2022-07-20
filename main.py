from PyPDF4 import PdfFileWriter, PdfFileReader
from os import walk

mypath = "input"
filenames = next(walk(mypath), (None, None, []))[2]

for file in filenames:
    print("0 Duplicating : " + file)

    #duplicating each pages for 8x
    with open("input\\" + file, "rb") as in_f:
        input1 = PdfFileReader(in_f)
        output = PdfFileWriter()
        numPages = input1.getNumPages()

        for dup in range(numPages):
            for rep in range(8):
                page = input1.getPage(dup)
                output.addPage(page)
            with open("temp\\"+file, "wb") as out_f:
                output.write(out_f)
    print("1 Duplicating : " + file)

    #crop each duplicated pages into page 1,2,3,etc...
    #each page ( n * (1 -> 8)  ) has unique location (pixel coordinate)
    print("2 Cropping : " + file)
    
    with open("temp\\" + file, "rb") as in_f:
        input1 = PdfFileReader(in_f)
        output = PdfFileWriter()
        numPages = input1.getNumPages()
                   
        
        x = [0,456,456*2,456*3]
        y_lower = [0,1296/2]
        k=0
        j=0
        for i in range(numPages):
            page = input1.getPage(i)

            if k >= 456*4:
                k=0
                j+= 1296/2

            if i%8 == 0:
                k=0
                j=0
        
            page.cropBox.lowerLeft = (0+k, (1296/2) - j)
            page.cropBox.lowerRight = (456+k, (1296/2) - j)
            page.cropBox.upperLeft = (0+k, 1296-j)
            page.cropBox.upperRight = (456+k, 1296-j)
            output.addPage(page)

            k+= 456
    
        print(file)
        print("3 Cropped : " + file)
        print("4 Printing : " + file)  
        with open("output\\"+file, "wb") as out_f:
            output.write(out_f)
        print("5 Printed : " + file)
        


