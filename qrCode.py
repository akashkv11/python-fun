import pyqrcode;

import png;

from pyqrcode import QRCode;

s = "https://github.com/akashkv11";

url = pyqrcode.create(s);

url.png('qr-gen.png', scale = 6);
