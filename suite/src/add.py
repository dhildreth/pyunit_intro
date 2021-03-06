'''This is a simple program to demonstrate how to create a unittest in 
Python.  For more information and documentation, please see the official
documentation page here: http://docs.python.org/library/unittest.html'''

import os, unittest    #Include the pyUnit unittest framework

def add(a,b,c=0):
   '''A simple adding function to demo unittest'''
   return a+b+c

# The following is the class in which all functions will be ran by unittest
class AddTest(unittest.TestCase):
   ''' Main class for add testing; Can be added to a suite'''


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
   def test_positive_add(self):
      '''Verify that adding positive numbers works''' # Printed if test fails
      self.assertEqual(add(10,23,22), 55) # Test will fail if "false" (boolean)
      self.assertEqual(add(11,23), 34)
      self.assertEqual(add(1,1,17), 19)

   # Functions beginning with "test" will be ran as a unit test.
   # @unittest.skip("demonstrating skipping") # Skip this test (Python >= 2.7)
   def test_negative_add(self):
      '''Verify that adding negative numbers works''' # Printed if test fails
      self.assertEqual(add(-12,23), 11)

   # Functions beginning with "test" will be ran as a unit test.
   # In this case, this test will be skipped.
   #@unittest.skip("demonstrating skipping")
   def test_negative_add_skip(self):
      '''Verify that adding negative numbers works (fail example)''' # Printed if test fails
      self.assertEqual(add(-12,23), 10)

# In case this script is called directly and not as a module
if __name__=='__main__':
   unittest.main()
