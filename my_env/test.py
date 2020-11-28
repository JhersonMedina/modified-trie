from flask import Flask, request, render_template

app = Flask(__name__)

#Modified Prefix Structure for Natural Language Processing
#Modified Prefix Structure for Natural Language Processing

#-------------GLOBAL VARIABLES------------------------------------------------------------
node = 0 #Number of nodes, the root node is node 0
tree = [{}] #Tree itself
valWord = {} #Set of the most frequent valid words
freq = [] #Frecuency of Node i
isWord = [] #Boolean value set true if the current node is a complete word
word = "" #Current word that it's written
tree.append([{}])
freq.append(1)
isWord.append(False)
#-----------------------------------------------------------------------------------------

#------------SEARCHING AND ADDING FUNCTIONS-----------------------------------------------
def find(curnode, curword): #Searhces for all valid words
  global isWord
  if isWord[curnode]: #If current node is an actual word
    valWord[curword] = [freq[curnode], curnode]
  for nxt in tree[curnode]: #Recursively finds other valid words
    find(nxt[1], curword + nxt[0])
  return
def add(c): #Updates the 'word' by appending 'c' to the end, and searches for new valid words
  global node
  global word
  if not c.isalpha():
    freq[node] += 1
    isWord[node] = True
    word = ""
    return
  if c in tree[node]:
    node = tree[node][c]
    word += c
  else :
    tree[node][c] = node + 1
    node += 1
    tree.append({})
    freq.append(1)
    isWord.append(False)
    word += c
  valWord.clear()
  #find(node, word)
  return

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['input']
	processed_text = text.upper()
	for c in processed_text:
		add(c)
	global node
	global word
	global tree
	global isWord
	global valWord
	isWord[node] = True
	find(node, word)
	print("tree")
	for i in tree:
		print(i)
	print("current val words", node, word)
	for i in valWord:
		print(i)
	node = 0
	word = ""
	return processed_text
