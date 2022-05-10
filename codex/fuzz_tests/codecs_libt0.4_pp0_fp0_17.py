import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# import cx_Oracle
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import datetime
# import time
# import sys
# import os
# import re
# import datetime
# import time
# from dateutil.relativedelta import relativedelta
# from dateutil.parser import parse
# from datetime import datetime, timedelta
# import calendar
# import logging
# import logging.handlers
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# from email.header import Header
# from email.utils import parseaddr, formataddr
# from email.utils import formatdate

