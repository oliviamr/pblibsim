#################################
######### SiLiCO v. 1.0 #########
### (c)2016 Ethan A. G. Baker ###
##### ethanagbaker@pitt.edu #####
#################################

from distutils.core import setup
import setuptools

setup(name='SiLiCO',
      version='1.0.0',
      description='A Simulator of Long Read Sequencing in PacBio and Oxford Nanopore',
      author='Ethan Alexander Garcia Baker',
      author_email='ethanagbaker@pitt.edu',
      url='https://ethanagbaker.github.io',
      packages=setuptools.find_packages(),
      py_modules=['simulateReads','convertToFasta','generateChrDist','splitGenomeFasta','getRandomPosition','findChromosome', 'SiLiCO'],
      classifiers=['Programming Language :: Python :: 2.7.11'],
      install_requires=['numpy', 'natsort','pybedtools']
     )