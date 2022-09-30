import os

print(os.getcwd())

from ..article_api.__main__ import main as main_url


def test_url():
    url = "https://www.bbc.com/news/science-environment-61383391"
    crawled_item = {
        "url": "https://www.bbc.com/news/science-environment-61383391",
        "source_name": "BBC News",
        "source_logo": "https://static.files.bbci.co.uk/ws/simorgh-assets/public/news/images/metadata/poster-1024x576.png",
        "date": "2022-05-09T23:38:30.000Z",
        "title": "Climate change: 'Fifty-fifty chance' of breaching 1.5C warming limit",
        "thumbnail": "https://ichef.bbci.co.uk/news/1024/branded_news/E4D9/production/_124658585_gettyimages-1240334571.jpg",
        "author": "By Matt McGrath",
    }
    item = main_url(url=url)
    assert item == crawled_item
