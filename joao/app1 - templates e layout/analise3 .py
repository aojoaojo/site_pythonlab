#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 10:20:21 2022

@author: aojoaojov
"""

import pandas as pd

def get_data3():
    dados = pd.read_csv('static/archive/ds_salaries.csv')
    return dados

