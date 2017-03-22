						Palindrome API Readme

===================================================================================
API Usage
===================================================================================
Call for list of palindromes: GET /palindromes
Call for list of palindromes: GET /palindromes/count


===================================================================================
Test Setup
===================================================================================
Setup Flask Server:
1) Install Flask in the root directory of the project as highlighted in [1]
2) The directories are already made so skip that step
3) Run the server: $ flask\Srcipts\python run.py
4) Open up browser http://localhost:5000/, a welcome message is visible

The test.py is a test runner which runs through the data sets in testset1, testset2,
and testset3. Testset1 covers just a list of palindromes in JSON text. Testset2 inserts
random garbage on different lines. Testset3 tests recursive calls of the search, false
paths and nested entries of the JSON file.

===================================================================================
Test Coverage
===================================================================================
Functional Tests:
1) Go to app directory
2) Open and run test.py

REST API Tests:
1) Setup the flask server
2) Go to http://localhost:5000/
3) Get a list of palindromes: http://localhost:5000/palindromes
4) Get a count of palindromes: http://localhost:5000/palindromes/count


Referece:
[1] https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world