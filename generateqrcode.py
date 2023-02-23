import qrcode

lien = input('Lien : ')
img = qrcode.make(lien)
img.save('qrcode.jpg')