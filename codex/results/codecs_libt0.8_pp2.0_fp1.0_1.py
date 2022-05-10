import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import sys
import re
import os


def main():
    original_datasets_filename = "data/datasets.txt"
    original_datasets = open(original_datasets_filename, "r")

    datasets_filename = "data/datasets-terminated.txt"
    datasets = open(datasets_filename, "w")

    projects_filename = "data/projects-terminated.txt"
    projects = open(projects_filename, "w")

    for line in original_datasets:
        dataset_parameters = re.split("\t", line)
        project_id = dataset_parameters[0]
        dataset_id = dataset_parameters[1]
        project_name = dataset_parameters[2]
        dataset_name = dataset_parameters[3]
        dataset_path = dataset_parameters[4]
        dataset_path = re.sub("\n", "", dataset_path)
