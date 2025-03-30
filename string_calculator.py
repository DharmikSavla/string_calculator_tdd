import re

THRESHOLD = 1000


class StringCalculator:

    def __init__(self, num_string: str):
        self.num_string = num_string

    def add(self) -> int:
        """This method takes string and returns the sum of the string seperated by delimiters"""
        try:
            num_string = self.num_string

            if not num_string:
                return 0

            default_delimiters = [",", "\n"]
            delimiters = "|".join(default_delimiters)
            num_list = (
                num_string
                if len(num_string) <= 1
                else re.split(f"\n|{delimiters}", num_string)
            )

            total = 0
            negatives = []
            for num_str in num_list:
                num = int(num_str)
                if num < 0:
                    negatives.append(num_str)
                elif num <= THRESHOLD:
                    total += num

            if negatives:
                raise Exception(f"""Negatives not allowed: {",".join(negatives)}""")

            return total
        except Exception as e:
            error = str(e)
            if "invalid literal" in error:
                return "Please provide valid test case"

            return error
