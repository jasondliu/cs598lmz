import weakref
# Test weakref.ref(buf) to make sure Python can handle circular references.
# We do this *before* importing anything from Bio.
buf = [1]
buf.append(weakref.ref(buf))
# This code is not part of Biopython, but needs to be run to create the test
# data for the code below.
#
# from Bio import SeqIO
# for seq_record in SeqIO.parse("GenBank/NC_005816.gb", "gb"):
#     print("Record %s has %i features" % (seq_record.id, len(seq_record.features)))
#     for feature in seq_record.features:
#         print("Feature location: %s" % repr(feature.location))
#         print("Feature type: %s" % feature.type)
#         print("Feature strand: %s" % feature.strand)
#         print("Feature id: %s" % feature.id)
#         print("Feature qualifiers:")
#         for key, value in sorted(feature.qualifiers.items()):
#             print("%s: %s
