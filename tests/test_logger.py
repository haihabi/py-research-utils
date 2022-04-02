import unittest
import pyresearchutils as pru


class TestLogger(unittest.TestCase):
    def test_something(self):
        pru.logger.print("Start Logger")
        print(pru.logger.get_log_file())
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
