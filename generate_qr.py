import pyqrcode
import png
from pyqrcode import QRCode
import pyfiglet

# string which represents the QRCode.
s = "https://couresera.org"

# generate QR code
url = pyqrcode.create(s)

# Create and save the SVG file.
url.svg("MyQR_svg.svg", scale = 10)

# Create and save the png file.
url.png("MyQR_png.png", scale = 12)

assci_msg = pyfiglet.figlet_format("Q R Generated !")
print(assci_msg)

