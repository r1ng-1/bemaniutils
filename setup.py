from setuptools import setup
from Cython.Build import cythonize

setup(
    name='bemani',
    version='1.0',
    description='Code and utilities for talking to BEMANI games',
    author='DragonMinded',
    license='Public Domain',
    packages=[
        # Core packages
        'bemani',
        'bemani.common',
        'bemani.data',
        'bemani.data.api',
        'bemani.data.mysql',
        'bemani.protocol',

        # Wrapper scripts and WSGI imports
        'bemani.utils',

        # Frontend packages
        'bemani.frontend',
        'bemani.frontend.account',
        'bemani.frontend.admin',
        'bemani.frontend.arcade',
        'bemani.frontend.home',
        'bemani.frontend.static',
        'bemani.frontend.templates',

        # Game frontends
        'bemani.frontend.iidx',
        'bemani.frontend.popn',
        'bemani.frontend.jubeat',
        'bemani.frontend.bishi',
        'bemani.frontend.ddr',
        'bemani.frontend.sdvx',
        'bemani.frontend.reflec',
        'bemani.frontend.museca',

        # Backend packages
        'bemani.backend',
        'bemani.backend.core',
        'bemani.backend.ess',
        'bemani.backend.iidx',
        'bemani.backend.jubeat',
        'bemani.backend.popn',
        'bemani.backend.bishi',
        'bemani.backend.ddr',
        'bemani.backend.sdvx',
        'bemani.backend.reflec',
        'bemani.backend.museca',

        # API packages
        'bemani.api',
        'bemani.api.objects',

        # Testing game client packages
        'bemani.client',
        'bemani.client.iidx',
        'bemani.client.jubeat',
        'bemani.client.popn',
        'bemani.client.bishi',
        'bemani.client.ddr',
        'bemani.client.sdvx',
        'bemani.client.reflec',
        'bemani.client.museca',
    ],
    install_requires=[
        req for req in open('requirements.txt').read().split('\n') if len(req) > 0
    ],
    ext_modules=cythonize(
        # Compile various low-level portions of the protocol to get a massive
        # per-packet speed boost.
        [
            "bemani/protocol/binary.py",
            "bemani/protocol/lz77.py",
            "bemani/protocol/node.py",
            "bemani/protocol/protocol.py",
            "bemani/protocol/stream.py",
            "bemani/protocol/xml.py",
        ],
        language_level=3,
    ),
    include_package_data=True,
    zip_safe=False,
)
