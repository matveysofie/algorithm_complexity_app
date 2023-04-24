from enum import Enum


class Complexity(str, Enum):
    linear_complexity = "O(n)"
    binary_search = "O(log n)"
    bubble_sorting = "O(n log n)"
    merge_sorting = "O(n^2)"
    constant_complexity = "O(1)"
    exponential_complexity = "O(2^n)"
    factorial_complexity = "O(n!)"
