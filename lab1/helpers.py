from os import walk
import time

BASE_LINK = './files'
DELIM = ', '

filenames = next(walk(BASE_LINK), (None, None, []))[2]  # [] if no file


def get_file_words(filename):
    f = open(filename)
    items_line = f.readline()
    f.close()

    # parse words
    words = items_line.strip('\n').split(DELIM)
    return list(dict.fromkeys(words))


def create_forward_idx():
    index = {}
    start_time = time.time()

    for filename in filenames:
        words = get_file_words(f'{BASE_LINK}/{filename}')
        index[filename] = words

    print("\n\n--- created forward idx in %s ---\n\n" %
          (time.time() - start_time))

    return index


def create_inverse_idx():
    index = {}
    start_time = time.time()

    for filename in filenames:

        words = get_file_words(f'{BASE_LINK}/{filename}')

        for word in words:
            if word not in index:
                index[word] = set([filename])
            else:
                index[word].add(filename)

    print("\n\n--- created inverse idx in %s ---\n\n" %
          (time.time() - start_time))

    return index


def search_forward_idx(index, word, isLogging=True):
    filenames = []
    start_time = time.time()

    for key, value in index.items():
        if word in value:
            filenames.append(key)

    if isLogging:
        print("\n\n--- forward search in %s ---\n\n" %
              (time.time() - start_time))
    return filenames


def search_inverse_idx(index, word, isLogging=True):
    start_time = time.time()

    filenames = index[word] if word in index else []

    if isLogging:
        print("\n\n--- inverse search in %s ---\n\n" %
              (time.time() - start_time))

    return filenames
