from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = lambda self, data: self.decompress(data).decode('utf-8')

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.json('s3://kaggle-coronavirus-source/biorxiv_medrxiv/biorxiv_medrxiv/pdf_json/*.json.bz2')

df.printSchema()

df.show()

df.createOrReplaceTempView('corona')

#df.write.parquet('s3://kaggle-coronavirus-source/biorxiv_medrxiv/biorxiv_medrxiv/pdf_json/corona.parquet', mode='overwrite')

#df.write.mode("overwrite").json("s3://kaggle-coronavirus-source/biorxiv_medrxiv/biorxiv_medrxiv/pdf_json/corona.json")

#df.write.mode("overwrite").csv
