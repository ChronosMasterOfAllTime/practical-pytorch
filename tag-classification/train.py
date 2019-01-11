import torch
import torch.nn.CrossEntropyLoss as Loss
from torch import optim
from models import TagRNN

def vectorize(letter):
	i = ord(letter)
	tensor = torch.zeros(256)
	tensor[i] = 1.0
	return tensor


rnn = TagRNN(256, 7)
rnn_opt = optim.Adam(rnn.parameters())
crit = Loss()

# load all training data into tups and shuffle for better learning
# the tagname will be the filename
word_tagidx_tup = []
taglist = []

for word, tagidx in word_tagidx_tup:
	rnn_opt.zero_grad()
	
	vectors = map(vectorize, word)
	
	h = None
	for vector in vectors:
		x, h = rnn(vector, h)
		
	loss = crit(x, torch.LongTensor([tagidx]))
	loss.backward()
	
	rnn_opt.step()
	

