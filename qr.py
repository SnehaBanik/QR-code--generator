import qrcode

data = input("Enter text or URL to generate QR code: ")


qr=qrcode.QRCode(

    version=1,
    box_size=10,    
    border=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")