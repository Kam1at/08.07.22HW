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

    def __len__(self):
        return len(self.content)

    def __bool__(self):
        return bool(len(self.content))

class TodoList:
    def __init__(self):
        self.tasks = []

    def __setitem__(self, key, value):
        self.tasks[key] = value

    def __getitem__(self, item):
        return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __repr__(self):
        return f"{self.__keys()}"




todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')
print(todo_list)
# [Сдать домашку (создано 2022-12-08 12:34:33), Выпить кофе (создано 2022-12-08 12:34:33)]

print(todo_list[0])
# Сдать домашку (создано 2022-12-08 12:34:33)

del todo_list[0]
print(todo_list)
# [Выпить кофе (создано 2022-12-08 12:34:33)]