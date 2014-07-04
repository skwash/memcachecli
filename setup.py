from setuptools import setup

setup(
    name="memcachecli",
    version="0.0.1",
    description="An interactive CLI for memcached.",
    author="Josh Hansen",
    author_email="josh@skwash.net",
    py_modules=["memcachecli"],
    install_requires=['python-memcached', ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'memcachecli = memcachecli.cli:main',
        ]
    }
)
