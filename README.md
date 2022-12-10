# web_fuzz
Just a tiny endpoint detection using wordlist.

fuzzing
---------

python3 fuzz.py

encoder
----------

python3 encoder.py "Write-Output 'Hello World!'"


CertUtil -encode "Write-Output 'Hello World!'" encoded_script.txt


CertUtil -decode encoded_script.txt decoded_script.txt


CertUtil -encode "C:\Users\[Username]\Desktop\my_file.txt" encoded_file.txt

CertUtil -encrypt -pwd [Password] -f "C:\Users\[Username]\Desktop\my_file.txt" encrypted_file.txt

CertUtil -decrypt -pwd [Password] -f encrypted_file.txt decrypted_file.txt

