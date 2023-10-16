#1
user_input = input("Введите строку с пробелами: ")
user_input = user_input.lower()
char_list = list(user_input)

print("Созданный список:")
print(char_list)

#2

user_input = input("Введите строку с пробелами: ")
user_input = user_input.lower()

char_count = {}
for char in user_input:
    if char != ' ': 
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

result = list(char_count.items())

print("Результат:")
print(result)

#3

user_input = input("Enter a string with whitespaces: ")

char_list = []

for char in user_input:
    char_list.append(char.lower())

print("Created list is:")
print(char_list)

char_frequency = {}

for char in char_list:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_list = [(char, count) for char, count in char_frequency.items()]

char_frequency_list.sort()

print(char_frequency_list)

list_vow = []
list_cons = []
list_sym = []

def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

for char, count in char_frequency_list:
    if is_vowel(char):
        list_vow.append((char, count))
    elif char.isalpha():
        list_cons.append((char, count))
    else:
        list_sym.append((char, count))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)

#4

list_A = input()

sorted_list_A = sorted(list_A)

length = len(sorted_list_A)
q1_index = length // 4
q2_index = q1_index * 2
q3_index = q1_index * 3

q1 = sorted_list_A[:q1_index]
q2 = sorted_list_A[q1_index:q2_index]
q3 = sorted_list_A[q2_index:q3_index]
q4 = sorted_list_A[q3_index:]

print("q1 =", q1)
print("q2 =", q2)
print("q3 =", q3)
print("q4 =", q4)

#5

name = input("Имя студента: ")
assignments = input("Баллы за задания: ").split(',')
labs = input("Баллы за лабораторные работы: ").split(',')
tests = input("Баллы за тесты: ").split(',')

assignments = [int(x.strip()) for x in assignments]
labs = [float(x.strip()) for x in labs]
tests = [int(x.strip()) for x in tests]

student = {'имя': name, 'назначение': assignments, 'тест': tests, 'лаборатория': labs}

print("student =", student)

#6
student = {'имя': 'Адам', 'назначение': [82, 56, 44, 30], 'тест': [78, 77], 'лаборатория': [78.2, 77.2]}

if len(student.get('назначение', [])) == 4 and len(student.get('тест', [])) == 2 and len(student.get('лаборатория', [])) == 2:
    submission_check = {student['имя']: 6}
else:
    submission_check = {student['имя']: 0}


print(submission_check)
нн

#7
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
submission_rate = {'Adam': 6}

if submission_rate.get(student['name'], 0) >= 4:
    assignment_avg = sum(student['assignment']) / len(student['assignment']) if student['assignment'] else 0
    test_avg = sum(student['test']) / len(student['test']) if student['test'] else 0
    lab_avg = sum(student['lab']) / len(student['lab']) if student['lab'] else 0

    final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
    student['final_grade'] = round(final_grade, 2)
else:
    student['final_grade'] = 0

print(student)

#8
student1 = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}

students = {student1['name']: {key: value for key, value in student1.items() if key != 'name'},
            student2['name']: {key: value for key, value in student2.items() if key != 'name'}}

print(students)

#9
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

stats = {}

for user_id, transaction_type in transactions:
    if user_id not in stats:
        stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}

    stats[user_id][transaction_type] += 1

for user_id, user_stats in stats.items():
    most_frequent = max(user_stats, key=lambda key: user_stats[key] if isinstance(key, int) else 0)
    least_frequent = min(user_stats, key=lambda key: user_stats[key] if isinstance(key, int) else 0)
    user_stats['mft'] = most_frequent
    user_stats['lft'] = least_frequent

print("stats =", stats)
