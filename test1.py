#Britney Huiracocha
#Take-home test for Unit 1

#Step-by-step


# 1. Have your program check the
# word 'coronavirus' itself and report what unique letters it contains.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
longword = 'coronavirus'
for word in alphabet:
        if word in longword:
             print(longword, 'contains' ,word)

# 2. Generate a series of questions of the form, "Can X treat Y?"
x_medications =['remdesivir','hydroxychloroquine','kaletra','favipiravir']
y_diseases = ['coronavirus','hepatitis','malaria','influenza']
for x in x_medications:
    for y in y_diseases:
        print ('Can',x,'treat',y,'?')

# 3.In this step, your program will search for common letters in some words that were
# uncommon before the coronavirus outbreak.
# Take each letter in the word 'coronavirus' and report whether each letter also exists in each medication from the list of medications in step 2 above.
for word in alphabet:
        if word in longword:
            for x in x_medications:
                if word in x:
                    print(word, 'is in',longword,'and also in',x)
