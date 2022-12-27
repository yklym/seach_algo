from common import get_file_content, map_term


def create_index(filenames, index, file_titles):
    for filename in filenames:

        content = get_file_content(filename)
        file_titles[filename] = content.partition('\n')[0]  # title

        terms_raw = content.split()
        for term_raw in terms_raw:
            mapped_term = map_term(term_raw)
            if not (mapped_term in index):
                index[mapped_term] = []
            if filename not in index[mapped_term]:
                index[mapped_term].append(filename)

    return 0
