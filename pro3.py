def counter(sample):
    vowels='aeiouAEIOU'
    vowel=0
    consonant=0
    for char in sample:
        if char.isalpha():
            if char in vowels:
                vowel+=1
            else:
                consonant+=1
    return vowel,consonant
sentence=input("Enter the sentence:")
vowel,consonant=counter(sentence)
print('number of vowels:',vowel)
print('number of consonants:',consonant)
