from setuptools import setup

setup(
    name = 'internal-utils',
    version = '0.0.1',
    description = 'internal utility methods',
    packages = [
        'internal',
    ],
    install_requires = [
        'flask'
    ]
)