""""""


def search_for_substring(string: str, substring: str) -> (int, int):
    from suffix_tree import Tree as SuffixTree
    tree = SuffixTree({"A": string})
    if tree.find(substring): return tree.find_all(substring)[0][1].ukko_str()



def find_common_substrings(string1: str, string2: str):
    from suffix_tree import Tree as SuffixTree
    tree = SuffixTree({"A": string1, "B": string2})
    # tree = SuffixTree({"A": "Hello World", "B": "yellow world"})
    common_substrings = tree.common_substrings()
    if len(common_substrings):
        return str(common_substrings[0][2].ukko_str())



def break_up_groups_of_k_length(s: str, k: int, delimiter: str = '.') -> str:
    new_s1 = ''
    n = len(s)
    i = 0
    while i < n:
        new_s1 += s[i]
        if i % k == 0:
            new_s1 += delimiter
        i += 1
    return new_s1




