def len_file(file_name: str) -> int:
    with open(f'{file_name}', encoding='utf-8') as file:
        count = 0
        for line in file:
            count += 1
    return count


def write_file(new_file: str, old_file_list: list) -> None:
    with open(f'{new_file}', mode='w', encoding='utf-8') as file:
        for file_ in sorted(old_file_list, key=lambda x: len_file(x)):
            with open(f'{file_}', mode='r', encoding='utf-8') as file_content:
                file_info = f'Название файла: {file_}\nКоличество строк: {len_file(file_)}\n'
                file.write(file_info)
                for line in file_content:
                    file.write(line)
                file.write('\n')


print(len_file('1.txt'))
print(len_file('2.txt'))
print(len_file('3.txt'))
list_text = ['1.txt', '2.txt', '3.txt']
write_file('result.txt', list_text)
