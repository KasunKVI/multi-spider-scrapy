from setuptools import setup, find_packages

setup(
    name='multi-spider-scrapy',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'scrapy': ['settings = multi-spider-scrapy.settings'],
    },
)
