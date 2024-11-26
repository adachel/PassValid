def pass_valid(password):
    result = False
    dataEn = "qwertyuiopasdfghjklzxcvbnm"
    dataInt = "1234567890"
    dataSym = "~!?@#$%^&*_-+()[]{}></\\|'.,:;"

    count_int = False
    count_up = False
    count_low = False
    count_sym = False

    for i in password:
        if i in dataInt:
            count_int = True
        elif i in dataEn.upper():
            count_up = True
        elif i in dataEn:
            count_low = True
        elif i in dataSym:
            count_sym = True

    if count_int and count_up and count_low and count_sym and len(password) >= 8:
        result = True

    return result


print("Пароль должен содержать не менее 8 символов, содержать цифры, содержать прописные и строчные буквы")
passMy = input("Введите пароль\n")

if pass_valid(passMy):
    print("Успех")
else:
    print("Пароль не соответствует требования")
