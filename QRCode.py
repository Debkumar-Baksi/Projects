# pip install qrcode
# pip install pillow 
import qrcode
import qrcode.constants

url=str(input("Enter URL : "))
fc=str(input("Enter fill color : ")) # should be in lowercase and correct spelling
bc=str(input("Enter back color : ")) # should be in lowercase and correct spelling


qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill_color=fc,back_color=bc)
img.save("MyQR.png")
print("QR Code Generated Successfully") # goto your folder where this code is running and check the file