from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [Extension("performace_cython", ["performace_cython.pyx"])]

setup(
    ext_modules = cythonize(extensions)
)
