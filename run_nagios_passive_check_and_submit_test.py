#!/usr/bin/python
from __future__ import division
import glob
import pep8
import sys
import unittest

from run_nagios_passive_check_and_submit import run_check


class RunCheckTestCase(unittest.TestCase):
    def testOK(self):
        result = run_check(['/bin/sh', '-c', '/bin/echo TRUE; /bin/true'])
        self.assertEqual(result, (0, 'TRUE'))

    def testWARNING(self):
        result = run_check(['/bin/sh', '-c', '/bin/echo FALSE; /bin/false'])
        self.assertEqual(result, (1, 'FALSE'))


class CodeFormatTestCase(unittest.TestCase):
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(glob.glob('*.py'))
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warnings).')

if __name__ == '__main__':
    unittest.main()
