# En setup.py

from setuptools import setup, find_packages

setup(
    name='arnautaga-GTDM-Functions',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        # Otras dependencias de tu biblioteca
    ],
)