# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.


url_list = ['https://www.pythonanywhere.com/g2g451b4h',
            'https://www.python.org/51gh1g1', 'https://www.cyberforum.ru/4fg5h1f18']


domen_list = list(map(lambda i: i[:i.find(
    '/')], [i for i in map(lambda i: i.replace('https://', ''), url_list)]))
print(domen_list)