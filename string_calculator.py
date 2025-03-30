import re

THRESHOLD = 1000


class StringCalculator:

    def __init__(self, num_string: str):
        self.num_string = num_string

    def add(self) -> int:
        """This method takes string and returns the sum of the string separated by delimiters"""
        try:
            num_string = self.num_string
            delimiter_scope = []

            if not num_string:
                return 0

            if "//" in num_string:
                # Dividing delimiters and numbers from the main list
                saperator = num_string.split("\n")
                numbers = len(saperator[0]) + 1
                num_string = num_string[numbers:]
                delimiter_scope = saperator[0][2:]

                # Replacing brackets with commas for easy separation of list
                delimiter_scope = (
                    delimiter_scope.replace("][", ",")
                    .replace("*", "\*")
                    .replace("[", "")
                    .replace("]", "")
                )

                delimiter_scope = delimiter_scope.split(",")

            # Creating a regex string of delimiters
            default_delimiters = [",", "\n", *delimiter_scope]
            delimiters = "|".join(default_delimiters)

            # Filtering out delimiters and generating a list of numeric strings
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
