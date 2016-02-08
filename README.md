#Word Generator

Generator of possible answers for a word game

##Launch
You have some alphabet with not necessarily unique letters, some required word length and a dictionary. The script comes with two dictionaries 'russian' and 'russian2'.
Then you just running the script and getting possible words.

```
./word_generator.py -denglish.noun --length=6 --alphabet=onfgclniecso | sort | uniq
coolie
cosine
ensign
gonion
insole
isogon
legion
lesion
logion
nelson
oscine
sconce
single

./word_generator.py -drussian --length=6 --alphabet=даннспсирётв
нарпит
пиастр
радист
расист
садист
спринт
```

##Dictionaries
English dictionary was generated from WordNet database of http://wordnet.princeton.edu/wordnet
```
egrep -o "^[0-9]{8}\s[0-9]{2}\s[a-z]\s[0-9]{2}\s[a-zA-Z_]*\s" data.noun | cut -d ' ' -f 5 > english.noun
egrep -o "^[0-9]{8}\s[0-9]{2}\s[a-z]\s[0-9]{2}\s[a-zA-Z_]*\s" data.adv | cut -d ' ' -f 5 > english.adv
```
