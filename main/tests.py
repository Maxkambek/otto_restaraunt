import qrcode

# qr_image = qrcode.make('https://test.goldblock.uz/')
# qr_image.save('ottomenu.png')
# import qrcode

# Data to encode
data = "https://test.goldblock.uz/"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='white',
                    back_color='black')

img.save('MyQRCode2.png')
