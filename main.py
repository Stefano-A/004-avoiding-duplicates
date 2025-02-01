user_list = []

user_input = input('insert a string (insert a blank line to stop): ')
while user_input != '':
    user_list.append(user_input)
    user_input = input('insert a string (insert a blank line to stop): ')

no_duplicate_list = list(dict.fromkeys(user_list))

for words in user_list:
    print(words)

print('')

for words in no_duplicate_list:
    print(words)