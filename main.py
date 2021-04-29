import json
from hashlib import md5


class URLmaker:
    def __init__(self, path, count: int):
        self.path = path
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        b_url = 'https://en.wikipedia.org/wiki/'
        with open(self.path) as f:
            file = json.load(f)
            try:
                name = file[self.count]['name']['common'].replace(' ', '_').replace(',', '')
                result = f'{name}: {b_url}{name}'
                self.count += 1
                with open('result.txt', 'a', encoding='utf-8') as r:
                    r.write(result + '\n')
            except IndexError:
                raise StopIteration
        return result


# for i in URLmaker('countries.json', 0):
#     print(i)


def line_hash(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '')
            line = md5(line.encode()).hexdigest()
            yield line


for i in line_hash('result.txt'):
    print(i)
