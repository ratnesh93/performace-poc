from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [Extension("cython_performance", ["cython_performance.pyx"])]

setup(
    ext_modules = cythonize(extensions)
)
