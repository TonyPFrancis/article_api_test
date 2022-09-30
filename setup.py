import os
import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent
NAME = "article_api"
# The text of the README file
README = (HERE / "README.md").read_text()


def get_version():
    about = {}
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, NAME.replace("-", "_"), "__version__.py")) as f:
        exec(f.read(), about)
    return about["__version__"]


# This call to setup() does all the work
setup(
    name="article-api-test",
    version=get_version(),
    description="Get basic details from Article URL",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/TonyPFrancis/article_api_test",
    author="Tony P Francis",
    author_email="tony.612.4u@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["article_api"],
    include_package_data=True,
    install_requires=["click", "jmespath", "requests", "lxml"],
    entry_points={
        "console_scripts": [
            "article-api=article_api.__main__:main",
        ]
    },
)
