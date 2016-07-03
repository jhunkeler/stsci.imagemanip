#!/usr/bin/env python
import os
import subprocess
import sys
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, find_packages, Extension


if os.path.exists('relic'):
    sys.path.insert(1, 'relic')
    import relic.release
else:
    try:
        import relic.release
    except ImportError:
        try:
            subprocess.check_call(['git', 'clone',
                'https://github.com/jhunkeler/relic.git'])
            sys.path.insert(1, 'relic')
            import relic.release
        except subprocess.CalledProcessError as e:
            print(e)
            exit(1)


version = relic.release.get_info()
relic.release.write_template(version, 'stsci/imagemanip')

setup(
    name = 'stsci.imagemanip',
    version = version.pep386,
    author = 'Christopher Hanley',
    author_email = 'help@stsci.edu',
    description = 'STScI general image manipulation tools',
    url = 'https://github.com/spacetelescope/stsci.imagemanip',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'nose',
        'numpy',
        'sphinx',
        'stsci.sphinxext',
        'stsci.tools'
    ],
    packages = find_packages(),
    package_data = {
        '': ['LICENSE.txt'],
    },
    ext_modules=[
        Extension('stsci.imagemanip.bilinearinterp',
            ['src/bilinearinterp.c'],
            include_dirs=[np_include()],
            define_macros=[('NUMPY', '1')])
    ],
)
