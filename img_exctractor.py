# this class extract all the links on an url
from urllib.request import urlopen
from urllib.parse import urljoin
import re


def download_page(url):
    return urlopen(url).read().decode('utf-8')


def extract_imagen(page):
    link_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page)


