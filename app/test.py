import parse_palindrome as parser 
import os


def main():

	#Prompt user for custom datasets
	custom_data = input("Enter custom dataset for testing... ")
	custom_key = input("Enter key for custom dataset... ")

	
	#Run custom tests if configured or run preset tests
	if (custom_key != "" and custom_data != ""):
		data_path = os.path.join(os.getcwd(), custom_data)

		print("=============================================================")
		print("Running custom data set: {} with Key:{}".format(custom_data, custom_key))
		print("=============================================================")
		
		li, count = parser.data_file_parser(data_path, custom_key)
		for l in li:
			print (l)
		print(count)

	else:
		#Get the path to the testing datasets
		data1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testset1.txt')
		data2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testset2.txt')
		data3 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testset3.txt')

		#Set key value for testing data sets
		key = 'key'
		

		"""
		Test set 1 tests if the parser can extract a line, extract the JSON,
		perform a level 1 search and compute a list and count of palindromes
		"""
		print("=============================================================")
		print("Running data set 1")
		print("=============================================================")
		li, count = parser.data_file_parser(data1, key)
		for l in li:
			print (l)

		print(count)

		"""
		Test set 2 tests if the parser can extract a line, check if it is valid
		JSON and extract it, perform a level 1 search and compute a list and 
		count of palindromes
		"""
		print("=============================================================")
		print("Running data set 2")
		print("=============================================================")
		li, count = parser.data_file_parser(data2, key)
		for l in li:
			print (l)

		print(count)
		
		"""
		Test set 3 tests if the parser can extract a line, check if it is valid
		JSON and extract it, perform a multi level search and compute a list and 
		count of palindromes
		"""
		print("=============================================================")
		print("Running data set 3")
		print("=============================================================")
		li, count = parser.data_file_parser(data3, key)
		for l in li:
			print (l)

		print(count)

if __name__ == '__main__':
	main()