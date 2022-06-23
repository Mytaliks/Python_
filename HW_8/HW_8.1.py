
from collections import Counter, deque


class HuffCod:

    def __init__(self, user_str):
        self.user_str = user_str
        self.cod_tab = dict()
        self.huff_cod(self.get_tree())

    def get_counter_sym(self):
        return Counter(self.user_str)

    def sort_counter_value(self):
        return deque(sorted(self.get_counter_sym().items(),
                            key=lambda item: item[1]))

    def get_tree(self):
        sort_value = self.sort_counter_value().copy()
        if len(sort_value) != 1:
            while len(sort_value) > 1:
                weight = sort_value[0][1] + sort_value[1][1]
                new_elem = {0: sort_value.popleft()[0],
                            1: sort_value.popleft()[0]}
                for i, _count in enumerate(sort_value):
                    if weight > _count[1]:
                        continue
                    else:
                        sort_value.insert(i, (new_elem, weight))
                        break
                else:
                    sort_value.append((new_elem, weight))
        else:
            weight = sort_value[0][1]
            new_elem = {0: sort_value.popleft()[0], 1: None}
            sort_value.append((new_elem, weight))
        return sort_value[0][0]

    def huff_cod(self, tree, path=''):
        if not isinstance(tree, dict):
            self.cod_tab[tree] = path
        else:
            self.huff_cod(tree[0], path=f'{path}0')
            self.huff_cod(tree[1], path=f'{path}1')

    def get_string_code(self):
        res = ''
        for i in self.user_str:
            res += self.cod_tab[i]
        return res

    def decoding(self, code_str):
        result = ''
        i = 0
        codes_dict = self.cod_tab
        while i < len(code_str):
            for code in codes_dict:
                if code_str[i:].find(codes_dict[code]) == 0:
                    result += code
                    i += len(codes_dict[code])
        return result


if __name__ == '__main__':
    string = input("Введите строку: ")
    b = HuffCod(string)
    print(f"Исходная строка:\n'{string}'")

    tree_1 = b.get_tree()
    print(f"Дерево:\n{tree_1}")

    print(f"Таблица c кодами:\n{b.cod_tab}")

    cod_str = b.get_string_code()
    print(f"Строка кода после кодирования:\n{cod_str}")
    print(f"Декодированная строка:\n'{b.decoding(cod_str)}'")
