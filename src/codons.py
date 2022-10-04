""""""
from collections import defaultdict

rna_codon_dict = dict(
    AAA='K', AAC='N', AAG='K', AAU='N', ACA='T', ACC='T', ACG='T', ACU='T', AGA='R', AGC='S', AGG='R', AGU='S', AUA='I',
    AUC='I', AUG='M', AUU='I', CAA='Q', CAC='H', CAG='Q', CAU='H', CCA='P', CCC='P', CCG='P', CCU='P', CGA='R', CGC='R',
    CGG='R', CGU='R', CUA='L', CUC='L', CUG='L', CUU='L', GAA='E', GAC='D', GAG='E', GAU='D', GCA='A', GCC='A', GCG='A',
    GCU='A', GGA='G', GGC='G', GGG='G', GGU='G', GUA='V', GUC='V', GUG='V', GUU='V', UAA='*', UAC='Y', UAG='*', UAU='Y',
    UCA='S', UCC='S', UCG='S', UCU='S', UGA='*', UGC='C', UGG='W', UGU='C', UUA='L', UUC='F', UUG='L', UUU='F'
)

dna_codon_dict = dict(
    TTT='F', TTC='F', TTA='L', TTG='L', TCT='S', TCC='S', TCA='S', TCG='S', TAT='Y', TAC='Y', TAA='*', TAG='*', TGT='C',
    TGC='C', TGA='*', TGG='W', CTT='L', CTC='L', CTA='L', CTG='L', CCT='P', CCC='P', CCA='P', CCG='P', CAT='H', CAC='H',
    CAA='Q', CAG='Q', CGT='R', CGC='R', CGA='R', CGG='R', ATT='I', ATC='I', ATA='I', ATG='M', ACT='T', ACC='T', ACA='T',
    ACG='T', AAT='N', AAC='N', AAA='K', AAG='K', AGT='S', AGC='S', AGA='R', AGG='R', GTT='V', GTC='V', GTA='V', GTG='V',
    GCT='A', GCC='A', GCA='A', GCG='A', GAT='D', GAC='D', GAA='E', GAG='E', GGT='G', GGC='G', GGA='G', GGG='G'
)


def k_most_common_amino_acids(counter, k: int):
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]


def scan_gene_sequence(seq: str, save_codons: bool = False, counter: defaultdict = None):
    proteins = [[]]
    index_of_current_protein = 0
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) < 3: break
        proteins[index_of_current_protein].append(codon if save_codons else dna_codon_dict[codon])
        if counter != None: counter[codon if save_codons else dna_codon_dict[codon]] += 1
        if codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            proteins.append([])
            index_of_current_protein += 1
    return (proteins, counter) if counter else (proteins, None)


