import os


def find_word(curr_list, migr_dir):

    new_list = []
    word = input('Введите строку:')

    for filename in curr_list:
        with open(os.path.join(migr_dir, filename)) as f:
            if word in f.read():
                new_list.append(filename)
                print(filename)

    print('Всего: {}'.format(len(new_list)))
    
    return new_list


def run_search():
    
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))

    migr_dir = os.path.join(current_dir, migrations)
    file_list = os.listdir(migr_dir)
    
    work_list = []
    for file in file_list:
        if os.path.splitext(file)[1] == '.sql':
            work_list.append(file)
    
    while True:
        work_list = find_word(work_list, migr_dir)
        if not work_list:
            break


if __name__ == '__main__':
    run_search()
