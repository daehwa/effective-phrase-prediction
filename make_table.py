import copy

wFile = open('./phrase_data.txt','w')
rFile = open('./corpus.txt','r')

N = 4 # n-gram
tau = 3
##########
# prune all phrases below the threshold parameter(tau) and store the rest
############
def frequency(tree):
	if tree:
		for node in tree.children:
			tree.children = [t for t in tree.children if t.count >= tau]
		for node in tree.children:
			frequency(node)

##########
# extract significant phrases with frequency number to .txt file
############
def phrase_list(tree):
	if tree:
		if not tree.children:
			t = tree
			ls = []
			while t.parent!=None:
				ls.insert(0,t.data)
				t=t.parent
			wFile.write(''.join(s+" " for s in ls) + str(tree.count) + "\n")
		else:
			for node in tree.children:
				phrase_list(node)

##########
# A Node for fussytree
############
class Node(object):
	def __init__(self,data):
		self.data = data
		self.count = 1
		self.children = []
		self.parent = None
	def add_child(self,obj,par):
		self.children.append(obj)
		self.children[len(self.children)-1].parent = par
		
	def contain_child(self,d):
		return [i for i, s in enumerate(self.children) if s.data==d]

# root node
fussytree = Node("root")

##########
# Extend fussytree
############
while True:
	data = rFile.readline()
	if not data:
		break;
	sentence = data.split()
	for n in range(len(sentence)):
		flag = False
		tree = fussytree
		leng = min(n+N,len(sentence))
		N_gram = sentence[n:leng]	# should cut down a sentence to n_gram
		for i in range(len(N_gram)):
			if (flag):
				tree.add_child(Node(N_gram[i]),tree)
				tree = tree.children[0]
			elif not tree.contain_child(N_gram[i]): # there is no the word
				tree.add_child(Node(N_gram[i]),tree)
				index = len(tree.children)-1
				tree = tree.children[index]
				flag = True
			else:	# there exits the word
				index = tree.contain_child(N_gram[i])
				tree = tree.children[index[0]]
				tree.count += 1
frequency(fussytree)
phrase_list(fussytree)
