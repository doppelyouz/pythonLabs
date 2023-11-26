import random
from collections import Counter

def read_and_display(file_path):
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())


def read_random_line(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        print(random.choice(lines).strip())


def count_uppercase(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            count += sum(1 for char in line if char.isupper())
    return count


def count_lines_not_start_with_d(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            if not line.startswith("D"):
                count += 1
    return count


def count_words_ending_with_f(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            count += sum(1 for word in line.split() if word.lower().endswith("f"))
    return count


def count_specific_words(file_path):
    count_all, count_none = 0, 0
    with open(file_path, "r") as file:
        for line in file:
            words = line.lower().split()
            count_all += words.count("all")
            count_none += words.count("none")
    return count_all, count_none


def word_frequency(file_path):
    with open(file_path, "r") as file:
        words = file.read().split()
        return Counter(words)


def find_longest_word(file_path):
    longest_word = ""
    with open(file_path, "r") as file:
        for line in file:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word


def correct_content(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        corrected_content = content.replace("B", "J").replace("b", "j")
        print(corrected_content)


def count_a_b(file_path):
    count_a, count_b = 0, 0
    with open(file_path, "r") as file:
        for char in file.read().lower():
            if char == "a":
                count_a += 1
            elif char == "b":
                count_b += 1
    return count_a, count_b


read_and_display("text.txt")