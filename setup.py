from setuptools import setup, find_packages

install_requires = [
    "graphql-server[webob]>=3.0.0b1",
]

tests_requires = [
    "pytest>=5.4,<5.5",
    "pytest-cov>=2.8,<3",
    "Jinja2>=2.10.1,<3",
]

dev_requires = [
    "flake8>=3.7,<4",
    "isort>=4,<5",
    "check-manifest>=0.40,<1",
] + tests_requires

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='WebOb-GraphQL',
    version='2.0rc0',
    description=
    'Adds GraphQL support to your WebOb (Pyramid/Pylons/...) application',
    long_description=readme,
    url='https://github.com/graphql-python/webob-graphql',
    download_url='https://github.com/graphql-python/webob-graphql/releases',
    author='Syrus Akbary',
    author_email='me@syrusakbary.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'License :: OSI Approved :: MIT License',
    ],
    keywords='api graphql protocol rest webob',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    tests_require=tests_requires,
    extras_require={
        'test': tests_requires,
        'dev': dev_requires,
    },
    include_package_data=True,
    zip_safe=False,
    platforms='any',
)
