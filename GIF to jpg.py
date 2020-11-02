from PIL import Image
s=input("Enter the gif image to convert: ")
m=input("Enter the format of file(jpeg/png): ")
Image.open(s+'.'+'gif').convert('RGB').save(s+'.'+m,m)
