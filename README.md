# Authentication-System

Hey
This is a basic Django project to make an Authentication system with the following features:

1. I've linked the proejct to my SQL database after creating a db consisting of a table named Users which will be used to store user information.
2. I've created 4 APIs with the following function:

Signup API: Accepts user info (name, email, password, dob) and stores it in the database.
Login API: Allows user to sign in after verifying email and password that the user enters, and giving them a JWT token.
View Details API: Allows user to view their details, using their JWT token, which is given to them during Login.
Update API: Allows user to update their details, which are also updated in the database.

3. This system uses API View and mainly works with GET, POST, PUT requests.
