'''This is a simple program to demonstrate how to create a unittest in 
Python.  For more information and documentation, please see the official
documentation page here: http://docs.python.org/library/unittest.html'''

import unittest    #Include the pyUnit unittest framework
import math        #Include math library

def sin(a):
   '''A simple function to demo unittest'''
   return math.sin(a) 

def cos(a):
   '''A simple function to demo unittest'''
   return math.cos(a) 

class TrigTest(unittest.TestCase):
   ''' Main class for add testing; Can be added to a suite'''

   def setUp(self):
      '''Verify environment is setup properly''' 
      pass

   def tearDown(self):
      '''Verify environment is tore down properly''' 
      pass

   def test_sin(self):
      '''Verify that sin() works'''
      # This is an example of using "assertAlmostEqual" with sin function
      # The actual result of sin((3/2)/math.pi) is 0.31296179620778664
      # The 'msg' will print in case of failure (Assert: msg)
      self.assertAlmostEqual(sin((3/2)/math.pi), 0.313, 3, msg=None)
      
   def test_cos(self):
      '''Verify that cos() works''' 
      self.assertEqual(cos(0), 1)

if __name__=='__main__':
   unittest.main()
