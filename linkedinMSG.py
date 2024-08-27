# fileSelection = input("Pick a template: Fordham, Loyola, Random\n>>>")
fileSelection = 'Random'
if fileSelection == 'Fordham':
    file = '/Users/Pedro/Desktop/Job Ish/fordham_ro'
elif fileSelection == 'Loyola':
    file = '/Users/Pedro/Desktop/Job Ish/loyola_ro'
else:
    file = '/Users/Pedro/Desktop/Job Ish/rando_ro'
userName = 'Pedro Vincenty'
name = userName.index(' ')
firstName = userName[:name]
prospect = input("Who\'s your prospect?\n>>>")
company = input("Enter prospect\'s company\n>>>")
company = company + "?"

f = open(file,'r')
filedata = f.read()
f.close()


char_to_replace = {'prospect': prospect, 'userName': userName, 'xyzCompany?': company,'userFirstName':firstName}

# Iterate over all key-value pairs in dictionary 
for key, value in char_to_replace.items():
    # Replace key character with value character in string
    filedata = filedata.replace(key, value)
print("\n")    
print(filedata)



