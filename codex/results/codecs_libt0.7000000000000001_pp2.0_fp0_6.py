import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import mysql.connector
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.dialects.mysql import TINYINT
from datetime import date, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy import desc
from sqlalchemy import func
import pandas as pd
import numpy as np
import datetime
import re
from datetime import date, timedelta
from sqlalchemy import desc
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.decomposition
