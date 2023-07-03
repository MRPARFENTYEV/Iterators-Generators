'''Доработать функцию flat_generator. Должен получиться генератор,
который принимает список списков и возвращает их плоское представление.
Функция test в коде ниже также должна отработать без ошибок.'''
import types
class FlatIterator:

    def __init__(self, list_of_list):
        self.items = sum(list_of_list, [])
        self.items_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.items_counter != len(self.items):
            item = self.items[self.items_counter]
            # print(self.items[self.items_counter])
            self.items_counter += 1

            return item
        else:
            raise StopIteration


def func():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    func()