#
# import getpass
#
# # Hard-coded correct PIN
# # set the correct pin by passing the value 1234 to variable correct_pin
# correct_pin = "1234"
#
# # Maximum number of attempts
# # This will compare the attempt value with this max number.
# # This is a variable and can be altered
# max_attempts = 3
#
# # Initialize attempt counter
# attempts = 0
#
# # Loop to take input, count number of attempts (ensure fewer than max) and check PIN
# while attempts < max_attempts:
#     # Prompt for PIN input
#     entered_pin = getpass.getpass("Enter your 4-digit PIN: ")
#     # entered_pin = input("Enter your 4-digit PIN: ")
#
#     # Check if entered PIN matches correct PIN
#     if entered_pin == correct_pin:
#         # you can add other conditions e.g. ..and entered_pin.isdigit() and len(entered_pin) == 4
#         print("Success! PIN accepted.")
#         break  # Exit loop on success
#     # Check if the supplied PIN matches the correct PIN
#     # Added one more if statement if the attempt is less than max_attempt
#     else:
#         attempts = attempts + 1
#         remaining_attempts = max_attempts - attempts
#         print("Incorrect PIN. Please try again. Attempts remaining:", remaining_attempts)
# # This adds one to the current attempt
# # you take the number of attempts + 1 from the max attempts to get the remaining attempts
# # Check if maximum attempts reached, if it is attempt 3 then show this following message
# if attempts == max_attempts:
#     print("You have exceeded the maximum number of attempts. Access denied.")

# Another method:
# for attempt in range(max_attempts):  # Ask the user to supply the PIN
#     supplied_pin = input("Please enter your PIN: ")
#     if supplied_pin == correct_pin:  # Check if the supplied PIN matches the correct PIN
#         print("PIN verification successful")
#         break
#     else:
#         attempts_remaining = max_attempts - attempt - 1
#     if attempts_remaining > 0:
#         print(f"Incorrect PIN. {attempts_remaining} attempts remaining.")
#     else:
#         print("No remaining attempts. Access denied.")
# Instead of remaining attempts = max - (attempts+1), this minuses 1 from max minus attempts

# -- LETICIA PIN CODE ---

# //////// WHILE LOOP ////////

# # EXERCISE 2 - Python Program that emulates the high-street mechanism for checking a PIN.
# #
# # def the correct pin
# desired_pin = 2489
# # def max attempts
# max_attempts = 3
# # initialise num of log in attempts
# attempts = 0
#
# # while loop is used to execute a set of statements as long it is true
# # while attempts is less than three from (0-3)
# while attempts < max_attempts:
#     # input prompts the user to enter pin as long
#     # int changes string values into integer and restricts user to only use integer values
#     supplied_pin = int(input("Enter your PIN: "))
#     # If user input a string = ValueError
#
#     # indented as the condition is a set of statement within a loop
#     # condition: if user input a pin that equals to desired pin
#     if supplied_pin == desired_pin:
#         # print the below string object in console - PIN successful
#         print('PIN successful')
#         # break t allows you to exit the loop
#         break
#
#     # else used to catch the amount of attempts the user has left
#     else:
#         # increment attempt by the value 1
#         # attempts = attempts + 1
#         # this increases the amount of the attempts by 1
#         attempts += 1
#         # to count the amount of attempts user has left
#         # everytime a user makes an attempt to input PIN, it takes 1 away from 3 which is the value of max attempts
#         remaining_attempts = max_attempts - attempts
#         # prints message of the remaining attempts left using f string
#         print(f"{remaining_attempts} attempts left")
#
# # conditional statement: if the attempts is equal to max attempts is TRUE
# if attempts == max_attempts:
#     # display string object to user
#     print('3 UNSUCCESSFUL ATTEMPTS. ACCOUNT LOCKED!')

