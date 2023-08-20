# mukoyadariu-Phase-3-Week-1-Toy-Problems-
These repositories contain solutions to three Python coding problems. Each problem focuses on different aspects of Python programming and provides sample solutions along with usage instructions.

## Table of Contents

- [Problem 1: Count Positive and Sum Negative](#problem-1-count-positive-and-sum-negative)
- [Problem 2: Highest Value of Consonant Substrings](#problem-2-highest-value-of-consonant-substrings)
- [Problem 3: Extract Time and Format to 24-hour](#problem-3-extract-time-and-format-to-24-hour)

## Problem 1: Count Positive and Sum Negative

### Description

This problem involves counting positive numbers and summing negative numbers in a list of integers.

#### Usage
def count_positive_sum_negative(numbers):

# Test cases
numbers1 = [1, 2, 3, -4, -5, 6]
result1 = count_positive_sum_negative(numbers1)
print(result1)  # Output: (3, -9)


## Problem 2: Highest Value of Consonant Substrings

### Description

In this problem, you need to find the highest value of consonant substrings in a given lowercase string.

#### Usage
def solve(s):

# Test cases
result2_1 = solve("zodiacs")
result2_2 = solve("strength")
print(result2_1)  # Output: 26
print(result2_2)  # Output: 57


## Problem 3: Extract Time and Format to 24-hour

### Description

This problem involves extracting time components from a string, adjusting based on AM/PM, and formatting to 24-hour time.

#### Usage
def convert_to_24_hour_format(time_str):

# Test case
input_time = "7 Apr 2023 08:30:45 PM"
result3 = convert_to_24_hour_format(input_time)
print(result3)  # Output: "08:30:45"

## License

This repository is licensed under the [MIT License](LICENSE).


