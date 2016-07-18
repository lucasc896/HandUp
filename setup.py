# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup

requirements = os.path.join(os.path.dirname(__file__), 'requirements.txt')


setup(
    name="HandUp",
    version="0.0.1",
    author="ChrisLucas",
    author_email="lucasc896@gmail.com",
    description="",
    url="https://github.com/lucasc896/HandUp",
    packages=find_packages(exclude=['tests', 'tests.*']),
    entry_points={
        "console_scripts": [
            "manage-db=handup.models.manage:main",
        ]
    }
)