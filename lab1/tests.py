from helpers import get_file_words, create_forward_idx, create_inverse_idx, search_inverse_idx, search_forward_idx


BASE_LINK = './test_files'


def test_get_file_words():
    # check 1: basic parse
    file_one_data = get_file_words(f'{BASE_LINK}/test_file1.txt')

    assert len(file_one_data) == 3, "has 3 items"
    assert file_one_data[0] == "antimage", "first item is am"
    assert file_one_data[1] == 'axe', "second item is axe"
    assert file_one_data[2] == 'bane', "third item is bane"

    print('test_get_file_words check 1 passed =====>')

    # check 2 remove duplicates
    file_two_data = get_file_words(f'{BASE_LINK}/test_file2.txt')

    assert len(file_one_data) == 3, "has 3 items"
    assert file_two_data[0] == "antimage", "first item is am"
    assert file_two_data[1] == 'axe', "second item is axe"
    assert file_two_data[2] == 'bane', "third item is bane"

    print('test_get_file_words check 2 passed =====>')


forward_index = {
    "file1": ['word1'],
    "file2": ['word1', 'word2'],
}

inverse_index = {
    'word1': ['file1', 'file2'],
    'word2': ['file2'],
}


def test_forward_search():
    # check 1 missing item
    filenames = search_forward_idx(forward_index, "word3", False)
    assert len(filenames) == 0, 'no results found'

    # check 2 single filename
    filenames = search_forward_idx(forward_index, "word2", False)

    assert len(filenames) == 1, 'has single file'
    assert (filenames[0]) == 'file2', 'contains file'

    # check 3 double filename
    filenames = search_forward_idx(forward_index, "word1", False)

    assert len(filenames) == 2
    assert 'file2' in filenames, 'contains file'
    assert 'file1' in filenames, 'contains file'

    # empty index
    filenames = search_forward_idx({}, "word1", False)
    assert len(filenames) == 0

    print('test forward search passed =====>')


def test_inverse_search():
    # check 1 missing item
    filenames = search_inverse_idx(inverse_index, "word3", False)
    assert len(filenames) == 0, 'no results found'

    # check 2 single filename
    filenames = search_inverse_idx(inverse_index, "word2", False)

    assert len(filenames) == 1, 'has single file'
    assert (filenames[0]) == 'file2', 'contains file'

    # check 3 double filename
    filenames = search_inverse_idx(inverse_index, "word1", False)

    assert len(filenames) == 2
    assert 'file2' in filenames, 'contains file'
    assert 'file1' in filenames, 'contains file'

    # empty index
    filenames = search_inverse_idx({}, "word1", False)
    assert len(filenames) == 0

    print('test inverse search passed =====>')


if __name__ == "__main__":
    test_get_file_words()
    test_forward_search()
    test_inverse_search()
    print("Everything passed")
