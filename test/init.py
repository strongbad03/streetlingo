import unittest
from src.etl.etl import *


class TestLID(unittest.TestCase):

    def test_chinese(self):
        sample = '影響包含對氣候的變化以及自然資源的枯竭程度'
        t = ('zh', 'zho', 'Chinese')
        self.assertEqual(lid_text(sample), t)


if __name__ == '__main__':
    unittest.main()
