import json
import re
import random
import unicodedata

from funkload.FunkLoadTestCase import FunkLoadTestCase


data =  [
        ('63.245.217.20', {"success": {"city": "Mountain View",
    "continent_code": "NA", "region": "CA", "charset": 0, "area_code": 650,
    "longitude": -122.0740966796875, "country_code3": "USA", "latitude":
    37.38850021362305, "postal_code": "94041", "dma_code": 807, "country_code":
    "US", "country_name": "United States"}})
        ]



class GeoIPTest(FunkLoadTestCase):

    def __init__(self, *args, **kwargs):
        super(GeoIPTest, self).__init__(*args, **kwargs)
        self.root = self.conf_get('main', 'url')

    def test_geoip(self):
        """Control the data sent back by the server"""
        for ip, wanted in data:
            res = self.get(self.root + '/%s' % ip)
            content = json.loads(res.body)
            res = content['success']
            res = res.items()
            res.sort()
            wanted = wanted['success'].items()
            wanted.sort()
            self.assertEquals(res, wanted)



if __name__ == '__main__':
    import unittest
    unittest.main()
