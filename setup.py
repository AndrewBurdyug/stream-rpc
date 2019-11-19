"""Пакет проекта."""
from setuptools import setup

setup(
    name="stream-rpc",
    packages=["stream_rpc"],
    version=open("VERSION").read().strip(),
    install_requires=["cryptography==2.8"],
    include_package_data=True,
    author="Andrew Burdyug",
    author_email="buran83@gmail.com",
    description="Stream RPC protocol with cryptography",
    url="https://gitlab.com/",
    license="Copyright (c) 2019 Andrew Burdyug. All rights reserved.",
    keywords="rpc crypto",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Other Audience",
        "Topic :: Internet :: Home Automation",
        "License :: OSI Approved :: Apache Software License v2.0",
        "Programming Language :: Python :: 3.7",
    ],
)
