from setuptools import setup, find_packages
setup(
    name="custom_stdio",
    version="preclassic-0.30",
    packages=find_packages(),
    author="Nguyễn Phúc Khang",
    author_email="Khang0762412064@outlook.com",
    description="A new Python package will simulate some function in stdio.h of C",
    long_description=open('README.md'),
    url="https://github.com/kalksdlkdsa/custom_stdio",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9, <3.12',
)
