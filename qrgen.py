# -*- coding: utf-8 -*-
from PIL import Image
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(""" But as the sun was rising from the fair sea into the firmament of heaven to shed light on mortals and
immortals, they reached Pylos the city of Neleus. Now the people of Pylos were gathered on the sea shore to offer
sacrifice of black bulls to Neptune lord of the Earthquake. There were nine guilds with five hundred men in each,
and there were nine bulls to each guild.
            """)

qr.make(fit=True)

img = qr.make_image()

img.save('link.png')
