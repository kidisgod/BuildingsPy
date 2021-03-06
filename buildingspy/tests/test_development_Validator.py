#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
#from __future__ import unicode_literals

import unittest

class Test_development_Validator(unittest.TestCase):
    """
       This class contains the unit tests for
       :mod:`buildingspy.development.Validator`.
    """

    def test_validateHTMLInPackage(self):
        import os
        import buildingspy.development.validator as v
        val = v.Validator()
        myMoLib = os.path.join("buildingspy", "tests", "MyModelicaLibrary")
        # Get a list whose elements are the error strings
        errStr = val.validateHTMLInPackage(myMoLib)
        self.assertEqual(len(errStr), 0)
        # Test a package that does not exist
        self.assertRaises(ValueError, val.validateHTMLInPackage, "non_existent_modelica_package")

if __name__ == '__main__':
    unittest.main()

