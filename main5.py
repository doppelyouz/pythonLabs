
#task1
def get_keys_with_value_true(input_dict):
    return [key for key, value in input_dict.items() if value == True]

input_dict = {
    "a": True,
    "b": False,
    "c": True,
}
result = get_keys_with_value_true(input_dict)
print(result)

#task2
def get_unique_elements(input_list):
    unique_elements = []
    seen_elements = set()

    for num in input_list:
        if input_list.count(num) == 1 and num not in seen_elements:
            unique_elements.append(num)
            seen_elements.add(num)

    return unique_elements

input_list = [1, 2, 3, 1, 2, 4]
result = get_unique_elements(input_list)
print(result)

#task3
def get_date_in_format(date):
    parts = date.split('.')
    day = parts[2]
    month = parts[1]
    year = parts[0]

    formatted_date = f'{day}.{month}.{year}'

    return formatted_date

input_date = '2023.10.23'
result = get_date_in_format(input_date)
print(result)

#task4
def get_elements_with_no_more_than_two_occurrences(input_list):
    result = []
    count_dict = {}

    for num in input_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count <= 2:
            result.append(num)

    return result

input_list = [1, 2, 3, 1, 2, 4, 1, 2]
result = get_elements_with_no_more_than_two_occurrences(input_list)
print(result)

#task5
def get_words_from_string(input_string):

    words = input_string.split()
    return words

input_string = "This a string with a several words."
result = get_words_from_string(input_string)
print(result)

#task6
def get_unique_elements_with_count(input_list):
    element_count = {} 

    for num in input_list:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    return element_count

input_list = [1, 2, 3, 1, 2, 4, 1, 2]
result = get_unique_elements_with_count(input_list)
print(result)

#task7
def get_prime_numbers(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for current_num in range(2, int(n**0.5) + 1):
        if is_prime[current_num]:
            for multiple in range(current_num * current_num, n + 1, current_num):
                is_prime[multiple] = False

    prime_numbers = [num for num in range(2, n + 1) if is_prime[num]]
    return prime_numbers

n = 100
result = get_prime_numbers(n)
print(result)

#task8
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers_in_list(input_list):
    prime_numbers = [num for num in input_list if is_prime(num)]
    return prime_numbers

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
result = get_prime_numbers_in_list(input_list)
print(result)

#task9
from datetime import datetime

def get_difference_between_dates(date1, date2):
    date1_obj = datetime.strptime(date1, '%Y.%m.%d')
    date2_obj = datetime.strptime(date2, '%Y.%m.%d')

    date_difference = abs(date2_obj - date1_obj).days

    return date_difference

date1 = '2023.10.20'
date2 = '2023.10.24'
result = get_difference_between_dates(date1, date2)
print(result)

#task10
def get_decimal_number_from_binary_string(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number

binary_string = "10110011"
result = get_decimal_number_from_binary_string(binary_string)
print(result)

#task11

def is_expression_true(expression):
    try:
        result = eval(expression)
        return result
    except SyntaxError:
        return False

expression = "True and False or True"
result = is_expression_true(expression)
print(result)

#task12

def sort_by_price(shopping_list):
    sorted_list = sorted(shopping_list, key=lambda x: x['price'])
    return sorted_list

shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]
result = sort_by_price(shopping_list)
print(result)

#task13
def get_words_starting_with_vowel(words):
    vowels = 'aeiouAEIOU'
    vowel_words = [word for word in words if word[0] in vowels]
    return vowel_words

words = ["apple", "banana", "orange", "bear", "cat"]
result = get_words_starting_with_vowel(words)
print(result)
