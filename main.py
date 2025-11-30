def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = 'A' if 'A' <= char <= 'Z' else 'А'
            else:
                base = 'a' if 'a' <= char <= 'z' else 'а'
            
            char_code = ord(char) - ord(base)
            shifted_code = (char_code + shift) % 32
            encrypted_text += chr(ord(base) + shifted_code)
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Шифратор Цезаря")
    print("===============")
    
    while True:
        print("\n1. Зашифровать текст")
        print("2. Расшифровать текст") 
        print("3. Выйти")
        
        choice = input("Выберите действие (1-3): ")
        
        if choice == "1":
            text = input("Введите текст для шифрования: ")
            shift = int(input("Введите ключ (число): "))
            result = caesar_encrypt(text, shift)
            print(f"Зашифрованный текст: {result}")
            
        elif choice == "2":
            text = input("Введите текст для расшифровки: ")
            shift = int(input("Введите ключ (число): "))
            result = caesar_decrypt(text, shift)
            print(f"Расшифрованный текст: {result}")
            
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
