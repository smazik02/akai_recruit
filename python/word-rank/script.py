from collections import Counter

#Wersja z wpisywaniem własnych zdań
sentences=[]
n=int(input("Ile zdań chcesz wpisać?\n"))
for i in range(n):
    word=str(input())
    sentences.append(word)

#Wersja z predefiniowaną tabelą, do wyboru do koloru
"""""
sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]
"""""

words=[]
for i in range(len(sentences)):
    temp=sentences[i].split()
    for j in range(len(temp)):
        words.append(temp[j].lower())

c = Counter(words).most_common(3)
print("Most common words in this list are:")
print('1. "',c[0][0],'" - ',c[0][1],sep="")
print('2. "',c[1][0],'" - ',c[1][1],sep="")
print('3. "',c[2][0],'" - ',c[2][1],sep="")