from nose2.tools import params
import unittest

class Layer(object):
    @classmethod
    def setUp(cls):
        print("set up test fixtures")
    @classmethod
    def testTearDown(cls):
        print("tear down test fixtures")

        
class TestExample(unittest.TestCase):

    layer = Layer

    @params("Red apple", "Yellow banana", "Green Guava")
    def test_is_red(self,value):
        self.assertTrue(value.startswith('Red'))

if __name__ == '__main__':
    unittest.main()

