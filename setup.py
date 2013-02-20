

from Cython.Distutils import build_ext
from distutils.core import setup 
from distutils.extension import Extension 


ext_modules = [
        Extension("hello", ["hello.pyx"])
    ]

setup( 
    name = "Hello world app", 
    cmdclass = {"build_ext": build_ext}, 
    ext_modules = ext_modules
)


