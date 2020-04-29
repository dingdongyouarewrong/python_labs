from PIL import ImageDraw, ImageFont
from PIL import Image

code_path = "qr.png"
output = "out.png"
image_width = 600
raw_image_path = "sokolov.jpg"
logo_path = "logo.png"

raw_image = Image.open(raw_image_path)
logo = Image.open(logo_path)
code = Image.open(code_path)
image_height = image_width * raw_image.size[1] // raw_image.size[0]
raw_image = raw_image.resize((image_width, image_height), Image.ANTIALIAS)
logo_width = image_width // 10
logo_height = logo_width * logo.size[1] // logo.size[0]
logo = logo.resize((logo_width, logo_height), Image.ANTIALIAS)
code = code.resize((100, 100), Image.ANTIALIAS)
if raw_image.size[1] > raw_image.size[0]:
    raw_image = raw_image.rotate(180)
idraw = ImageDraw.Draw(raw_image)
text = "Было снято в городе ессентуки \n Georgia go! go! go!"
font = ImageFont.truetype("9206.otf", size=18)
idraw.text((image_width // 2 - 125, image_height - 50), text, font=font)
raw_image.paste(logo, (image_width - logo_width, 0), logo)
raw_image.paste(code, (0, 0))
raw_image.save(output)


