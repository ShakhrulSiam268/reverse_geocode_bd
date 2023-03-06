from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.0'
DESCRIPTION = 'Offline reverse geocoder for Bangladesh Map'
LONG_DESCRIPTION = 'A Python library for offline reverse geocoding. Reverse Geocode BD takes a (latitude , longitude) coordinate and returns the Division, District, Upazila and Thana of any location in Bangladesh.'

with open("readme.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="reverse-gecode-bd",
    version=VERSION,
    author="Shakhrul Iman Siam",
    author_email="<shakhrulsiam268@gmail.com>",
    url= "https://github.com/ShakhrulSiam268/reverse_geocode_bd",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)