# SEN5105
SEN5105 - Final Exam

1. CAESAR CIPHER (caesarcipher.py)

The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by a certain number of places in the alphabet. We call the length of shift the key. For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the opposite direction. This program lets the user encrypt and decrypt messages according to this algorithm.

When you run **caesarcipher.py**, the output will look like this:


- Do you want to (e)ncrypt or (d)ecrypt? 
- e
- Please enter the key (0 to 25) to use.
- 4
- Enter the message to encrypt.
- Meet me by the rose bushes tonight.
- QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
- Full encrypted text copied to clipboard.

or

- Do you want to (e)ncrypt or (d)ecrypt? 
- d
- Please enter the key (0 to 26) to use.
- 4
- Enter the message to decrypt.
- QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
- MEET ME BY THE ROSE BUSHES TONIGHT.
- Full decrypted text copied to clipboard.

---------------

2. TRIVIA GAME (triviagame.py)

In this programming exercise, you will create a simple trivia game for two players. The program will work like this:

- Starting with player 1, each player gets a turn at answering 5 trivia questions. (There should be a total of 10 questions.) When a question is displayed, 4 possible answers are also displayed. Only one of the answers is correct, and if the player selects the correct answer, he or she earns a point.
- After answers have been selected for all the questions, the program displays the number of points earned by each player and declares the player with the highest number of points the winner.

To create this program, write a Question class to hold the data for a trivia question. The Question class should have attributes for the following data:

- A trivia question
- Possible answer 1
- Possible answer 2
- Possible answer 3
- Possible answer 4
- The number of the correct answer (1, 2, 3, or 4)

The Question class also should have an appropriate __init__, method, accessors, and mutators.

The program should have a list or a dictionary containing 10 Question objects, one for each trivia question. Make up your own trivia questions on the subject or subjects of your choice for the objects.

---------------

3. PATIENT SYSTEM (patientsystem.py)

Write a class named Patient that has attributes for the following data:

- First name, middle name, and last name
- Address, city, state, and ZIP code
- Phone number
- Name and phone number of emergency contact

The Patient class’s __init__ method should accept an argument for each attribute. The Patient class should also have accessor and mutator methods for each attribute. Next, write a class named Procedure that represents a medical procedure that has been performed on a patient. The Procedure class should have attributes for the following data:

- Name of the procedure
- Date of the procedure
- Name of the practitioner who performed the procedure
- Charges for the procedure

The Procedure class’s __init__ method should accept an argument for each attribute. The Procedure class should also have accessor and mutator methods for each attribute. Next, write a program that creates an instance of the Patient class, initialized with sample data. Then, create three instances of the Procedure class, initialized with the following data:

![image](https://github.com/Kbgezmisoglu/SEN5105/assets/97810764/a7366cf4-b4f8-4a92-8b2a-99b8c4a10cca)

The program should display the patient’s information, information about all three of the procedures, and the total charges of the three procedures.
