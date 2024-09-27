#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




with open("Input/Names/invited_names.txt") as name_text:
    name_list = name_text.readlines()
clean_name_list = []
for i in name_list:
    clean_name_list.append(i.replace('\n',""))
print(clean_name_list)
for name in clean_name_list:
    with open("Input/Letters/starting_letter.txt") as letter_text:
        letter = letter_text.read()
    new_letter = letter.replace("[name]",name)
    with open(f"Output/ReadyToSend/{name}.txt",mode="w") as output_text:
        output_text.write(new_letter)


