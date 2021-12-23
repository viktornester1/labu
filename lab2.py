text = 'abcdefghijklmnopqrstuvwxyzaABCDEFGHGKLMNOPQRSTUVWXYZабвгґдеєжзиіїйклмнопрстуфхцчшщьюяаАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
no = set(['як', 'від', 'до', 'за', 'для', 'є', 'у', 'хто', 'що', 'чий', 'чиє', 'чия', 'тут', 'і', 'але', 'бо', 'над', 'ні', 'то', 'так', 'той', 'що', 'та', 'яка', 'ці', 'цей', 'ця', 'у', 'в'])
while True:
    inp = str(input("Input text"))
    choice = input("Choose operation 'a' or 'b': ")
    if choice == 'a':
        temp_list = []
        print("Count of separate letters: ")
        for i in inp:
            if i in text:
                count = inp.count(i)
                if i not in temp_list:
                    temp_list.append(i)
                    print(i, ': ', count)
    elif choice == 'b':
        temp_list = []
        words = [word.lower() for word in inp.split()]
        words.sort()

        print("The sorted words are:")
        for word in words:
            if word not in temp_list:
                temp_list.append(word)
                if word not in no:
                    print(word)

    else:
        print("Wrong operation")
