import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# What is the most common word used to address you on GitHub?

# Setup your `wc` library with your GitHub token.
!export GITHUB_TOKEN=a97c1603b7e17c99caa9218f6355299ac6d05ab2;
!pip install wc
!wc setup --token $GITHUB_TOKEN

#Get data for your GitHub repositories and make a DataFrame.
!wc repos
!wc repos list --default
import pandas as pd
import json

def load_github_data(file_):
    """Load a json file as a Pandas DataFrame."""
    with open(file_) as f:
        return pd.DataFrame(json.load(f))

df = load_github_data("./table.json")

#Get individual contributors and messages.
!wc repos contributors --default
!wc repos messages --default
df = load_github_data("./table.json")
df_cont
