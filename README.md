# Deciphering cryptography
Python code to decipher the Caesar Cipher and the Vigenère Cipher. 


**Decoding the Caesar Cipher**

The Caesar Cipher shifts all of the letters in a word by a certain offset. For example, with an offset of 3 and a message of "hello", the message will be encrypted by shifting each letter 3 places to the left (with respect to the alphabet). So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". The coded message will be "ebiil"!

Two functions are defined `decoder(message, offset)` and `coder(message, offset)`, which can be used to quickly decode and code messages given any offset.

Even without knowing the shift value, we can try all 26 different shifts to find the one comprehensible output. 


**Decoding the Vigenère Cipher**

The Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword. For example, encrypt the word “HELLO” using the keyword “KEY”. First, repeat the keyword to match the length of the plaintext: “KEYKE”. Then, find the corresponding letters in the Vigenère square. The letter ‘H’ is shifted by ‘K’, resulting in ‘S’. ‘E’ is shifted by ‘E’, resulting in ‘X’. ‘L’ is shifted by ‘Y’, resulting in ‘M’. And so on. The encrypted message would be “SXMMR”.
