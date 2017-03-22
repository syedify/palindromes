#!/Python34/python

import json
import string

"""
Search through the dictionary based on the key. If the matched
value is a dictionary, search it otherwise return the value.
Recursively perform dictionary searches until key is found.

@params: 	node - the next node in the dicitonary to search
			key	 - the matching key to search against
@return:	the value which matches the key in the dict
"""
def json_search(node, key):
	
	if isinstance(node, dict):
		if key in node:
			#If the found value is a dicitonary, perform another search
			if isinstance(node[key], dict):
				return json_search(node[key], key)
			else:
				return node[key]	

		for child in node.values():
			return json_search(child, key)
"""
Convert the value to a string and clean it (remove whitespace,
punctuation and fix case).Invert the string an test the inversion.

@params: 	val 	- the value to check palindrome
@return:	bool	- True if val is a palindrome
"""
def check_palindrome(val):

	s = str(val).replace(" ","").lower()
	#Remove all punctuation
	s_clean = s.translate(s.maketrans('','', string.punctuation))
	#Invert the string
	s_invert = s_clean[::-1]
	return s_clean == s_invert

"""
Open a streaming parser for a file with file_name. Take each line
and search the string using the provided key. If a match is found
check if it is a palindome and add to the list. Return after all
the file has been parsed.

@params:	file_name 	- name of the file to parse
			key 		- the matching id to look for palindrome
@return:	results 	- list of palindrome in file
			count		- count of matching lines
"""
def data_file_parser (file_name, key):
	json_data = {}
	results = []
	
	try:
		with open (file_name) as f:
			for line in f:
				#The loads function will throw a ValueError if the
				#string is not JSON formatted.
				try:
					json_data = json.loads(line)
					
					#If no match then the result is None
					result = json_search(json_data, str(key))

					if result != None and check_palindrome(result):
						results.append(result)
				except ValueError:
					# Fails if the string is not a JSON string
					pass
	except Exception as e:
		print("Error occured: {}".format(e))

	count = len(results)
	return results, count

if __name__ == '__main__':
	pass
