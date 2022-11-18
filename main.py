#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Solution:

# seperated names as list from invited_names.txt
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

# removed \n from the ending of all names
for i in range(len(names)):
    names[i] = names[i].replace('\n','')

print(names)

# seperated the letter present in example.txt file as a list based on lines
with open('./Input/Letters/starting_letter.txt') as file:
    letter = file.readlines()

print(letter)

# we have both names and letter as a list. Now used loop to take the names, loop through letter
# first line to replace the name and stored the new letter everytime with person_name.txt using open function
for i in names:
    letter[0] = letter[0].replace(letter[0][5:],f'{i},\n')
    with open(f'./Output/ReadyToSend/{i}.txt', mode = 'w') as new_file:
        for j in letter:
            new_file.write(j)



