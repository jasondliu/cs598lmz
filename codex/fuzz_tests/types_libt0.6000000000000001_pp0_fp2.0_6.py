import types
types.ClassType

import sys, os
sys.path.append(os.getcwd() + '/../../../')
from common.config import Config
from common.logger import Logger

class Test_Survey_Add(unittest.TestCase):
    u"""Test_Survey_Add"""
    def setUp(self):
        self.logger = Logger()
        self.logger.info('########################### TestSurveyAdd START ###########################')
        config = Config()
        self.url = config.get('BaseUrl')
        self.logger.info('url:%s' % self.url)

    def tearDown(self):
        self.logger.info('############################ TestSurveyAdd END ############################')

    def test_survey_add(self):
        u"""测试"""
        data = {
            'name': 'survey_add_test_%s' % int(time.time()),
            'description': 'survey_add_test_%s' % int(time.time()),
           
