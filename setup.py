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
            'memcachecli = memcachecli:main',
        ]
    },
    license="MIT",
    keywords='memcached',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
