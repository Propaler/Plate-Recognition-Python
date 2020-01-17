import setuptools
import sys
import os

try:  # for pip >= 10
    from pip._internal.req import parse_requirements as parse
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements as parse

from setuptools import find_packages

requirements = (lambda f: [str(i.req) for i in parse(f, session=False)])(
    "requirements.txt"
)

setuptools.setup(
    name="plateDetector",
    version="0.0.1",
    author="Propaler",
    description="Package to detect plates",
    platforms="any",
    license="None",
    package_data={"texts": ["plateDetect/texts/ *"]},
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)
