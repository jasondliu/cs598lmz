from bz2 import BZ2Decompressor
BZ2Decompressor

# Read the smaller file first, to be able to extract specific features of it.
df = spark.read.csv('s3a://mass-dph-opioid-overdose-data/intermediate/pinnacle_mapping.csv',
                    header = True, 
                    schema = 'icdcode STRING, icdname STRING, drugname STRING')
# df.show()

# df.write.parquet('s3a://mass-dph-opioid-overdose-data/intermediate/pinnacle_mapping.pq')
# df.write.orc('s3a://mass-dph-opioid-overdose-data/intermediate/pinnacle_mapping.orc')

drug_mapping = df.select('icdcode', 'drugname').orderBy('icdcode')
# drug_mapping.show()
drug_mapping_pd = drug_mapping.toPandas()

# drugs = drug_mapping.dropDuplicates(['icdcode'])
# drugs.show()
drugs = drug_mapping
