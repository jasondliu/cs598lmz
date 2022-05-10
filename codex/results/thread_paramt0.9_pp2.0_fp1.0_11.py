import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n')).start()

torch.set_grad_enabled(True)

alphas = [0.001,0.01,0.1,1.0,10,100]
trainLoss, testLoss = [], []
#compute loss/error for different learning rate
for alpha in alphas:
  mlp = MLP([inputTensor.shape[1],inputTensor.shape[1]],[nn.Sigmoid()])
  mlp.optimizer = torch.optim.SGD(mlp.parameters(),lr=alpha)
  trainLoss.append(nnTrainer(mlp,inputTensor,targetTensor,1))
  testLoss.append(nnEvaluator(mlp,inputTensor,targetTensor))

#plot trainLoss vs testLoss
plt.semilogx(alphas, trainLoss)
plt.semilogx(alphas, testLoss)
plt.grid(True)
plt.legend(['train', 'test'], loc
