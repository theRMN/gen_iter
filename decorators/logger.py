from datetime import datetime
import inspect
import itertools


def path_to_log(path):
    def make_log(old_function):
        def new_function(*args, **kwargs):

            result = old_function(*args, **kwargs)

            log = str(f'{old_function.__name__}: {datetime.now(tz=None)} | {args, kwargs} | {result}')
            with open(path, 'a', encoding='utf-8') as f:
                f.write(log + '\n')

            return result
        return new_function
    return make_log


@path_to_log('log.txt')
def foo(text):
    text = text + ', world'
    return text


foo('Hello')
