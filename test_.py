#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest

from app import app

class BasicTestCase(unittest.TestCase):
    
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard(self):
        tester = app.test_client(self)
        response = tester.get('dashboard', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_predict(self):
        tester = app.test_client(self)
        response = tester.get('predict', content_type='html/text')
        self.assertEqual(response.status_code, 200)


# In[2]:


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

