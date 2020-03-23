# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="vanilla-fastapi-skeleton",
    version="1.0.0",
    description="REST API's for testing FastAPI",
    author="Ratan Boddu",
    author_email="ratanboddu@gmail.com",
    classifiers=["Programming Language :: Python :: 3.7"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi==0.52.0",
        "uvicorn==0.11.3"
    ]
)
