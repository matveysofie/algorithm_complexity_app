
async def generate_linear_complexity():
    """
    Асинхронная функция, которая предоставляет код алгоритма линейной сложности
    """
    code = "def linear_search(arr, target):\n"
    code += "\tfor i in range(len(arr)):\n"
    code += "\t\tif arr[i] == target:\n"
    code += "\t\t\treturn i\n"
    code += "\treturn -1\n"
    return code


async def generate_binary_search():
    """
    Асинхронная функция, которая предоставляет код алгоритма бинарного поиска
    """
    code = "def binary_search(arr, target):\n"
    code += "\tleft, right = 0, len(arr) - 1\n"
    code += "\twhile left <= right:\n"
    code += "\t\tmid = (left + right) // 2\n"
    code += "\t\tif arr[mid] == target:\n"
    code += "\t\t\treturn mid\n"
    code += "\t\telif arr[mid] < target:\n"
    code += "\t\t\tleft = mid + 1\n"
    code += "\t\telse:\n"
    code += "\t\t\tright = mid - 1\n"
    code += "\treturn -1\n"
    return code


async def generate_bubble_sorting():
    """
    Асинхронная функция, которая предоставляет код сортировки пузырьком
    """
    code = "def bubble_sort(arr):\n"
    code += "\tfor i in range(len(arr) - 1):\n"
    code += "\t\tfor j in range(len(arr) - i - 1):\n"
    code += "\t\t\tif arr[j] > arr[j + 1]:\n"
    code += "\t\t\t\tarr[j], arr[j + 1] = arr[j + 1], arr[j]\n"
    code += "\treturn arr\n"
    return code


async def generate_merge_sorting():
    """
    Асинхронная функция, которая предоставляет код алгоритма сортировки слиянием
    """
    code = "def merge_sort(arr):\n"
    code += "\tif len(arr) > 1:\n"
    code += "\t\tmid = len(arr) // 2\n"
    code += "\t\tleft_half = arr[:mid]\n"
    code += "\t\tright_half = arr[mid:]\n"
    code += "\t\tmerge_sort(left_half)\n"
    code += "\t\tmerge_sort(right_half)\n"
    code += "\t\ti = j = k = 0\n"
    code += "\t\twhile i < len(left_half) and j < len(right_half):\n"
    code += "\t\t\tif left_half[i] < right_half[j]:\n"
    code += "\t\t\t\tarr[k] = left_half[i]\n"
    code += "\t\t\t\ti += 1\n"
    code += "\t\t\telse:\n"
    code += "\t\t\t\tarr[k] = right_half[j]\n"
    code += "\t\t\t\tj += 1\n"
    code += "\t\t\tk += 1\n"
    code += "\t\twhile i < len(left_half):\n"
    code += "\t\t\tarr[k] = left_half[i]\n"
    code += "\t\t\ti += 1\n"
    code += "\t\t\tk += 1\n"
    code += "\t\twhile j < len(right_half):\n"
    code += "\t\t\tarr[k] = right_half[j]\n"
    code += "\t\t\tj += 1\n"
    code += "\t\t\tk += 1\n"
    code += "\treturn arr\n"

    return code


async def generate_exponential_complexity():
    """
    Асинхронная функция, которая предоставляет код экспоненциального алгоритма
    """
    code = "def exponential_search(arr, target):\n"
    code += "\tif arr[0] == target:\n"
    code += "\t\treturn 0\n"
    code += "\tpos = 1\n"
    code += "\twhile pos < len(arr) and arr[pos] <= target:\n"
    code += "\t\tpos = pos * 2\n"
    code += "\tleft, right = pos // 2, min(pos, len(arr))\n"
    code += "\twhile left < right:\n"
    code += "\t\tmid = (left + right) // 2\n"
    code += "\t\tif arr[mid] == target:\n"
    code += "\t\t\treturn mid\n"
    code += "\t\telif arr[mid] < target:\n"
    code += "\t\t\tleft = mid + 1\n"
    code += "\t\telse:\n"
    code += "\t\t\tright = mid\n"
    code += "\treturn -1\n"
    return code


async def generate_factorial_complexity():
    """
    Асинхронная функция, которая предоставляет код алгоритма факториальной сложности
    """
    code = "def factorial(n):\n"
    code += "\tif n == 0 or n == 1:\n"
    code += "\t\treturn 1\n"
    code += "\telse:\n"
    code += "\t\treturn n * factorial(n-1)\n"
    return code
