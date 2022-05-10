import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from sqlalchemy import create_engine

# SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Flask
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, make_response
from flask import session as login_session
from flask import make_response

# OAuth2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

# Requests
import requests
import httplib2

# JSON
import json

# Random
import random

# Time
import time

# OS
import os

# JSON
import json

# Database
from database_setup import Base, Category, Item

# Create session and
