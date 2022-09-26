
'''
#The DB
partsDB = []

#An individual part
parts = []

#A 'dictionary' with index of attributes
partAttr = ['company_part_no', 'manufact_part_no', 'description', 'cost', 'on_hand', 'needed', 'lead_time']

#attIdx = partAttr.index('company_part_no')
#print(attIdx)

while True:
    #Iterate through attributes, prompting input from user for information and add to part list
    for attrib in partAttr:
        item = input(f'{attrib}: ')
        parts.insert(partAttr.index(attrib), item)
    #Append the part to the parts db
    partsDB.append(parts.copy())
    #prompt user to continue entering parts or quit
    another = input('Another part? "Y" to continue "Q" to quit: ')
    if another.casefold() == 'q':
        break

print(partsDB.__len__())
print(partsDB)
'''

#Continuation from week 3 problem
def menu():
    print('******************************')
    print('\tPART DATABASE')
    print('******************************')
    print('Options: ')
    print('1. Create a record')
    print('2. Delete a record')
    return (input('Insert number corresponding to option: '))

def createPart():
    parts = []
    #A 'dictionary' with index of attributes
    partAttr = ['company_part_no', 'manufact_part_no', 'description', 'cost', 'on_hand', 'needed', 'lead_time']
    for attrib in partAttr:
        item = input(f'{attrib}: ')
        parts.insert(partAttr.index(attrib), item)
    print()
    
    return parts
    
#The DB
partsDB = []

#the looping menu
while True:
    choice = menu()
    if choice == '1':
        partsDB.append(createPart())
