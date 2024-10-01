# setup.py

from setuptools import setup, find_packages

setup(
    name='sisop',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pycryptodome',
    ],
    entry_points={
        'console_scripts': [
            'sisop=my_module.main:main',
        ],
    },
)