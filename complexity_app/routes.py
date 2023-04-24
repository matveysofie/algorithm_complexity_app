import json

from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

from complexity_app.services.generate_code import generate_linear_complexity, generate_binary_search, \
    generate_bubble_sorting, generate_merge_sorting, generate_exponential_complexity, generate_factorial_complexity

from complexity_app.settings import get_settings

settings = get_settings()

router = APIRouter()


# @router.get("/algorithm/{complexity}")
# async def get_algorithm(complexity: Complexity):
#     algorithms = [
#         Algorithm(name="Линейная сложность",
#                   description="Алгоритм поиска, который последовательно проверяет каждый элемент списка до тех пор, пока не будет найдено совпадение.",
#                   complexity=complexity.linear_complexity,
#                   code_example=""),
#         Algorithm(name="Бинарный поиск",
#                   description="Алгоритм поиска, который работает с отсортированным списком путем многократного деления интервала поиска пополам.",
#                   complexity=complexity.binary_search,
#                   code_example=""),
#         Algorithm(name="Сортировка пузырьком",
#                   description="Простой алгоритм сортировки, который многократно проходит по списку, сравнивает соседние элементы и меняет их местами, если они расположены в неправильном порядке.",
#                   complexity=complexity.bubble_sorting,
#                   code_example=""),
#         Algorithm(name="Сортировка слиянием",
#                   description="Алгоритм сортировки, который делит несортированный список на n подсписков, каждый из которых содержит 1 элемент, а затем многократно объединяет подсписки для создания новых отсортированных подсписков, пока не останется только 1 подсписк.",
#                   complexity=complexity.merge_sorting,
#                   code_example=""),
#         Algorithm(name="Константная сложность",
#                   description="Алгоритм с постоянной сложностью, который выполняет одну операцию независимо от размера входных данных.",
#                   complexity=complexity.constant_complexity,
#                   code_example=""),
#         Algorithm(name="Экспоненциальная сложность",
#                   description="Алгоритм со сложностью O(2^n), который решает задачи за экспоненциальное время и быстро становится непрактичным при увеличении размера входных данных.",
#                   complexity=complexity.exponential_complexity,
#                   code_example=""),
#         Algorithm(name="Факториальная сложность",
#                   description="Алгоритм со сложностью O(n!), который быстро становится непрактичным при увеличении размера входных данных.",
#                   complexity=complexity.factorial_complexity,
#                   code_example="")
#     ]
#     for algorithm in algorithms:
#         if algorithm.complexity == complexity:
#             return algorithm
#     raise HTTPException(status_code=404, detail="Алгоритм не найден")


@router.get("/linear_complexity", response_class=PlainTextResponse)
async def get_linear_complexity():
    """
    O(n) - линейная сложность, время выполнения алгоритма прямо пропорционально размеру входных данных.
    """
    return await generate_linear_complexity()


@router.get("/binary_search", response_class=PlainTextResponse)
async def get_binary_search():
    """
    O(log n) - логарифмическая сложность, время выполнения алгоритма увеличивается логарифмически с размером входных данных.
    """
    return await generate_binary_search()


@router.get("/bubble_sorting", response_class=PlainTextResponse)
async def get_bubble_sorting():
    """
     O(n log n) - сложность «быстрого» сортировочного алгоритма, например, быстрой сортировки.
    """
    return await generate_bubble_sorting()


@router.get("/merge_sorting", response_class=PlainTextResponse)
async def get_merge_sorting():
    """
    O(n^2) - квадратичная сложность, время выполнения алгоритма увеличивается квадратично с размером входных данных.
    """
    return await generate_merge_sorting()


@router.get("/exponential_complexity", response_class=PlainTextResponse)
async def get_exponential_complexity():
    """
    O(2^n) - экспоненциальная сложность, время выполнения алгоритма увеличивается экспоненциально с размером входных данных.
    """
    return await generate_exponential_complexity()


@router.get("/factorial_complexity", response_class=PlainTextResponse)
async def get_factorial_complexity():
    """
    O(n!) - факториальная сложность, время выполнения алгоритма увеличивается факториально с размером входных данных.
    Факториальная сложность возникает, когда алгоритм имеет вложенные циклы, в которых каждый следующий цикл выполняется на один раз меньше, чем предыдущий. Примером алгоритма с факториальной сложностью может служить перебор всех перестановок множества элементов.
    Использование алгоритма факториальной сложности не рекомендуется для больших входных данных.
    """
    return await generate_factorial_complexity()
