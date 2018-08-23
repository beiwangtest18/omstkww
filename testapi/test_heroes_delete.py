# -*- coding: utf-8 -*-
#coding=utf-8
__author__ = 'Alicia'
import unittest
import requests
import os
import json
from urllib import urlencode
from conf import *

class Test_heroes_post(unittest.TestCase):
   def setUp(self):
       self.uri = '/heroes/'+CASES['deleteid']
       self.url = URL[env] +self.uri
       self.body = ''

   def tearDown(self):
       pass

   def test_heroes_post(self):
       params = {}
       urlencode(params)
       headers = {"Content-Type":"application/json"}
       resp = requests.request('DELETE', self.url, headers=headers, params=params)
       print resp.url
       print resp.status_code
       self.assertEqual(resp.status_code,200)

if __name__ == '__main__':
   unittest.main()
