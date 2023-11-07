# 27) в id есть хотя бы одна нечётная цифра, в логине не меньше двух гласных,
# в пароле не меньше 3 цифр и хотя бы одна маленькая буква
import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits


def random_id():
    odd_digits = "13579"
    even_digits = "02468"

    while True:
        id_result = random.choices(odd_digits + even_digits, k=4)
        id_result.append(random.choice(odd_digits))

        random.shuffle(id_result)

        if id_result[0] != '0':
            return int(''.join(id_result))


def random_login():
    vowels = "aeiou"
    login_result = random.choices(vowels, k=2)
    login_result += random.choices(ascii_lowercase, k=4)
    random.shuffle(login_result)
    return ''.join(login_result)


def random_password():
    lowercase_letter = random.choice(ascii_lowercase)
    three_digits = random.choices(digits, k=3)
    password_result = random.choices(ascii_lowercase + ascii_uppercase, k=6) + three_digits
    password_result.append(lowercase_letter)

    random.shuffle(password_result)
    return ''.join(password_result)


def generate_collection(number_of_iteration):
    generated_ids = set()
    generated_logins = set()
    generated_passwords = set()

    while len(generated_ids) < number_of_iteration:
        generated_ids.add(random_id())
    while len(generated_logins) < number_of_iteration:
        generated_logins.add(random_login())
    while len(generated_passwords) < number_of_iteration:
        generated_passwords.add(random_password())
    return [[random_id(), random_login(), random_password()] for _ in range(number_of_iteration)]


n = int(input())
result_collection = generate_collection(n)
for row in result_collection:
    print(*row)