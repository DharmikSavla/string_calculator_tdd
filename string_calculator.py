import re

THRESHOLD = 1000
DEFAULT_DELIMITERS = [",", "\n"]
REG_CONDITIONS = [
    {"old": "][", "new": ","},
    {"old": "*", "new": "\*"},
    {"old": "["},
    {"old": "]"},
]


class StringCalculator:

    def __init__(self, num_string: str):
        self.num_string = num_string

    @staticmethod
    def replace(string: str, conditions: list[dict]) -> str:
        for item in conditions:
            string = string.replace(item["old"], item.get("new", ""))

        return string

    @staticmethod
    def __compute_numeric_string(num_list: list) -> int:
        total = 0
        negatives = []
        for num_str in num_list:
            num = int(num_str)
            if num < 0:
                negatives.append(num_str)
            elif num <= THRESHOLD:
                total += num

        return total, negatives

    def __extract_delimiter(self):
        """Returns delimiters used for string separation"""

        num_string = self.num_string
        delimiter_scope = []

        if "//" in num_string:
            # Dividing delimiters and numbers from the main list
            separator = num_string.split("\n")
            numbers = len(separator[0]) + 1
            num_string = num_string[numbers:]
            delimiter_scope = separator[0][2:]

            # Replacing brackets with commas for easy separation of list
            delimiter_scope = self.replace(
                string=delimiter_scope, conditions=REG_CONDITIONS
            )

            delimiter_scope = delimiter_scope.split(",")

        # Creating a regex string of delimiters
        delimiters = "|".join([*DEFAULT_DELIMITERS, *delimiter_scope])

        return delimiters, num_string

    def add(self) -> int:
        """This method takes string and returns the sum of the string separated by delimiters"""
        try:
            num_string = self.num_string

            if not num_string:
                return 0

            delimiters, num_string = self.__extract_delimiter()

            # Filtering out delimiters and generating a list of numeric strings
            num_list = re.split(f"\n|{delimiters}", num_string)

            total, negatives = self.__compute_numeric_string(num_list=num_list)

            if negatives:
                raise Exception(f"""Negatives not allowed: {",".join(negatives)}""")

            return total
        except Exception as e:
            error = str(e)
            if "invalid literal" in error:
                error = "Please provide valid test case"

            return error
