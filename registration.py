from user import User

user = User()

user.register("james", "08009", "testemail.com", "abc")

email = input("Enter Your email ")
password = input("Enter Your password ")

print(user.login(email, password))