
import numpy
from setuptools import Extension,setup
from glob import glob
import os


AUTHOR='Russell Ryan'
PKG='polyclip'
info={
    '__author__': AUTHOR,
    '__version__': '1.0',
    '__maintainer__': AUTHOR,
    '__email__': 'rryan@stsci.edu',
    '__credits__': ['python: {}'.format(AUTHOR),'C: JD Smith'],
    '__doc__':'Python driver for polyclip routines written by JD Smith',

}

# Generate package metadata
with open(os.path.join(PKG, 'info.py'), 'w+') as fp:
    for k, v in info.items():
        fp.write('{} = "{}"{}'.format(k, v, os.linesep))


setup(name=PKG,
      version=info['__version__'],
      author=info['__author__'],
      author_email=info['__email__'],
      keywords="Sutherland Hodgman polygon clipping C python",\
      long_description=info['__doc__'],
      license='MIT',\
      packages=['polyclip'],\
      install_requires=['numpy'],\
      classifiers=["Development Status :: 5 Production/Stable ",
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering :: Astronomy',],\
      ext_modules=[
          Extension('polyclip.cpolyclip',glob(os.path.join(PKG,'src','*.c')),
                    include_dirs=[os.path.join(PKG,'include'),
                                  numpy.get_include()])])
      
