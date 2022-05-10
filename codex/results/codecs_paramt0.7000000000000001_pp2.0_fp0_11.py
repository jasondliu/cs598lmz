import codecs
codecs.register_error("strict", codecs.ignore_errors)
import os
import sys

def func(k,v):
    return k, v

def main():
    hdfs_path = "hdfs://10.1.1.47:8020/user/adnetik/simple_click/"
    #hdfs_path = "hdfs://10.1.1.47:8020/user/adnetik/simple_click/simple_click.tsv"
    hdfs_path_output = "hdfs://10.1.1.47:8020/user/adnetik/result/"
    #hdfs_path_output = "hdfs://10.1.1.47:8020/user/adnetik/simple_click/"
    conf = SparkConf().setAppName("click_count").set("spark.executor.memory", "2g")
    sc = SparkContext(conf = conf)
    hdfs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.h
