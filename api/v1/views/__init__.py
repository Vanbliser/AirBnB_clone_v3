#!/usr/bin/python3
"""This script contains the implementation of blueprints for AirBnB clone"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
