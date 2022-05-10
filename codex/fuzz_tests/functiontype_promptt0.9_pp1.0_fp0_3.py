import types
# Test types.FunctionType()

###############################################################################
# create and return a few functions
def random_scripts():
	# random seq from DNA
	return random_seq(DNA.alphabets.unambiguous_dna, 10)
	#random_seq(DNA.alphabets.degenerate_dna, 10)

	#random_seq(IOB.alphabets.alu, 10)

	#random_seq(IOB.alphabets.degenerate_alu, 10)

	#random_seq(Codons.alphabets.dna_by_id["Standard"], 10)
	#random_seq(Codons.alphabets.dna_by_name["Standard"], 10)

	#random_seq(Codons.alphabets.protein_by_id["Vertebrate_Mitochondrial"], 10)
	#random_seq(Codons.alphabets.protein_by_name["Vertebrate_Mitochondrial"], 10)

	#random_seq(RNA.alphabets.unambiguous_rna, 10)
	#random_seq(RNA
