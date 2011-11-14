'''This is a simple program to demonstrate how to create a unittest in 
Python.  For more information and documentation, please see the official
documentation page here: http://docs.python.org/library/unittest.html'''

import unittest    #Include the pyUnit unittest framework

def subtract(a,b):
   '''A simple subtracting function to demo unittest'''
   return a-b

# The following is the class in which all functions will be ran by unittest
class SubtractTest(unittest.TestCase):
   ''' Main class for subtract testing; Can be added to a suite'''

   # The function "setUp" will always be ran in order to setup the
   # test environment before all the tests have run.
   def setUp(self):
      '''Verify environment is setup properly''' # Printed if test fails
      pass

   # The function "tearDown" will always be ran in order to cleanup the
   # test environment after all the tests have run.
   def tearDown(self):
      '''Verify environment is tore down properly''' # Printed if test fails
      pass

   # Functions beginning with "test" will be ran as a unit test.
   def test_positive_subtract(self):
      '''Verify that subtracting positive numbers works''' # Printed if test fails
      self.assertEqual(subtract(10,5), 5) # Test will fail if "false" (boolean)

   # Functions beginning with "test" will be ran as a unit test.
   # @unittest.skip("demonstrating skipping") # Skip this test (Python >= 2.7)
   def test_negative_add(self):
      '''Verify that subtracting negative numbers works''' # Printed if test fails
      self.assertEqual(subtract(-10,5), -15)

# In case this script is called directly and not as a module
if __name__=='__main__':
   unittest.main()
