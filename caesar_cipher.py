def caesar_cipher(original_text, shift, direction):
    if direction == "decrypt":
        shift *= -1
    final_text = ""
    for char in original_text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr((ord(char)-97+shift)%26+97)
            else:
                shifted_char = chr((ord(char)-65+shift)%26+65)
            final_text += shifted_char
        else:
            final_text += char
    return final_text

text = input("Enter the text: ")
shift = int(input("Shift: "))
direction = input("Enter encrypt/decrypt: ")
print(caesar_cipher(text, shift, direction))
