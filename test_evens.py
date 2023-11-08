import unittest
# Import function into test file
from evens import even_number_of_evens

# Create a test case
#Create a class which needs to inherit from the unittest.TestCase class
class TestEvens(unittest.TestCase):
    # the pass statement allows the code to run error free when you have no code
    #pass

    # A basic test that tests whether our function returns True. It will be a method and needs to start with the word "test"
    # def test_function_returns_True(self):
    #     self.assertTrue(even_number_of_evens([]))

    # This will call the assertRaises method frorm TestCase and when the test is run it checks to see if a TypeError
    # is raised when the function is called with the value of 4
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)

if __name__ == '__main__':
    unittest.main()
