import unittest
import pycoinmon as pcm

class TestPycoinmon(unittest.TestCase):
    def test_create(self):
        print("--test create--")
        self.assertEqual("r","r")

if __name__ == '__main__':
    unittest.main()
