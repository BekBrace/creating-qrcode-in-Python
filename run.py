import qrcode

data_input = 'https://www.youtube.com/watch?v=uAk_cYFPg0s&list=PLrOQsSoS-V6-xXxsZ7hhfRRLETPm2g14h'


# Setup of QR
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4)

# Adding our data to QR
qr.add_data(data_input)

# Compile data to QR code array
qr.make(fit=True)

link = qr.make_image(fill_color="black", back_color="white")
link.save("qrcode_youtube.png")

# ///////////////////////////////////////

# How to create a QRCODE quickly [ not recommended ]
password = "123456"
qr = qrcode.make(password)
qr.save('password.png')


# Documentation for QRCODE
# https://pypi.org/project/qrcode/
