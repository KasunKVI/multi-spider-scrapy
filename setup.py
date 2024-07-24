from setuptools import setup, find_packages

setup(
    name='multi_spider_scrapy',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'scrapy': [
            'settings = multi_spider.settings'
        ],
    },
)
