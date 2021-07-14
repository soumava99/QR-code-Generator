import qrcode 


qr = qrcode.QRCode(version = 1,
                    error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = 4,
                    border = 1)
qr.add_data("Any data or link")
qr.make(fit = True)

img = qr.make_image(fill_color = "black",back_color = "white")
img.save("myQR.png")


 
