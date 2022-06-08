# this class extract all the links on an url
from urllib.request import urlopen
from urllib.parse import urljoin
import re


def download_page(url):
    return urlopen(url).read().decode('utf-8')


def extract_links(page):
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page)


if __name__ == '__main__':
    target_url = 'https://www.apress.com/'
    apress = download_page(target_url)
    links = extract_links(apress)
    for link in links:
        print(urljoin(target_url, link))
