""""""
from collections import defaultdict

from src.codons import scan_gene_sequence, k_most_common_amino_acids
from src.rle import rle, rld
from src.stringutils import find_common_substrings, search_for_substring
from src.bwt import bwt, ibwt

def test_lcs():
    GABRA1 = ''.join(line.rstrip() for line in open(r'data/GABRA1.txt', 'r').readlines())
    GABRA2 = ''.join(line.rstrip() for line in open(r'data/GABRA2.txt', 'r').readlines())

    longest_common_substring = find_common_substrings(GABRA1, GABRA2)
    print(longest_common_substring)
    # T T A T T A T T A T A C T T T A A G T T T T A G G G T A C A T G T G C



## BURROWS WHEELER ##
def test_bwt():
    s1 = 'SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES'
    transformed = bwt(s1)
    inverted_back = ibwt(transformed)
    assert s1 == inverted_back

    print(s1)
    print(transformed)
    print(inverted_back)


## RUN LENGTH ENCODING ##
def test_rle():
    GABRA1 = ''.join(line.rstrip() for line in open(r'data/GABRA1.txt', 'r').readlines())
    #GABRA1 = break_up_groups_of_k_length(GABRA1[:len(GABRA1)//20], 20)
    GABRA1 = GABRA1[:len(GABRA1)//30]
    print(GABRA1)

    transformed = bwt(GABRA1)
    inverted_back = ibwt(transformed)
    assert GABRA1 == inverted_back

    print(GABRA1)
    print(transformed)
    print(inverted_back)

    print(rle(GABRA1))
    print(rle(transformed))

    degree_of_compression_without_bwt = (len(rle(GABRA1)) / len(GABRA1)) * 100
    degree_of_compression_with_bwt = (len(rle(transformed)) / len(transformed)) * 100
    rle_with_transform_vs_neither = (len(rle(transformed)) / len(GABRA1)) * 100

    print(f"Degree of compression without BWT: {degree_of_compression_without_bwt:.2f}%")
    print(f"Degree of compression with BWT: {degree_of_compression_with_bwt:.2f}%")
    print(f"RLE with BWT vs neither: {rle_with_transform_vs_neither:.2f}%")

    print(rle(GABRA1))
    print(rld(rle(GABRA1)))
    assert rld(rle(GABRA1)) == GABRA1



test_rle()




def test_codons():
    GABRA1 = ''.join(line.rstrip() for line in open(r'data/GABRA1.txt', 'r').readlines())
    gabra1, counter = scan_gene_sequence(GABRA1, counter=defaultdict(int))
    print(gabra1[0])
    print(k_most_common_amino_acids(counter, 3))


#test_codons()



def test_substring_search():
    s = "Hello World"
    k_p, substring = search_for_substring(s, "World").rstrip('"').split(' k..p="')
    print(k_p)
    start_index, end_index = [kp.rstrip().split('=')[-1] for kp in k_p.split(' ')]
    print(f"Substring: {substring.replace(' ', '')}")
    print(f"Start index: {start_index}")
    print(f"End index: {end_index}")
    print(f"Reconstructed: {s[int(start_index):int(end_index)]}")


test_substring_search()



