g= ' Ünlü deterjan markası Arielin reklamı hakkında Ticaret Bakanlığına yapılan şikayet bir gerçeği gözler önüne serdi. Markanın reklamında 1 ölçekte temizlendiğini iddia ettiği leke, bakanlığın yaptığı testte 8 yıkamada çıktı. Rakip ürünlere göre az deterjanla daha iyi temizlik sağladığını ileri süren şirket, yanıltıcı reklam nedeniyle 2,2 milyon lira para cezasına çarptırıldı.'
kelimeler=g.split(' ')

def donustur(a):
    sayac = []
    for kelime in a:
       print(kelime)
       sayici = 0
       for harf in range(len(kelime)):
        sayici+=1
       print(sayici)
       sayac.append(sayici)
    return sayac
b = donustur(kelimeler)
print(b)