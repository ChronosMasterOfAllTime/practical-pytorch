import torch.nn as nn


class TagRNN(nn.Module):

    def __init__(self, isize, osize):
        super(TagRNN, self).__init__()
        self.rnn = nn.GRU(isize, osize)
        self.act = nn.Sigmoid()

    def forward(self, x, h):
        x, h = self.rnn(x, h)
        return x, h
