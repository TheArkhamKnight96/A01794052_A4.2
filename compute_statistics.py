"""
Program created to read a file that is assumed to contain only numbers
"""
# filename: print_numbers.py
import sys
import time


class StatisticsArray(list):
    """
    Custom class which extends list
    and does required computation of it's elements
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_count = None
        self._mean = None
        self._median = None
        self._mode = None
        self._standard_deviation = None
        self._variance = None

    def set_original_count(self, _original_count):
        """
        Method used to calculate the mean
        of the elements that the class contains
        """
        self._original_count = _original_count

    def get_original_count(self):
        """
        Method used to get the mean of the class
        """
        return self._original_count

    def calculate_mean(self):
        """
        Method used to calculate the mean
        of the elements that the class contains
        """
        self._mean = sum(self) / len(self)

    def get_mean(self):
        """
        Method used to get the mean of the class
        """
        return self._mean

    def calculate_median(self):
        """
        Method used to calculate the median
        of the elements that the class contains
        """
        sorted_array = sorted(self)
        n = len(sorted_array)
        median = None

        if n % 2 == 0:
            # If the length of the array is even,
            # take the average of the middle two elements
            middle_left = sorted_array[n // 2 - 1]
            middle_right = sorted_array[n // 2]
            median = (middle_left + middle_right) / 2
        else:
            # If the length of the array is odd, return the middle element
            median = sorted_array[n // 2]

        self._median = median

    def get_median(self):
        """
        Method used to get the median of the class
        """
        return self._median

    def calculate_mode(self):
        """
        Method used to calculate the mode
        of the elements that the class contains
        """
        if not self:
            return "N/A"

        frequency = {}
        for num in self:
            frequency[num] = frequency.get(num, 0) + 1

        max_frequency = max(frequency.values())

        mode = [
            key for key, value in frequency.items() if value == max_frequency
        ]

        self._mode = "N/A" if len(mode) == len(frequency.values()) else mode[0]

    def get_mode(self):
        """
        Method used to get the mode of the class
        """
        return self._mode

    def calculate_standard_deviation(self):
        """
        Method used to calculate the standard deviation
        of the elements that the class contains
        """
        # Calculate mean
        mean = sum(self) / len(self)

        # Calculate squared differences from the mean
        squared_diff = [(x - mean) ** 2 for x in self]

        # Calculate variance
        variance = sum(squared_diff) / len(self)

        # Calculate standard deviation as the square root of the variance
        std_deviation = variance ** 0.5

        self._standard_deviation = std_deviation

    def get_standard_deviation(self):
        """
        Method used to get the standard deviation of the class
        """
        return self._standard_deviation

    def calculate_variance(self):
        """
        Method used to calculate the variance
        of the elements that the class contains
        """
        n = len(self)

        # Calculate the mean
        mean = sum(self) / n

        # Calculate the sum of squared differences
        sum_squared_diff = sum((x - mean) ** 2 for x in self)

        # Calculate the sample variance
        sample_variance = sum_squared_diff / (n - 1)

        self._variance = sample_variance

    def get_variance(self):
        """
        Method used to get the variance of the class
        """
        return self._variance

    def __str__(self):
        return (
            f"Statistics.\nCOUNT: {self.get_original_count()}\n"
            f"Mean: {self.get_mean()}\n"
            f"Median: {self.get_median()}\nMode: {self.get_mode()}\n"
            f"Standard deviation: {self.get_standard_deviation()}\n"
            f"Variance: {self.get_variance()}"
        )


def print_numbers(file_path):
    """
    Method to print the numbers that the file contains
    """
    try:
        start_time = time.time()
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        with open(file_path, 'r', encoding="utf-8") as file:
            # Read the numbers from the file and convert them to a list
            numbers = []
            for index, line in enumerate(file):
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(
                        f"Error: File contains non_numeric "
                        f"values in line {index+1}"
                    )

            custom_array = StatisticsArray(numbers)
            custom_array.set_original_count(len(lines))
            custom_array.calculate_mean()
            custom_array.calculate_median()
            custom_array.calculate_mode()
            custom_array.calculate_standard_deviation()
            custom_array.calculate_variance()
            end_time = time.time()
            elapsed_time_ms = (end_time - start_time) * 1000

            print(custom_array)
            print("\n")
            execution_time_result = (
                f"Time of execution: "
                f"{elapsed_time_ms:.6f} milliseconds"
            )
            print(execution_time_result)
            with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
                # Print the object to the file using the print function
                print(custom_array, file=file)
                print("\n", file=file)
                print(execution_time_result, file=file)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


if __name__ == "__main__":
    # Check if a file path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py P1/TC2.txt")
        sys.exit(1)

    # Get the file path from the command line argument
    path_to_file = sys.argv[1]

    # Print the numbers from the file
    print_numbers(path_to_file)
