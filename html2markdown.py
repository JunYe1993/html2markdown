import re
from bs4 import BeautifulSoup

__tag_ignore_set = set([
    '[document]',
    'html',
    'body'
])

def createMarkdownString (tag):
    # recursively change tag string to markdown string
    children = tag.find_all(recursive=False)

    if tag.name in __tag_ignore_set:
        for child in children:
            createMarkdownString(child)
        return
    print(tag.name)        

def convert (html):
    # convert html with BeautifulSoup
    soup = BeautifulSoup(html, features="lxml")

    # change the material in the soup
    createMarkdownString(soup)