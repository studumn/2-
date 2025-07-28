from datetime import datetime as dt

def check_time(func):
    def wrapper():
        time_now = dt.now()
        print(f'Функция была вызвана {time_now.day}.{time_now.month}.{time_now.year} в {time_now.hour}:{time_now.minute}:{time_now.second}')
    func()
    return wrapper

@check_time
def hello_world():
    print("hello world")

hello_world()
