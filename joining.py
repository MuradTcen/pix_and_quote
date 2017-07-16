#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from random import choice
import pictures
import quote
import textwrap

text = quote.parse_quote(quote.load_feed())
pic = pictures.download_photo(pictures.get_url_pic(
    pictures.get_random_link(pictures.get_max_id())))
types = open('fonts/list.txt').read().split('\n')

is_rgb = lambda x: True if x.mode == 'RGB' else False


def convert_to_png_rgb(pic):
    png_pic = pic.split('.')[-2] + '.png'
    Image.open(pic).convert('RGB').save(png_pic)
    return png_pic


def get_size_for_rect(img, lines):
    pass


def adding_text(pic, text):
    # print(pic)
    if not is_rgb:
        pic = convert_to_png_rgb(pic)
    output_pic = 'out/' + \
        pic.split('.')[-2].split('/')[-1] + '_out.' + pic.split('.')[-1]
    image = Image.open(pic)
    print(image.size)
    font = ImageFont.truetype('fonts/' + choice(types), 32)
    draw = ImageDraw.Draw(image)
    lines = textwrap.wrap(text, width=40)
    margin = offset = 40
    # print(font.getsize(lines[0])[0], font.getsize(lines[0])[1])
    # print(max(lines))
    rect_y1 = (font.getsize(lines[0])[1] + 2) * len(lines)
    rect_x1 = max([(font.getsize(line)[0]) for line in lines])
    rect_size = (rect_x1, rect_y1)
    rect_img = Image.new('RGBA', rect_size, (0, 0, 0, 140))
    image.paste(rect_img, (margin, margin), rect_img)
    for line in lines:
        draw.text((margin, offset), line, font=font, fill=(255, 255, 255))
        offset += font.getsize(line)[1]
        offset += 2
    image.save(output_pic)


def main():
    print(text, pic)
    adding_text(pic, text)

if __name__ == '__main__':
    main()
