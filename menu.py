from kuznyechick import encrypt, decrypt
def menu():
    while True:
        
        action = str(input("Выберите действие:\n 1 - Зашифровать текст\n 2 - Расшифровать текст\n 3 - Остановить программу\n Ваш выбор: "))
        
        if action == '1':
            file_name = str(input("Введите путь к файлу с текстом для зашифрования: "))
            key = str(input("Введите ключ длиной 256 бит/32 латинских символа: "))
            encrypt(file_name, key)

        if action == '2':
            file_name = str(input("Введите путь к файлу с текстом для расшифрования: "))
            key = str(input("Введите ключ длиной 256 бит/32 латинских символа: "))
            decrypt(file_name, key)

        if action == '3':
            break

menu()            

        



