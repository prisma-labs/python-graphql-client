from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='graphqlclient',
      version='0.2.1',
      description='Simple GraphQL client for Python 2.7+',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/graphcool/python-graphql-client',
      author='prisma.io',
      author_email='hello@prisma.io',
      license='MIT',
      packages=['graphqlclient'],
      install_requires=[
          'six',
      ],
      zip_safe=False)
