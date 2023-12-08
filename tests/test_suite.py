import unittest

def add(a, b):
    return a + b

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)

    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-1, 1), 0)

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStringMethods))
    suite.addTest(TestAdd('test_add'))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(load_tests)

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(TestStringMethods))
#     suite.addTest(TestAdd('test_add'))
#     unittest.TextTestRunner(verbosity=2).run(suite)

# If load_tests exists then discovery does not recurse into the package, 
# load_tests is responsible for loading all tests in the package.
# https://stackoverflow.com/questions/53399258/how-to-use-unittest-testsuite-in-vs-code
