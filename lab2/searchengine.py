import os
import sys
from create_index import create_index
from search import search


def search_menu(index, file_titles):
    while True:
        query = input("Query, empty to stop: ")
        if query == '':
            break
        results = search(index, query)

        # display query results
        print(f"Results for [{query}] :\n")

        if not len(results):
            print(f"No results for [{query}]")

        for i in range(len(results)):
            title = file_titles[results[i]]
            print(f"title: [{title}], file: [{results[i]}]")
        print('==============')


def main():
    args = sys.argv[1:]

    num_args = len(args)

    directory = args[0]

    if not os.path.exists(directory):
        return 1

    files = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            files.append(os.path.join(directory, filename))

    index = {}
    file_titles = {}
    create_index(files, index, file_titles)

    # Either allow the user to search using the index, or just print the index
    if num_args == 2 and args[1] == '-s':
        search_menu(index, file_titles)
    else:
        print('index: ', index)
        print('\ntitles: ', file_titles)


if __name__ == '__main__':
    main()
