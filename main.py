import time
import hashlib as hasher

print('Sha256: Her metni 64 karakterlik şifrelenmiş yazıya dönüştürür -Seçmek için 1- \n')
print('Md5: Girilen verinin boyutundan bağımsız olarak, 128-bit özet değeri üretir -Seçmek için 2-')
inp = input('Şifreleme türünü seçin: \n')

if inp == "1":
    sif = hasher.sha256()
    tx = input('Şifrelenecek metni giriniz: ')
    sif.update(tx.encode('utf-8'))
    hsh = sif.hexdigest()
    time.sleep(2)
    print(hsh)
    time.sleep(30)
elif inp == "2":
    sif = hasher.md5()
    tx = input('Şifrelenecek metni giriniz: ')
    sif.update(tx.encode('utf-8'))
    hsh = sif.hexdigest()
    time.sleep(2)
    print(hsh)
    time.sleep(30)
else:
    print('Yanlış seçim yaptınız')
    time.sleep(2)
