#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from random import randint
global source_url
source_url = 'https://desktoppr.co/wallpapers'


def get_max_id():
    soup = BeautifulSoup(requests.get(source_url).text, 'lxml')
    max_id = int(soup.find('div', id='wallpapers-list').find('a',
                                                             href=True)['href'].split('/')[2])
    return max_id


def download_photo(url):
    filename = 'src/' + url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(filename, 'w') as file:
        for chunk in r.iter_content(4096):
            file.write(chunk)
    return filename


def get_random_link(max_id):
    url_pix = source_url + '/' + str(randint(0, max_id))
    if check_existence_pic(url_pix):
        return url_pix
    else:
        get_random_link(max_id)


def get_url_pix(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    result = soup.find('img')['src']
    return result


def check_existence_pic(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    if not soup.find('div', id='error-page'):
        return True
    else:
        return False


def main():
    print(download_photo(get_url_pix(get_random_link(get_max_id()))))

if __name__ == '__main__':
    main()
