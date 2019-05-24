# -*- coding: utf-8 -*-
import os

import pandas as pd
import numpy as np
import json
import shutil

from app import app
from flask import render_template, send_from_directory
from flask import Flask, flash, request, redirect, url_for

from werkzeug.utils import secure_filename

from app.api_tools import *

import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode
import plotly.offline as py
from plotly import tools
init_notebook_mode(connected=True)

import colorlover as cl

#ADD_NEW_MODEL
#Here import your files ----------------
#from app.models.______ import *
#

import warnings
warnings.filterwarnings('ignore')

ALLOWED_EXTENSIONS = set(['csv'])

#----check if all required directories exists
folders = ['WORK']
for name in folders:
    path = app.config[name + '_FOLDER']
    os.system("if [ ! -d " + path + " ]; then mkdir -p " + path + "; fi")


json_path = app.config['PATH_JSON']
working_path = app.config['WORK_FOLDER']


#-----------------------------------------------------
#--------Routes----------------------

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html', title='Home')


@app.route('/plot/<name>', methods=['GET', 'POST'])
def plot(name):
    path = 'maps/'+str(name) +'.html'
    print(path)
    return render_template(path, title='Graphic')
