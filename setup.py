from setuptools import setup, find_packages


PACKAGE = "multi_form"
NAME = "django-multi-form"
DESCRIPTION = "Django class based views for using more than one Form in a single view."
AUTHOR = "firexd2"
AUTHOR_EMAIL = "den@beloglazov.me"
URL = "https://github.com/Firexd2/django-multi-form"

VERSION = __import__(PACKAGE).__version__

with open("README.rst", 'r') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests", "examples"]),
    zip_safe=False,
)
