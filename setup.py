
from distutils.core import setup, Extension
import numpy.distutils.misc_util


setup(name='polyclip',\
      version='1.0', \
      author='Russell Ryan', \
      author_email='rryan@stsci.edu',\
      keywords="Sutherland Hodgman polygon clipping C python",\
      description='Python API for calling JD Smith polyclip',\
      license='MIT',\
      packages=['polyclip'],\
      #install_requires=['numpy'],\
      classifiers=["Development Status :: 5 Production/Stable ",
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering :: Astronomy',],\
      ext_modules=[Extension('cpolyclip',['polyclip/_polyclip.c',\
                                          'polyclip/polyclip.c'])],\
      include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs())


