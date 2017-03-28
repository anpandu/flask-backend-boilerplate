import os
import unittest
import json

from application import app
 
class ApplicationTests(unittest.TestCase):
 
  def setUp(self):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['DEBUG'] = False
    self.app = app.test_client()
 
  def tearDown(self):
    pass
 
  def testBasic(self):
    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)
    
if __name__ == "__main__":
  unittest.main()