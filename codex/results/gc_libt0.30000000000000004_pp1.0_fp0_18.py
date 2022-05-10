import gc, weakref
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os, sys

from multiprocessing import Pool
from functools import partial

from tqdm import tqdm

from sklearn.preprocessing import LabelEncoder

from utils import (
    read_data, 
    reduce_mem_usage, 
    one_hot_encoder, 
    label_encoder, 
    column_index, 
    get_dummies,
    transform_datetime,
    transform_lat_lon,
    clip_lat_lon,
    clip_altitude,
    clip_speed,
    clip_accuracy,
    clip_bearing,
    clip_acceleration,
    clip_gyro,
    clip_magnetic,
    clip_orientation,
    clip_rotation,
    clip_gravity,
    clip_linear_acceleration,
    clip_pressure,
    clip_humidity,
    clip_temperature,
    clip_light,

