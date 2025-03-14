import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#variaveis de entrada:
comer = ctrl.Antecedent(np.arange(0, 31, 1), 'comer')  # Vai de 0 a 10, de 2 em 2
atv = ctrl.Antecedent(np.arange(0, 31, 1), 'atv')  # Vai de 0 a 10, de 2 em 2

#variaveis de saída:
peso = ctrl.Consequent(np.arange(0, 31, 1), 'peso')  # Vai de 0 a 10, de 2 em 2

#trimf:

peso['leve'] = fuzz.trimf(peso.universe, [0, 5, 10])
peso['medio'] = fuzz.trimf(peso.universe, [8, 15, 22])
peso['pesado'] = fuzz.trimf(peso.universe, [18, 25, 30])
peso.view()


comer['pouco'] = fuzz.trimf(comer.universe, [0, 5, 10])
comer['razoavel'] = fuzz.trimf(comer.universe, [8, 15, 22])
comer['bastante'] = fuzz.trimf(comer.universe, [18, 25, 30])
comer.view()

atv['pouca'] = fuzz.trimf(atv.universe, [0, 5, 10])
atv['razoavel'] = fuzz.trimf(atv.universe, [8, 15, 22])
atv['bastante'] = fuzz.trimf(atv.universe, [18, 25, 30])
atv.view()

#gaussmf
'''
peso['leve'] = fuzz.gaussmf(peso.universe, 5, 2)
peso['medio'] = fuzz.gaussmf(peso.universe, 15, 3)
peso['pesado'] = fuzz.gaussmf(peso.universe, 25, 4)
peso.view()

comer['pouco'] = fuzz.gaussmf(comer.universe, 5, 2)
comer['razoavel'] = fuzz.gaussmf(comer.universe, 15, 3)
comer['bastante'] = fuzz.gaussmf(comer.universe, 25, 4)
comer.view()

atv['pouca'] = fuzz.gaussmf(atv.universe, 5, 2)
atv['razoavel'] = fuzz.gaussmf(atv.universe, 15, 3)
atv['bastante'] = fuzz.gaussmf(atv.universe, 25, 4)
atv.view()
'''
#trapmf
'''
peso['leve'] = fuzz.trapmf(peso.universe, [0, 3, 7, 10])
peso['medio'] = fuzz.trapmf(peso.universe, [8, 12, 18, 22])
peso['pesado'] = fuzz.trapmf(peso.universe, [20, 25, 28, 30])
peso.view()

comer['pouco'] = fuzz.trapmf(comer.universe, [0, 3, 7, 10])
comer['razoavel'] = fuzz.trapmf(comer.universe, [8, 12, 18, 22])
comer['bastante'] = fuzz.trapmf(comer.universe, [20, 25, 28, 30])
comer.view()

atv['pouca'] = fuzz.trapmf(atv.universe, [0, 3, 7, 10])
atv['razoavel'] = fuzz.trapmf(atv.universe, [8, 12, 18, 22])
atv['bastante'] = fuzz.trapmf(atv.universe, [20, 25, 28, 30])
atv.view()
'''

#regras:
r1 = ctrl.Rule(comer['pouco'] & atv['bastante'], peso['leve'])
r2 = ctrl.Rule(comer['razoavel'] & atv['razoavel'], peso['medio'])
r3 = ctrl.Rule(comer['bastante'] & atv['pouca'], peso['pesado'])
controlador = ctrl.ControlSystem([r1, r2, r3])

#simulacao:
CalculoObesidade = ctrl.ControlSystemSimulation(controlador)
CalculoObesidade.input['comer'] = 3
CalculoObesidade.input['atv'] = 5
#CalculoObesidade.input['peso'] = 7

#crunch (onde executa o calculo aparentemente):
CalculoObesidade.compute()

#print(CalculoObesidade.output['peso'])
comer.view(sim=CalculoObesidade)
atv.view(sim=CalculoObesidade)
peso.view(sim=CalculoObesidade)
plt.show()
