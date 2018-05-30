# -*- coding: utf-8 -*-
"""
Created on Wed May 30 09:16:21 2018

@author: j.robinson
"""

from __future__ import division
from pyomo.environ import *

model = ConcreteModel()



model.P1 = Var(domain = NonNegativeReals)
model.P2 = Var(domain = NonNegativeReals)
model.P3 = Var(domain = NonNegativeReals)

model.OBJ = Objective(expr = 20 + 50 + 45 + 
                      6*model.P1 + 0.045*model.P1 + 
                      7*model.P2 + 0.01*model.P2 + 
                      8*model.P3 + 0.02*model.P3)

model.Constraint1 = Constraint(expr = model.P1 <= 500)
model.Constraint2 = Constraint(expr = model.P2 >= 50)
model.Constraint3 = Constraint(expr = model.P2 <= 1000)
model.Constraint4 = Constraint(expr = model.P3 <= 670)     
model.Constraint5 = Constraint(expr = model.P1 + model.P2 + model.P3 == 1320 + 225)



#model.P = Var([1,3], domain = NonNegativeReals)
#
#model.OBJ = Objective(expr = 20 + 50 + 45 + 
#                      10*model.P[1] + 0.045*model.P[1]**2 + 
#                      7*model.P[2] + 0.01*model.P[2]**2 + 
#                      8*model.P[3] + 0.02*model.P[3]**2)
#
#model.Constraint1 = Constraint(expr = model.P[1] <= 500)
#model.Constraint2 = Constraint(expr = model.P[2] >= 50)
#model.Constraint3 = Constraint(expr = model.P[2] <= 1000)
#model.Constraint4 = Constraint(expr = model.P[3] <= 670)     
#model.Constraint5 = Constraint(expr = model.P[1] + model.P[2] + model.P[3] == 1320 + 225)