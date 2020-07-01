sentence = input('Enter your sentence to Spongebobify: ')

x = 0
spongesentence = []   #define variables to


for letter in sentence.lower():
    if x%2 == 0 and letter!='i' and x!= 0:
        upperLetter = letter.upper()
        spongesentence.append(upperLetter)
    else:
        spongesentence.append(letter)
    x +=1

print(''.join(spongesentence))


