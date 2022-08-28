#`load_candidates()`, которая загрузит данные из файла

#`get_all()`, которая покажет всех кандидатов

#`get_by_pk(pk)`, которая вернет кандидата по pk

#`get_by_skill(skill_name)`, которая вернет кандидатов по навыку
import json

from candidate import Candidate

"""Pагружает данные из файла"""


def load_candidates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


"""Показывает всех кандидатов"""


def get_all(data):
    arr = []
    for item in data:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        arr.append(candidate)
    return arr


"""Возвращает кандидата по pk"""


def get_by_pk(pk, data):
    for item in data:
        if item.pk == pk:
            return pk


"""Возвращает кандидатов по навыку"""


def get_by_skill(skill_name, data):
    arr = []
    for item in data:
        if skill_name in item.skills:
            arr.append(item)
    return arr


print(get_all(load_candidates('candidates.json')))

