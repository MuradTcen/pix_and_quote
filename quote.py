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
    result = '\u201c' + \
        quot.split('&quot;')[1] + '\u201d\n' + \
        '-'.join(quot.split('&quot;')[2].split('-')[1:])
    result = result.replace('&lt;br/&gt;', '<br/>')
    return result


def main():
    parse_quote(load_feed())


if __name__ == '__main__':
    main()
