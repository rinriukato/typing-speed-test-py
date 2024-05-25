from typing import List
from random import choice

with open('words.txt', 'r') as file:
    word_bank = file.readlines()


def create_random_typing_test() -> List[str]:
    typing_test_list = []
    for i in range(500):
        word = choice(word_bank)
        word = word.replace('\n', '')
        typing_test_list.append(word)

    return typing_test_list
