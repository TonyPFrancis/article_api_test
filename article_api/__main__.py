"""
This is a test module to show the Creation of packages in Zytes Internal PyPi
"""
import argparse
import json
import logging

import jmespath
import requests
from lxml import html

# logger specific variables
log_format = "%(name)s - %(asctime)s - %(levelname)7s ==> %(message)s"
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
log_format = logging.Formatter(fmt=log_format)
c_handler.setFormatter(log_format)
logger.addHandler(c_handler)

# requests specific variables
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
}


def main(*args, **kwargs):
    if not (url := kwargs.get("url")):
        parser = argparse.ArgumentParser()
        parser.add_argument("--url", help="Article URL to extract")
        parser_args = parser.parse_args()
        url = parser_args.url
    response = requests.get(url=url, headers=HEADERS)
    sel = html.document_fromstring(response.text)
    json_data = json.loads(sel.xpath('//script[@type="application/ld+json"]/text()')[0])
    item = {
        "url": jmespath.search("url", json_data),
        "source_name": jmespath.search("publisher.name", json_data),
        "source_logo": jmespath.search("publisher.logo.url", json_data),
        "date": jmespath.search("datePublished", json_data),
        "title": jmespath.search("headline", json_data),
        "thumbnail": jmespath.search("image.url", json_data),
        "author": jmespath.search("author.name", json_data),
    }
    return item


if __name__ == "__main__":
    main()
