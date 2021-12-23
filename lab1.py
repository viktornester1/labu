def ceasar():
    a = '01234567890abcdefghijklmnopqrstuvwxyzaABCDEFGHGKLMNOPQRSTUVWXYZAабвгґдеєжзиіїйклмнопрстуфхцчшщьюяаАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯА'
    result = ''

    text = input("Enter text")
    for i in text:
        if i in a:
            position = a.find(i)
            newposition = position + 1
            if i in a:
                result = result + a[newposition]
            else:
                result = (' ', result + i)

    encrypted = result
    result = ''
    print(encrypted)


ceasar()



