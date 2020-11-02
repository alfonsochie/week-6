def login (user,username,password):
    for items in user:
        if username == items:
            if password == user[items]:
                return True
        else:
            return False

print (login({'user1':'password1','user2':'password2'},'user4','password1'))


