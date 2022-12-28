def common(list1, list2):
    return list(set([x for x in list1 if x in list2]))


if __name__ == '__main__':
    print(""" common(['a', 'b', 'c'], ['c', 'a', 'z']) == ['a', 'c'] :""", common(
        ['a', 'b', 'c'], ['c', 'a', 'z']))
    print(""" common(['a', 'b', 'c'], ['x', 'y', 'z']) == [] :""",
          common(['a', 'b', 'c'], ['x', 'y', 'z']))
    print(""" common(['a', 'a', 'b'], ['x', 'a', 'a']) == ['a'] :""",
          common(['a', 'a', 'b'], ['x', 'a', 'a']))
