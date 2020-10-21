#!/bin/bash

IV=01FF00
#KEY=00010203040506070809101112
#KEY=7e1a0bbc8c770667be44dce10c
KEY=3c4a70ab8ce5073e1d9c900998

#echo " Les variables son  IV $IV i KEY $KEY"

#echo -n 'Hello World!' | openssl enc -K '01FF0300010203040506070809101112' -rc4 | xxd

#echo -n 'Hello World!' | openssl enc -K "$IV$KEY" -rc4 | xxd

output=resultatsXifrats3M.txt

ivin=327424

for i in {1..256}
do 
    #printf -v ivinhex "%02x" "$ivin"
    ivinhex=$(printf %02x $ivin)
    #echo $ivinhex
    #echo -n 'H' | openssl enc -K '01FF0000010203040506070809101112' -rc4 | xxd
    #echo -n 'H' | openssl enc -K "0$ivinhex$KEY" -rc4 | xxd
    echo -n 'M' | openssl enc -K "0$ivinhex$KEY" -rc4 | xxd >> $output
    #echo -n 'Hello World!' | openssl enc -K "0$ivinhex$KEY" -rc4 -P
    iv2=$(( $ivin + 1 ))
    #echo $iv2
    ivin=$iv2
    #echo $ivin
    #echo -n 'Hello World!' | openssl enc -K "$IV$KEY" -rc4 | xxd
done