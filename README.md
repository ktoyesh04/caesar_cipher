# Caesar Cipher
This is a simple implementation of the Caesar Cipher encryption and decryption algorithm in Python. The Caesar Cipher is a substitution cipher that shifts the letters of the alphabet by a certain number of positions down the alphabet.

## Description
It takes a plain-text message as input along with the shift value and direction of cipher (encrypt or decrypt) specified by the user. The program then shifts each letter of the message by the specified shift value and returns the encrypted or decrypted message.

The code uses a simple algorithm to shift the letters. First, it checks whether the letter is upper or lowercase, then applies the shift value to the ASCII value of that letter, and finally converts the resulting ASCII value back to a character


## Usage
To use this program, simply run caesar_cipher.py and follow the instructions on the command line. You can choose to either encrypt or decrypt a message and specify the number of positions to shift the letters.
![image](https://user-images.githubusercontent.com/124575344/229275961-8a9c9659-bd61-433c-8cdf-7975bd8348a3.png)

## Example
Here is an example of encrypting the message "hello world" with a shift of 3:
![image](https://user-images.githubusercontent.com/124575344/229275987-4d17d550-ecbe-4f9a-9fa3-11b0b91a22ee.png)

## Future Improvements
This implementation is a simple command line tool and could be improved with a user interface, better input validation, and more robust error handling. Additionally, the algorithm could be extended to support more complex characters and languages beyond the English alphabet.
