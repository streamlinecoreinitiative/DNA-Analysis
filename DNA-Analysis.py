import ssl
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

# Bypass SSL certificate verification (for development purposes)
ssl._create_default_https_context = ssl._create_unverified_context

# Codon to amino acid lookup table
codon_table = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_', 'TGA': '_'
}

# Function to translate DNA sequence into a protein
def translate_dna_to_protein(dna_sequence):
    protein = []

    # Process the sequence in chunks of 3 (codons)
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i + 3]  # Extract a codon (3 bases)

        # Make sure codon is complete (sometimes the last codon might be incomplete)
        if len(codon) == 3:
            # Translate the codon using the codon table
            amino_acid = codon_table.get(codon, '?')  # Use '?' if the codon is unknown
            protein.append(amino_acid)

    # Return the protein sequence
    return ''.join(protein)

# Function to query BLAST with a protein sequence and return matching results
def blast_protein_sequence(protein_sequence):
    # Query BLAST with the protein sequence
    print("Querying BLAST for the protein sequence...")
    result_handle = NCBIWWW.qblast("blastp", "nr", protein_sequence)

    # Save the result to a file (optional, for reference)
    with open("blast_result.xml", "w") as out_file:
        out_file.write(result_handle.read())

    # Parse the BLAST result to extract useful information
    print("Parsing BLAST results...")
    with open("blast_result.xml") as result_handle:
        blast_record = NCBIXML.read(result_handle)

    # Check if any matches were found
    if not blast_record.alignments:
        print("No matches found in BLAST.")
    else:
        # Extract and print information from the BLAST results
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                print(f"****Alignment****")
                print(f"sequence: {alignment.title}")
                print(f"length: {alignment.length}")
                print(f"e-value: {hsp.expect}")
                print(f"identity: {hsp.identities}")
                print(f"match description: {alignment.title}")

# Example DNA sequence (feel free to change it to a longer one)
dna_sequence = "ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG"

# Step 1: Translate the DNA sequence into a protein
protein_sequence = translate_dna_to_protein(dna_sequence)

# Step 2: Print the DNA and protein sequence
print(f"DNA Sequence: {dna_sequence}")
print(f"Protein Sequence: {protein_sequence}")

# Step 3: Query BLAST with the protein sequence to get protein matches
blast_protein_sequence(protein_sequence)
