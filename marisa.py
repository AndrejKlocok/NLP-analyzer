#!/usr/bin/python3
'''  
 	Autor: Andrej Klocok, xkloco00@stud.fit.vutbr.cz
'''
import marisa_trie
import sys, argparse

# Ulozenie do struktury
def SaveToTrie(key, data, kind, info):
	b = info.encode('utf-8')
	key.append(kind)
	data.append(b)
	pass

# Najdenie slova (key) v trie strukture
def FindInTrie(trie, key):
	try:
		l = trie[key]
		return l
	except KeyError:
		return None

# Vypis hladaneho slova (key) vo formate "tvar:lema:tag:vzor"
def PrintTrie(trie, key):
	l = FindInTrie(trie, key)
	if(l is None):
		key = key.lower()
		l = FindInTrie(trie, key)
		if(l is None):
			print("Nenájdené>")
			return
	print("Tvar> " + key)

	for x in l:
		output = x.decode('utf-8')
		row = output.split("#")
		lemma = row[0]
		tag = row[1]
		pattern = row[3]
		print(key+":"+lemma+":"+tag+":"+pattern)
	pass

# Vytvorenie trie struktury zo subora inputfile v danom formate
def Iterate(inputFile):
	key = []
	data = []
	i = 0
	with open(inputFile, "r", encoding='utf-8') as file:
		line = file.readline()
		while(line):
			line = line[:-1]
			row = line.split("#")
			
			tmp = ""
			for x in row[1:]:
				tmp += x +"#"
			tmp = tmp[:-1]
			SaveToTrie(key, data, row[0], tmp)

			i+=1
			if(i%100000 ==0):
				print(i)
			line = file.readline()
	
	trie = marisa_trie.BytesTrie(zip(key,data))
	trie.save('corpora.marisa')
	pass

# Vypise napovedu
def PrintHelp(name=None):
	return'''usage: marisa.py [-h] marisa
  Morfologický analyzátor, ktorý číta vstupné slova z stdin.
  Využíva slovník, uložený v štruktúre marisa-trie.
  Vypisuje na stdout tvar:lema:tag:vzor.
	'''


def Main(argv):
	# ArgParser
	parser = argparse.ArgumentParser(usage=PrintHelp())
	parser.add_argument("marisa", help = "Cesta ku slovníku vo formáte marisa_trie.")

	args = parser.parse_args()
	# Nacitanie trie
	trie = marisa_trie.BytesTrie()
	trie.load(args.marisa)
	print("Morphological analyser")
	# Vstup
	for line in sys.stdin:
		for word in line.split():
			if(word == "."):
				sys.exit()
			PrintTrie(trie, word)

if __name__ == '__main__':
	Main(sys.argv[1:])