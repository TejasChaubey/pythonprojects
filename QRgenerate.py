import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10,
border=4,)
     #QRcode change the functionality of qr.
qr.add_data("https://github.com/TejasChaubey")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("tejas_github.png")