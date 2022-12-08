import datetime

class Task:

    def __init__(self, content):
        self.content = content
        self.date = datetime.datetime.now().replace(microsecond=0)

    def __keys(self):
        return f"{self.content} (создано {str(self.date)})"

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.__keys() == other.__keys()
        return NotImplemented

    def __hash__(self):
        return hash(self.__keys())

    def __repr__(self):
        return f"{self.__keys()}"



todo_list = set()

todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))

for item in todo_list:
    print(item)
