#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pictures
import quote
import textwrap

text = quote.parse_quote(quote.load_feed())
pix = pictures.download_photo(pictures.get_url_pix(
    pictures.get_random_link(pictures.get_max_id())))


def adding_text(pix, text):
    output_pix = pix.split('.')[-2] + '_out.' + pix.split('.')[-1]
    lines = textwrap.wrap(text, width=20)
    y_text = 100
    image = Image.open(pix)
    # font = ImageFont.load_default().font
    # font = ImageFont.truetype("fonts/Verdana.ttf", 48)
    # font = ImageFont.truetype("fonts/CAC Champagne.ttf", 32)
    font = ImageFont.truetype("fonts/44v2.ttf", 32)
    draw = ImageDraw.Draw(image)
    # draw.text((0, 0), text, (0, 0, 0), font=font)
    # draw.multiline_text((50, 50), text, fill='white', font=font)
    for line in lines:
        width, height = font.getsize(line)
        draw.text((100, y_text), line, font=font, fill='black')
        y_text += height
    image.save(output_pix)


def main():
    print(text, pix)
    adding_text(pix, text)

if __name__ == '__main__':
    main()
