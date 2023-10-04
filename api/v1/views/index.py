#!/usr/bin/python3
"""This module contains the status endpoint"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """returns a simple JSON response"""
    return jsonify({"status": "OK"})
