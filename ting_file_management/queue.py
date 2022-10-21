class Queue:
    def __init__(self):
        self._file = list()

    def __len__(self):
        return len(self._file)

    def enqueue(self, value):
        self._file.append(value)

    def dequeue(self):
        value = self._file[0]
        del self._file[0]
        return value

    def search(self, index):
        lenght = self.__len__() - 1
        if lenght >= index and index >= 0:
            return self._file[index]

        raise IndexError
