# Script to handle installation (dependencies, package building, etc.)

from setuptools import find_packages, setup

setup (
    name = "Medical Chatbot AI",
    version = "0.0.1",
    author = "Pritha Majumder",
    author_email = "prithatiti@gmail.com",
    packages = find_packages(),
    install_requires = []
)