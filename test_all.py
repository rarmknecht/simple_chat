#!/usr/bin/env python
#
#   Randy Armknecht (rarmknecht@gmail.com)
#

import unittest
import pep8
from testscenarios import generate_scenarios, TestWithScenarios


class Pep8ConformanceTestCase(unittest.TestCase):
    """Test that all code confirms to PEP8"""

    def test_pep8_conformance(self):
        self.pep8style = pep8.StyleGuide(show_source=True)
        files = ('server.py', 'test_all.py')
        self.pep8style.check_files(files)
        self.assertEqual(self.pep8style.options.report.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
