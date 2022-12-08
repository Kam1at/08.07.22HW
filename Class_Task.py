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



todo_list = []

todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))

non_empty_tasks = [item for item in todo_list if item]
print(non_empty_tasks)
# [Сделать домашку (создано 2022-12-08 12:21:16), Сделать домашку (создано 2022-12-08 12:21:16)]

print(len([item for item in todo_list if not item]))
# 2
