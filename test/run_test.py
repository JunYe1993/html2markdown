import sys
import unittest
from bs4 import BeautifulSoup

sys.path.insert(0, "..")
import html2markdown as h2m

class Test_createMarkdownString (unittest.TestCase):

    def test_case1 (self):
        data = ""
        with open ("./sample/testcase1.html") as f:
            data = f.read()
        soup = BeautifulSoup(data, features="html.parser")
        h2m.createMarkdownString(soup)

if __name__ == '__main__':
	unittest.main()