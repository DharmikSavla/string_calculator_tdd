import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    """
    Test the string_calculator module
    """

    def test_happy_path(self):
        """
        The method can take up to two numbers, separated by commas, and will return their sum and for an empty string return 0.
        In test_case, input is the test string and output is the expected outcome.
        """
        test_cases = [
            {"input": "", "output": 0},
            {"input": "1", "output": 1},
            {"input": "1,2", "output": 3},
        ]
        for test_case in test_cases:
            string_calculator = StringCalculator(num_string=test_case["input"])
            result = string_calculator.add()

            self.assertEqual(result, test_case["output"])

    def test_new_lines(self):
        """
        Test the new lines between numbers (instead of commas) and also invalid test case exception handling.
        """
        test_cases = [
            {"input": "1\n2,3", "output": 6},
            {
                "input": "1,\n",  # Invalid test case
                "output": "Please provide valid test case",
            },
        ]
        for test_case in test_cases:
            string_calculator = StringCalculator(num_string=test_case["input"])
            result = string_calculator.add()

            self.assertEqual(result, test_case["output"])

    def test_negative_exception(self):
        """
        Calling add method with a negative number will throw an exception
        """
        test_cases = [
            {"input": "-1\n2,-3,4,5,6,-7", "output": "Negatives not allowed: -1,-3,-7"},
            {"input": "1,3,4,-5,6,7", "output": "Negatives not allowed: -5"},
        ]
        for test_case in test_cases:
            string_calculator = StringCalculator(num_string=test_case["input"])
            result = string_calculator.add()

            self.assertEqual(result, test_case["output"])

    def test_threshold_number(self):
        """
        Numbers bigger than 1000 should be ignored
        """
        test_cases = [
            {"input": "2,1001", "output": 2},
            {"input": "1001,1002,2000", "output": 0},
            {"input": "5\n1000,2,1009", "output": 1007},
        ]
        for test_case in test_cases:
            string_calculator = StringCalculator(num_string=test_case["input"])
            result = string_calculator.add()

            self.assertEqual(result, test_case["output"])


if __name__ == "__main__":
    unittest.main()
