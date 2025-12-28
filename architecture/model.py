import torch.nn as nn

class RegressionModel(nn.Module):
    def __init__(self, input_size=2, hidden_size=32, num_layers=1, output_size=2): # input/output size (cpu_percent, mem_mb)
        super(RegressionModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = out[:, -1, :]
        out = self.fc(out)
        return out