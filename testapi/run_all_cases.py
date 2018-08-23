# -*- coding: utf-8 -*-
#coding=utf-8
__author__ = 'Alicia'
import unittest
import os
import time
import HTMLTestRunner
from conf import *

case_path = os.path.join(os.getcwd())
report_path = os.path.join(os.getcwd(),'reports')

def all_cases():
  discovery = unittest.defaultTestLoader.discover('.','test*.py', top_level_dir=None)
  print "allcases:"+case_path
  print discovery
  return discovery

if __name__ == '__main__':
  now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
  report_abspath = os.path.join(report_path, "APITestResult_"+now+".html")
  print report_abspath
  fp = file(report_abspath, "wb")
  suite = unittest.TestSuite()
  [suite.addTest(case) for case in all_cases()]
  runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='API test Report', description='Results:', verbosity=2)
  runner.run(suite)
  fp.close()
