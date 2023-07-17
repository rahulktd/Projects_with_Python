import qrcode
from PIL import Image

# data = 'https://rahulkp.netlify.app/'
data = 'https://github.com/rahulktd'

qr = qrcode.QRCode(version=1, border=5,box_size=10)
qr.add_data(data)
qr.make(fit=True)

Image =qr.make_image(fill="black", black_color='white')

Image.save("github_qr.png")
# Image.open("twitter_qr.png")
