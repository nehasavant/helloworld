from setuptools import setup, find_packages
setup(
    name="helloworld",
    version="0.1",
    packages=find_packages(),
    author="Neha Savant",
    license="GPLv3",
    description="A package for saying hello and other things",
    entry_points={
        'console_scripts': ['helloworld = helloworld.__main__:main']
        },
    classifiers=["Programming Language :: Python :: 3"],
)