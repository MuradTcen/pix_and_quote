#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
global source_url
source_url = 'https://www.quotesdaddy.com/feed'


def load_feed():
    r = requests.get(source_url)
    return r.text


def parse_quote(text):
    quot = text.split('<description>')[2].split('</description>')[0]
    result = quot.split('&quot;')[1] + quot.split('&quot;')[2]
    return result


def main():
    parse_quote(load_feed())


if __name__ == '__main__':
    main()
