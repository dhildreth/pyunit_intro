'''This is a simple program to demonstrate how to create a unittest in 
Python.  For more information and documentation, please see the official
documentation page here: http://docs.python.org/library/unittest.html'''

import unittest    #Include the pyUnit unittest framework

def hello(a):
   '''A simple function to demo unittest'''
   return "Hello " + a + "!" 

class HelloTest(unittest.TestCase):
   ''' Main class for add testing; Can be added to a suite'''

   def setUp(self):
      '''Verify environment is setup properly''' 
      pass

   def tearDown(self):
      '''Verify environment is tore down properly''' 
      pass

   def test_hello(self):
      '''Verify that hello() works'''
      self.assertEqual(hello("World"), "Hello World!")
      
if __name__=='__main__':
   unittest.main()
