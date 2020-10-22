# PracticalAttackAgainstRC4_DPROT

In this section we propose a easy-to-implement key-recovery attack against a particular mode of operation of RC4. We need several assumptions to launch a successful attack:

- The initialization value iv is a 3-byte counter prepended to a 13-byte long-term key, making a 16-byte string that is used as the actual RC4 key.

- The iv is incremented in every new encryption.

- RC4 is used in a communication system to send some well-structured packets with a constant header of at least one byte m[0] .

- The attacker has access to many encryptions, so that he can wait for the use of some specific iv values.

The previous assumptions can be fulfiled in some systems implementing handshake packets encrypted with RC4.

Practical work:

- From the description of the key scheduling phase of RC4, show that using iv=01 FF x results with high probability in a keystream first byte equal to x+2 , for any byte x .

- Use it to recover the first (fixed) byte of the encrypted message m[0] . This would require a trial-and-error process, testing all possible values of m[0] and computing how often the first keystream value is equal to . Then, the most likely value for m[0] is the one with the highest frequency.

- Show now that the first keystream byte produced with iv=03 FF x is, with a noticeable probability, x+6+k[0] , where k[0] denotes the first byte of the long-term key. Similarly, iv=04 FF x produces the first keystream byte equal to x+10+k[0]+k[1] , and so on.

- Put the previous ideas in practice to learn the first two bytes of the long-term key. To do that, generate a 13-byte random key and a one-byte random message (the message header suffices to perform the attack). Then, use the previous special values of iv to generate the encrypted byte for all 256 values of x , and use frequencies to detect the most probable value for m[0] , then k[0] and finally k[1] .

------------------------------------------------------------------------------------------------------------------------------

The bash scryt generates a text file with the encrypted bytes (you should generate 3, one for each IV detailed in the exercice). The python file reads the 3 text files, and decrypt the first byte of the messag eand the first two bytes of the key. If you want to try the python file, you can use the txt files as an example. 