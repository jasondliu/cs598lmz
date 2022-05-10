import sys, threading
threading.Thread(target=lambda: sys.stdout.write(' ')).start()
import urllib
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from urllib.request import urlopen
import json
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
# Create your views here.

# Set Global variables
twilio_account='AC66ecd9253cba1d2cde83c04fde115c50'
twilio_token='586fc72822e2b7922445deebbf4a1463'

# You'll need to put your specif user login in here.
client = Client(twilio_account, twilio_token)

def index(request) :
    return HttpResponse('welcome to funnnnn')

def send_text(request) :
    # print(request.GET['probability'], type(request.GET['
