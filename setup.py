from setuptools import setup, find_packages
import memcachecli

setup(
    name="memcachecli",
    version=memcachecli.__version__,
    description="An interactive CLI for memcached.",
    packages=find_packages(exclude=["tests"]),
    install_requires=['python-memcached', ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'memcachecli = memcachecli.cli:main',
        ]
    }
)
