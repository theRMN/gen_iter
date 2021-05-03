import inspect
from datetime import datetime


def path_to_log(path):
    def make_log(old_function):
        def new_function():
            text = old_function
            log = str(f'{old_function.__name__}: {datetime.now(tz=None)} | {inspect.getfullargspec(old_function)}')
            with open(path, 'a', encoding='utf-8') as f:
                f.write(log + '\n')
            return text
        return new_function()
    return make_log


@path_to_log('log.txt')
def test_function(text):
    return print(text)


test_function('Hello')
