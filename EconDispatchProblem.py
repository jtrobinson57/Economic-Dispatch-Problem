# -*- coding: utf-8 -*-
"""
Created on Wed May 30 09:16:21 2018

@author: j.robinson
"""

from __future__ import division
from pyomo.environ import *
from pyomo.opt import SolverFactory
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

opt = SolverFactory('glpk')

model = ConcreteModel()

data = pd.read_excel('load_cost_data.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

model.P = Var([1,2,3], domain = NonNegativeReals)

model.OBJ = Objective(expr = data.iloc[0,0] + data.iloc[0,1] + data.iloc[0,2] + 
                      data.iloc[1,0]*model.P[1] + data.iloc[2,0]*model.P[1] + 
                      data.iloc[1,1]*model.P[2] + data.iloc[2,1]*model.P[2] + 
                      data.iloc[1,2]*model.P[3] + data.iloc[2,2]*model.P[3])

model.Constraint1 = Constraint(expr = model.P[1] <= data.iloc[4,0])
model.Constraint2 = Constraint(expr = model.P[2] >= data.iloc[3,1])
model.Constraint3 = Constraint(expr = model.P[2] <= data.iloc[4,1])
model.Constraint4 = Constraint(expr = model.P[3] <= data.iloc[4,2])     
model.Constraint5 = Constraint(expr = model.P[1] + model.P[2] + model.P[3] == data.iloc[8,0] + data.iloc[9,0])

results = opt.solve(model)
model.display()


#
#model.P1 = Var(domain = NonNegativeReals)
#model.P2 = Var(domain = NonNegativeReals)
#model.P3 = Var(domain = NonNegativeReals)
#
#model.OBJ = Objective(expr = 20 + 50 + 45 + 
#                      6*model.P1 + 0.045*model.P1 + 
#                      7*model.P2 + 0.01*model.P2 + 
#                      8*model.P3 + 0.02*model.P3)
#
#model.Constraint1 = Constraint(expr = model.P1 <= 500)
#model.Constraint2 = Constraint(expr = model.P2 >= 50)
#model.Constraint3 = Constraint(expr = model.P2 <= 1000)
#model.Constraint4 = Constraint(expr = model.P3 <= 670)     
#model.Constraint5 = Constraint(expr = model.P1 + model.P2 + model.P3 == 1320 + 225)
#
