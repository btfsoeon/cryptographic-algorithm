from setuptools import find_packages, setup, version

setup(
    name = 'cryptographic algorithms',
    version = '0.1',
    description = 'Implementation of modern cryptographic algorithms from scratch',
    author = 'Soeon Park',
    python_requires = '>3.7',
    install_requires = [
        'pytest',
        'ipytest'
    ]
)
