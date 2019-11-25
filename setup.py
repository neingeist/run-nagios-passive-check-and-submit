from __future__ import division, print_function

from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages
import sys


class Tox(TestCommand):

    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


install_requires = ['PyYAML', 'beautifulsoup4', 'lxml', 'requests',
                    'termcolor']
tests_require = ['pep8']

setup(
    name='run-nagios-passive-check-and-submit',
    version='0.1.5',
    packages=find_packages(),
    scripts=['run-nagios-passive-check-and-submit'],
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': Tox},
)
