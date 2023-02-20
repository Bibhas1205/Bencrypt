# Bencrypt
Byte encryption tool

Examples:  python3 bencrypt.py [100,101] test.txt

![Screenshot (73)](https://user-images.githubusercontent.com/125908181/220179490-ad54e090-a995-46ed-a6b0-1eaa2f545edf.png)


Remember the list values should be less than equls to 255. It is mandatory. Example [0,100,200,255]


To decode You should run the same command but the list should be reversed. Exampple [100,101] => [101,100]

Encode :  python3 bencrypt.py [100,101] test.py

Decode :  python3 bencrypt.py [101,100] test.py
