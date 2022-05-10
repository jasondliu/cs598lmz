import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import sys
sys.path.append('../')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from src.utils.utils import get_movies_dataframe, get_ratings_dataframe, get_tags_dataframe, get_links_dataframe
from src.utils.utils import get_movie_genres_dataframe, get_movie_directors_dataframe, get_movie_actors_dataframe
from src.utils.utils import get_movie_keywords_dataframe
from src.utils.utils import get_movie_tags_dataframe
from src.utils.utils import get_movie_recommendations
from src.utils.utils import get_movie_title

%matplotlib inline

# Set the default style for matplotlib
plt.style.use
