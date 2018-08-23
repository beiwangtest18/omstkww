# -*- coding: utf-8 -*-
#coding=utf-8
__author__ = 'Alicia'
import unittest
import requests
#import urllib
import os
import json
from urllib import urlencode
from conf import *

class Test_heroes_get_all(unittest.TestCase):
   def setUp(self):
       self.uri = '/heroes'
       self.url = URL[env] +self.uri
       self.body = ''

   def tearDown(self):
       pass

   def test_heroes_get_all(self):
       params = {}
       urlencode(params)
       #httpcode = urllib.urlopen(self.url).getcode()
       #print httpcode
       #self.assertEqual(httpcode,200)
       resp = requests.request('GET', self.url, params=params)
       print resp.url
       print resp.status_code
       rj = json.loads(resp.content)
       print resp.content
       self.assertEqual(resp.status_code,200)

if __name__ == '__main__':
   unittest.main()
