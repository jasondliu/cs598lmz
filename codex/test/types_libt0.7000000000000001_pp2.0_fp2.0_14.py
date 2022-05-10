import types
types.NoneType = None

import json
import unittest
import requests

import config
from test_utils import get_test_cases


class TestCreate(unittest.TestCase):
    def test_create(self):
        test_cases = get_test_cases('tests/tests_create.json')
        for test_case in test_cases:
            result = requests.post(
                config.API_HOST + '/' + test_case['endpoint'],
                json=test_case['body'],
                headers={'Authorization': 'Token ' + config.TOKEN},
            )
            self.assertEqual(result.status_code, test_case['status_code'])
            if result.status_code == 201:
                result_data = json.loads(result.text)
                for key in test_case['keys']:
                    self.assertTrue(key in result_data)
                endpoint = test_case['endpoint'].split('/')[-1]
