from common import map_term
from common_elements import common as get_common


def search(index, query):
    # reading words from query separated by empty spaces
    terms_raw = query.split()

    if not len(terms_raw):
        return []

    res = None
    for term_raw in terms_raw:
        term = map_term(term_raw)

        term_files = index[term] if term in index.keys() else []
        # first item
        if res is None:
            res = term_files
            continue

        # common item
        res = get_common(res, term_files)
        if len(res) == 0:
            break

    return res
