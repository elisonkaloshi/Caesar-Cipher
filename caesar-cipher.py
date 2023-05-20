def selected_mode():
    print("===========================")
    print("Options")
    print("1. Encrypt")
    print("2. Decrypt")
    print("===========================")

    while True:
        mode = int(input("[+] Choose Options:"))

        if mode == 1:
            print("===========================")
            print("[+] Encryption mode started")
            print("===========================")

            return 'encrypt'
        elif mode == 2:
            print("===========================")
            print("[+] Decryption mode started")
            print("===========================")

            return 'decrypt'
        else:
            print("===========================")
            print("[-] Please enter the correct option")
            print("===========================")


def secret_message():
    return input("[+] Enter your secret message: ")


def encryption_key():
    return int(input("[+] Enter your encryption key: "))


def translate_message():
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_ndex = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                translated_index = symbol_ndex + key
            elif mode == 'decrypt':
                translated_index = symbol_ndex - key

            if translated_index >= len(SYMBOLS):
                translated_index = translated_index - len(SYMBOLS)
            elif translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)

            translated = translated + SYMBOLS[translated_index]
        else:
            translated = translated + symbol

    return translated


mode = selected_mode()
message = secret_message()
key = encryption_key()

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

print("===========================")
print("[+]", translate_message())
print("===========================")
