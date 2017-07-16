#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('..')
from quote import parse_quote
BASE_QUOTE = '<description></description><description> '
base = '\u201c\u201d\n '


class MyListTest(unittest.TestCase):

    def test_double_name_with_dash(self):
        res = parse_quote(
            BASE_QUOTE + '&quot;&quot;- Abe Lemons-Lemons-Lemons - Lemons </description>')
        self.assertEqual(res, base + 'Abe Lemons-Lemons-Lemons - Lemons ')

    def test_br(self):
        res = parse_quote(BASE_QUOTE + '''&quot;&lt;br/&gt;&quot; - R.C. Sherriff</description>''')
        print(res)
        print(res)
        self.assertEqual(res, '\u201c<br/>\u201d\n R.C. Sherriff')
if __name__ == '__main__':
    unittest.main()
