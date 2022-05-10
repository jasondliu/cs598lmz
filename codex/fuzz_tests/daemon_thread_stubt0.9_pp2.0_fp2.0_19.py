import sys, threading

def run():
    server.serve_forever()

def get_vacancies(keyword, city):
    ''' Возвращает словарь с основными данными о вакансиях и количество вакансий '''
    hh = hh_api.HHApi()
    vacancies = hh.vacancies(keyword, city)
    collection = db['vacancies']
    new_vacancies_count = 0
    new_vacancies = []
    # Отсекаем дублирующиеся вакансии и записываем в базу только новые
    for vacancy in vacancies:
        result = collection.find_one
