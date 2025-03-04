# DNA Learning Tool – Technical Documentation

## Overview

This repository contains a Python script that demonstrates basic concepts of DNA analysis, including:
1. Translating a DNA sequence into a protein sequence (using codons).
2. Querying the BLAST database (via BioPython) to identify matching proteins.
3. (Optional) Simulating mutations or analyzing DNA stability (e.g., G-C content) can be added or expanded.

## Features

- **Codon to Amino Acid Translation:**
  - Converts triplets of nucleotides (codons) into corresponding amino acids using a predefined lookup table.
- **BLAST Integration:**
  - Uses BioPython to connect with the NCBI BLAST service, bypassing SSL certificate verification (for demonstration purposes).
- **Protein Match Identification:**
  - Retrieves potential matches from the “nr” database, enabling basic analysis of protein functions.

## System Requirements

- **Python 3.11.1 (or later)** is recommended.
- **BioPython** (for BLAST queries and sequence handling).
- **Internet Connection** (required to query NCBI’s BLAST service).
- **SSL Bypass Note:** The script disables SSL certificate verification, which may not be secure for production use.

## Installation

1. **Clone or Download the Repository**
   - Clone the repo using:
     ```bash
     git clone https://github.com/your-username/DNALearningTool.git
     ```
   - Or download the ZIP file and extract it.

2. **Install Dependencies**
   - Create a virtual environment (optional but recommended):
     - **On Windows:**
       ```bash
       python -m venv env
       env\Scripts\activate
       ```
     - **On Linux:**
       ```bash
       python3 -m venv env
       source env/bin/activate
       ```
   - Install BioPython (and any other required packages):
     ```bash
     pip install biopython
     ```

3. **Run the Script**
   - **On Windows:**
     ```bash
     python dna_program.py
     ```
   - **On Linux:**
     ```bash
     python3 dna_program.py
     ```

## Usage

1. **Check or Modify the DNA Sequence**
   - Open `dna_program.py` in a text editor.
   - Update the `dna_sequence` variable with your own sequence if desired.
2. **Translate DNA to Protein**
   - The script splits the DNA into codons, then uses the codon lookup table to generate a protein sequence.
3. **Query BLAST**
   - The script uses BioPython’s `NCBIWWW.qblast` to query the “nr” database.
   - Results are saved to an XML file (`blast_result.xml`) and then parsed to display potential matches.
4. **Inspect or Extend**
   - Explore or modify the functions for analyzing GC content, simulating mutations, or checking secondary structure predictions (if you add that logic).

## Security Note

- The code bypasses SSL certificate verification for demonstration purposes, which is not secure. If you plan to use this in a more permanent or production environment, remove the SSL bypass and ensure proper certificate handling.

## Roadmap

- **Mutations Simulation:** Expand the script to randomize or systematically introduce mutations and observe changes in the resulting protein.
- **Advanced Analysis:** Integrate further tools from BioPython (e.g., alignment, advanced search options).
- **Error Handling:** Improve error handling for incomplete codons, network issues, or BLAST service downtime.

## Contributing

1. Fork this repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Open a pull request for review.

## License

This project is distributed under the MIT License. See LICENSE for more information.
