from flask import Flask, request, render_template

app = Flask(__name__)

#Modified Prefix Structure for Natural Language Processing

#-------------GLOBAL VARIABLES------------------------------------------------------------
node = 0 #Number of nodes, the root node is node 0
tree = [] #Tree itself
valWord = [] #Set of the most frequent valid words
freq = [] #Frecuency of Node i
isWord = [] #Boolean value set true if the current node is a complete word
word = "" #Current word that it's written
tree.append({})
freq.append(1)
isWord.append(False)
#-----------------------------------------------------------------------------------------

#------------SEARCHING AND ADDING FUNCTIONS-----------------------------------------------
#Searhces for all valid words
def find(curnode, curword):
  global isWord
  global valWord
  global Tree
  global freq
  if isWord[curnode]:
    valWord.append({freq[curnode], curnode})
  else:
    for c in tree[curnode]:
      find(i[1], curword + i[0])
  return
#Updates the 'word' by appending 'c' to the end, and searches for new valid words
def add(c):
  global node
  global tree
  global freq
  global isWord
  global word
  print(c)
  if c in tree[node]:
    node = tree[node][c]
    isWord[node] += 1
  else:
    tree[node][c] = node + 1
    node += 1
    freq.append(1)
    isWord.append(1)
    tree.append({})
  word += c
  find(node, word)
  return

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
  global tree
  global node
  global word
  global valWord
  text = request.form['input']
  processed_text = text.upper()
  print(tree)
  for c in processed_text:
    print(c)
    add(c)
  node = 0
  word = ""
  return processed_text
