from setuptools import setup, find_packages

required_packages = [
    'graphql-core>=2.0', 'webob', 'graphql-server-core>=1.0.dev'
]

tests_require = ['pytest>=2.7.3', 'mako']

setup(
    name='WebOb-GraphQL',
    version='1.0',
    description=
    'Adds GraphQL support to your WebOb (Pyramid/Pylons/...) application',
    long_description=open('README.rst').read(),
    url='https://github.com/graphql-python/webob-graphql',
    download_url='https://github.com/graphql-python/webob-graphql/releases',
    author='Syrus Akbary',
    author_email='me@syrusakbary.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='api graphql protocol rest webob',
    packages=find_packages(exclude=['tests']),
    install_requires=required_packages,
    extras_require={
        'test': tests_require,
    },
    tests_require=tests_require,
    include_package_data=True,
    zip_safe=False,
    platforms='any', )
