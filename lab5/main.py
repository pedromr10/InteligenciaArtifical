import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

print('Carregando Arquivo de teste')
arquivo = np.load('teste5.npy') #Mudar valor do arquivo de teste
x = arquivo[0]
y = np.ravel(arquivo[1])


iteracoes =  30000
#calculoMedia:
somaMedia = 0
qtdExecucoes = 10
#calcuoDesvioPadrao:
valDesvio = []

#inicio do for:
for i in range (qtdExecucoes):
  regr = MLPRegressor(hidden_layer_sizes=(50, 45, 40, 35, 30, 25, 20, 15), #para criar mais hidden layers, ficaria (2,3,4) -> primeira com duas, segunda camada com 3 neuronios, etc...
                      max_iter=iteracoes,
                      activation='tanh', #{'identity', 'logistic', 'tanh', 'relu'},
                      solver='adam',
                      learning_rate = 'adaptive',
                      n_iter_no_change=iteracoes)
  print('Treinando RNA')
  regr = regr.fit(x,y)

  print('Preditor')
  y_est = regr.predict(x)

  #somando e mostrando o valor da soma dos "best_loss":
  somaMedia+=regr.best_loss_
  print("Soma das best_loss atuais: ", somaMedia)
  #adicionando os valores do best_loss para um array para utilizacao de desvio padrao:
  valDesvio.append(regr.best_loss_)

#fim do for;
print("##################################################################")
print("Media da best_loss: ", somaMedia/qtdExecucoes)
print("Desvio padrão do best_loss: ", np.std(valDesvio))
print("##################################################################")



plt.figure(figsize=[14,7])

#plot curso original
plt.subplot(1,3,1)
plt.plot(x,y)

#plot aprendizagem
plt.subplot(1,3,2)
plt.plot(regr.loss_curve_)
#print(regr.best_loss_)

#plot regressor
plt.subplot(1,3,3)
plt.plot(x,y,linewidth=1,color='yellow')
plt.plot(x,y_est,linewidth=2)




plt.show()