
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

#put the attribute list global for use by all methods needed
partAttr = ['Company Part #', 'Manufacturer\'s Part #', 'Description', 'Cost', 'Amt On Hand', 'Amt Needed', 'Lead Time']

#menu function for basic UI
def menu():
    print('******************************')
    print('\tPART DATABASE')
    print('******************************')
    print('Options: ')
    print('1. Create a record')
    print('2. Delete a record')
    print('3. Search for a record')
    print('4. Print Database records')
    print('5. Exit')
    return (input('Insert number corresponding to option: '))

#function to create a part item from user input and return it
def createPart():
    parts = []
    for attrib in partAttr:
        item = input(f'{attrib}: ')
        parts.insert(partAttr.index(attrib), item)
    print()
    
    return parts

#delete a part by company part #
def deletePart(partsDB):
    part_num = input('Enter the company part number for the deletion: ')
    for record in partsDB:
        if record[0] == part_num:
            partsDB.remove(record)

#Search function by company part # or manufacturer part #
def searchPart(partsDB):
    print()
    print('1. Search by Company Part #')
    print('2. Search by Manufaturer\'s Part #')
    print('3. Return to main menu')
    choice = input('Enter number corresponding to search method: ')
    if choice == '1':
        company_partno = input('Enter the Company Part #: ')
        for record in partsDB:
            if company_partno == record[0]:
                print('Part Found')
                return record
    elif choice == '2':
        manufact_partno = input('Enter the Manufacturer\'s Part #: ')
        for record in partsDB:
            if manufact_partno == record[1]:
                print('Part Found')
                return record
    elif choice == '3':
        return None
    else:
        print('Invalid input, please enter 1 or 2: ')
        searchPart(partsDB)
            
#formatted print function
def pretty_print(records):
    print('\tPART DATABASE')
    print('\t-------------')
    for record in records:
        for i in range(len(record)):
            print(f'{i+1}. {partAttr[i]}: {record[i]}')
            
    print()
    
#The DB collection
partsDB = []
#A list of returned search records for other operations
searchRecords = []

#the looping menu
while True:
    choice = menu()
    if choice == '1':
        partsDB.append(createPart())
    elif choice == '2':
        deletePart(partsDB)
    elif choice == '3':
        record = searchPart(partsDB)
        if record is not None:
            searchRecords.append(record)
            pretty_print(searchRecords)
        else:
            print('No records found')
    elif choice == '4':
        pretty_print(partsDB)
    elif choice == '5':
        print('Closing program...')
        break
