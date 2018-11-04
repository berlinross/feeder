from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='feeder',
    version='0.1',
    description='Easily fetch, parse and munge data feeds',
    long_description=readme(),
    classifiers=[
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='data feed munger parse fetch get data-feed data-munge parser',
    url='http://github.com/berlinross/feeder',
    author='Seiyifa Tawari',
    author_email='seiyifa@berlinross.io',
    license='MIT',
    packages=['feeder'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
