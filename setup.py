from os import path

here = path.abspath(path.dirname(__file__))

from pip.req import parse_requirements

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(path.join(here, 'requirements.txt'), session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

from distutils.core import setup
setup(
  name = 'fono',
  packages = ['fono'], # this must be the same as the name above
  version = '0.1.2',
  description = 'A python package to find optimal number of orders',
  long_description=long_description,
  author = 'Dheepak Krishnamurthy',
  author_email = 'kdheepak89@gmail.com',
  url = 'https://github.com/kdheepak89/fono', # use the URL to the github repo
  download_url = 'https://github.com/kdheepak89/fono/tarball/0.1', # I'll explain this in a second
  keywords = ['pyomo', 'operations'], # arbitrary keywords
  license = ['LICENSE'],
  install_requires=reqs,
  classifiers = [],
)
