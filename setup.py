from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.1.0'
DESCRIPTION = 'Package to do maths'
LONG_DESCRIPTION = 'A package that allows to do math calculation. For webapp visit https://mathscal.netlify.app'

# Setting up
setup(name="mathscal",
      version=VERSION,
      author="Aayam Shrestha",
      author_email="aayamthebest555@gmail.com",
      description=DESCRIPTION,
      long_description_content_type="text/markdown",
      long_description=LONG_DESCRIPTION,
      packages=find_packages(),
      keywords=[
          'python', 'math calculation', 'mathscal', 'mathscal python',
          'mathscal python by aayam', 'math calculation by aayam'
      ],
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ])
