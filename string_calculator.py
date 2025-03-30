import re


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

            total = sum(int(num) for num in num_list)

            return total
        except Exception as e:
            error = str(e)
            if "invalid literal" in error:
                return "Please provide valid test case"

            return error
