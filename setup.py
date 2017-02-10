import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "HumanReadableBinaryConverter",
    version = "0.1.1.0.1.0.1",
    author = "Tim Lardner",
    author_email = "timlardner@gmail.com",
    description = ("A utility to convert unfriendly binary code into something that's readable by humans."),
    license = "MIT",
    keywords = "binary human readable",
    url = "https://github.com/timlardner/HumanReadablePython",
    #packages=['an_example_pypi_project', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)
