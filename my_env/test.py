from flask import Flask, request, render_template

app = Flask(__name__)

#Modified Prefix Structure for Natural Language Processing

#-------------GLOBAL VARIABLES------------------------------------------------------------
node = 0 #Number of nodes, the root node is node 0
tree = [] #Tree itself
valWord = {} #Set of the most frequent valid words
freq = [] #Frecuency of Node i
isWord = [] #Boolean value set true if the current node is a complete word
word = "" #Current word that it's written
done = {None} 
#Words that predicts
words = [None] * 5

tree.append({})
freq.append(1)
isWord.append(False)
#-----------------------------------------------------------------------------------------

#------------SEARCHING AND ADDING FUNCTIONS-----------------------------------------------
#Searhces for all valid words
def find(curnode, curword):
  global isWord
  global valWord
  global tree
  global freq
  if isWord[curnode]:
    print(curnode, curword, isWord[curnode])
    valWord[curword] = freq[curnode]
    print(curnode, curword)
  for c in tree[curnode]:
    find(tree[curnode][c], curword + c)
  return
#Updates the 'word' by appending 'c' to the end, and searches for new valid words
def add(newWord):
  global tree
  global freq
  cur = 0
  for c in newWord:
    if c in tree[cur]:
      cur = tree[cur][c]
    else:
      tree[cur][c] = cur + 1
      cur += 1
      tree.append({})
      freq.append(1)
      isWord.append(False)
  return cur

@app.route('/')
def index():
  return render_template('index.html', word1 = words[0], word2 = words[1], word3 = words[2], word4 = words[3], word5 = words[4])

@app.route('/', methods=['POST'])
def my_form_post():
  global tree
  global node
  global word
  global valWord
  global isWord
  text = request.form['input']
  processed_text = text.upper()
  newNode = add(processed_text)
  isWord[newNode] = True
  done.add(processed_text)
  freq[newNode] += 1
  valWord.clear()
  find(newNode, processed_text)
  node = 0
  word = ""
  print(valWord)
  swords = sorted(valWord.items(), key=lambda x: x[1], reverse = True)
  i = 0
  for c in swords:
    if i >= 5: break
    if c[0] in done:
      words[i] = c[0]
    i += 1
  while i < 5:
    words[i] = None 
    i += 1
  return render_template('index.html', word1 = words[0], word2 = words[1], word3 = words[2], word4 = words[3], word5 = words[4])
