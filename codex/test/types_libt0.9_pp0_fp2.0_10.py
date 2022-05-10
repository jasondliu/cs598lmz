import types
types.ModuleType.__getstate__ = lambda self: None

# #############################################################################
# Main script

best_model_wts = copy.deepcopy(model.state_dict())
best_acc = 0.0


class Save_model:
    def __init__(self, model,temperature):
        self.model = model
        self.temperature = temperature

    def save_model(self):
        torch.save(self.model.state_dict(),
                   './models_log/best_model_' + str(self.temperature) + '.pth')


# 模型训练过程
result = {}
for i in range(epochs):
    print('Epoch {}/{}'.format(i + 1, epochs))
    print(time.strftime('%Y-%m-%d %X', time.localtime()))
    print('-' * 30)
