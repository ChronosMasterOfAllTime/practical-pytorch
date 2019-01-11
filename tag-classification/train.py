import string
import torch
import torch.nn.CrossEntropyLoss as CELoss
import data
from torch import optim
from models import TagRNN


# load all training data into tups and shuffle for better learning
# the tagname will be the filename
word_tagidx_tup = []
taglist = []

all_letters = string.ascii_letters + " .,;'-"
n_letters = len(all_letters)


def vectorize(letter):
    i = ord(letter)
    tensor = torch.zeros(n_letters)
    tensor[i] = 1.0
    return tensor


rnn = TagRNN(n_letters, len(taglist))
rnn_optimizer = optim.Adam(rnn.parameters())
criterion = CELoss()

for filename in data.findfiles('../data/*.txt'):
    category = filename.split('\\')[-1].split('.txt')[0]

    lines = data.readlines(filename)

    for line in lines:
        word_tagidx_tup.append((line, category))

for word, tagidx in word_tagidx_tup:
    rnn_optimizer.zero_grad()

    vectors = map(vectorize, word)

    h = None
    x = None

    for vector in vectors:
        x, h = rnn(vector, h)

    loss = criterion(x, torch.LongTensor([tagidx]))
    loss.backward()

    rnn_optimizer.step()
