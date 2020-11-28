from flask import Flask, request, render_template

app = Flask(__name__)

#Modified Prefix Structure for Natural Language Processing

#-------------GLOBAL VARIABLES------------------------------------------------------------
node = 0 #Number of nodes, the root node is node 0
tree = [{}] #Tree itself
valWord = [{}] #Set of the most frequent valid words
freq = [{}] #Frecuency of Node i
isWord = [{}] #Boolean value set true if the current node is a complete word
word = "" #Current word that it's written
#-----------------------------------------------------------------------------------------

#------------SEARCHING AND ADDING FUNCTIONS-----------------------------------------------
def find(curnode, curword): #Searhces for all valid words
    if curnode in isWord: #If current node is an actual word
        valWord[curword] = freq[curnode]
    for nxt in tree[curnode]: #Recursively finds other valid words
        find(nxt[0], curword + nxt[1])
    return
def add(c): #Updates the 'word' by appending 'c' to the end, and searches for new valid words
    if not isalpha(c):
        freq[node] += 1
        isWord[node] = True
        word = ""
        #Clean text box
        return
    if c in tree[node]:
        node = tree[node][c]
        word += c
    else :
        tree[node][c] = node + 1
        node += 1
        tree[node] = {}
        freq[node] = 1
        isWord[node] = False
        word += c
    valWord.clear()
    find(node, word)
    return

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['input']
	processed_text = text.upper()
	print(processed_text)
	if len(word) > 1:
		mostFreq = sorted(valWord) #Sorts the valwords by their frequency
		need = 5 #Prints up to 5 words
		for i in mostFreq: #From the most frequent one to the least frequent one
			if need == 0: #5 words have are already been printed
				break
				#print(i[0])
				need -= 1

	return processed_text

