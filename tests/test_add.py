import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    # unittest fixtures
    def setUp(self):
        print("set up test fixtures")
        self.x = 2

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
    
    def test_add2(self):
        self.assertEqual(add(self.x + 2, 4), 8)
    
    def test_add3(self):
        self.assertEqual(add(self.x + self.x, 4), 8)

if __name__ == '__main__':
    unittest.main()