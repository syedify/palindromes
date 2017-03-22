from app import parse_palindrome as parser 
from app import app

#Set the path and key to the custom dataset to use this API
file_name = "app\\testset2.txt"
key = "key"
l,c = parser.data_file_parser(file_name, key)

@app.route('/')
def index():
	return "Palindone API"

@app.route('/palindromes')
@app.route('/palindromes/')
def get_palindromes():
	return '</br>'.join(l)
	
@app.route('/palindromes/count')
@app.route('/palindromes/count/')
def get_palindromes_count():
    return (str(c))

if __name__ == '__main__':
	pass