#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Obiettivo dello homework è leggere alcune stringhe contenute in una serie di
file e generare una nuova stringa a partire da tutte le stringhe lette.
Le stringhe da leggere sono contenute in diversi file, collegati fra loro a
formare una catena chiusa. Infatti, la prima stringa di ogni file è il nome di
un altro file che appartiene alla catena: partendo da un qualsiasi file e
seguendo la catena, si ritorna sempre nel file di partenza.

Esempio: il contenuto di "A.txt" inizia con "B.txt", il file "B.txt", inizia
con "C.txt" e il file "C.txt" inizia con "A.txt", formando la catena
"A.txt"-"B.txt"-"C.txt".

Oltre alla stringa con il nome del file successivo, ogni file contiene anche
altre stringhe separate da spazi, tabulazioni o caratteri di a capo. La
funzione deve leggere tutte le stringhe presenti nei file della catena e
costruire la stringa che si ottiene concatenando i caratteri con la più alta
frequenza in ogni posizione. Ovvero, nella stringa da costruire, alla
posizione p ci sarà il carattere che ha frequenza massima nella posizione p di
ogni stringa letta dai file. Nel caso in cui ci fossero più caratteri con
la stessa frequenza, si consideri l'ordine alfabetico.
La stringa da costruire ha lunghezza pari alla
lunghezza massima delle stringhe lette dai file.

Quindi, si deve scrivere una funzione che prende in ingresso una stringa A 
che rappresenta il nome di un file e restituisce una stringa.
La funzione deve costruire la stringa secondo le indicazioni illustrate sopra
e ritornare le stringa così costruita.

Esempio: se il contenuto dei tre file A.txt, B.txt e C.txt nella directory
test01 è il seguente

test01/A.txt          test01/B.txt         test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite                                                                       
garden                park                 hello                                                                       
kitchen               affair               portrait                                                                     
balloon                                    angel                                                                                                                                               
                                           surfing                                                               

la funzione most_frequent_chars("test01/A.txt") dovrà restituire la stringa
"hareennt".
'''
def most_frequent_chars(filename: str) -> str:
	start_file = filename
	next_file = ''
	contents = []
	max_len = 0
	while start_file != next_file:
		with open(filename, encoding='utf8') as f:
			righe = f.read().split()
			i = 0
			while i < len(righe):
				if i == 0:
					next_file = righe[i]
					filename = next_file
				else:
					max_len = max_string_length(righe[i], max_len)
					contents.append(righe[i])
				i += 1
	return max_freq_by_pos(sort_chars_by_pos(contents, max_len))
	pass
	
def max_string_length(string: str, max_length: int) -> int:
	if len(string) > max_length:
		return len(string)
	else:
		return max_length
	pass
	
def	sort_chars_by_pos(strings: list, str_len: int) -> list:
	sorted_chars = []
	i = 0
	while i < str_len:
		temp_str = ''
		for s in strings:
			if i < len(s):
				temp_str += s[i]
		sorted_chars.append(temp_str)
		i += 1
	return sorted_chars
	pass
	
	
def max_freq_by_pos(strings: str) -> str:
	output = ''
	i = 0
	while i < len(strings):
		max_freq = {}
		for c in sorted(strings[i]):
			max_freq[c] = max_freq.get(c, 0) + 1
		output += max(max_freq, key=max_freq.get)
		i += 1
	return output
	pass
	
###############################################################################
if __name__ == '__main__':
    print(most_frequent_chars('test01/A.txt'))
    print(most_frequent_chars('test02/misappropriated.txt'))
    print(most_frequent_chars('test03/bitchily.txt'))
    print(most_frequent_chars('test04/parasites.txt'))
    print(most_frequent_chars('test05/angel.txt'))
    print(most_frequent_chars('test06/cassias.txt'))
    print(most_frequent_chars('test07/madness.txt'))
    print(most_frequent_chars('test08/wolf.txt'))
    print(most_frequent_chars('test09/barest.txt'))
    print(most_frequent_chars('test10/affirmations.txt'))
    print(most_frequent_chars('test11/aberrations.txt'))
    print(most_frequent_chars('test12/couch.txt'))
        
