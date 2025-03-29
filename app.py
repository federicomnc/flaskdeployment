#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 10:06:37 2025

@author: federicomancini
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "THIS IS WORKING"

if __name__== '__main__':
    app.run()