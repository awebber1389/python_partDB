import PartVersion as pvers

#put the attribute list global for use by all methods needed
partAttr = ['Company Part #', 'Manufacturer\'s Part #', 'Description', 'Cost', 'Amt On Hand', 'Amt Needed', 'Lead Time']
#The DB collection
partsDB = []

#List the part object templates for user
def showVersions():
    print("====Part Templates====")
    for template in pvers.templateList:
        for k,v in template.items():
            print(f'{k}: {v}')
        print()

#function to create a part item from user input and return it
def createPart():
    parts = dict()
    showVersions()
    versionNum = input('\nInsert the number of the template you wish to use: ')
    for template in pvers.templateList:
        if template["version"] == versionNum:
            parts = template
            for key in parts.keys():
                if key != 'version':
                    parts[key] = input(f'Insert {key}: ')

    return parts

#delete a part by company part #
def deletePart(partsDB):
    part_num = input('Enter the company part number for the deletion: ')
    for record in partsDB:
        if record["Company Part #"] == part_num:
            partsDB.remove(record)

#Search function by company part # or manufacturer part #
def searchPart(partsDB):
    print()
    choice = input('Enter the Company Part #: ')
    for record in partsDB:
        if record.get("Company Part #") == choice:
            return record
        else: 
            print("Record not found...\n")
            searchPart(partsDB)
    
#Edit the fields of the existing part
def editPart(record):
    partDBRecordIndex = partsDB.index(record)
    partDBRecord = partsDB.pop(partDBRecordIndex)
    for k, v in partDBRecord.items():
        print(f'Current - {k}: {v}')
        partDBRecord[k] = input(f'Insert new {k}: ')
    partsDB.insert(partDBRecordIndex, partDBRecord)
    
#Changing to a version with more fields
def changeVersionAndAddFields(partDBRecord, newVersion):
    newTemplate = pvers.templateList[int(newVersion)-1]
    for k in newTemplate.keys():
        if k == 'version':
            continue
        elif partDBRecord.__contains__(k):
            newTemplate[k] = partDBRecord.get(k)
        else:
            newTemplate[k] = input(f'Input new field value {k}: ')
    return newTemplate
 
#Changing to a version with less fields 
def changeVersionAndRemoveFields(partDBRecord, newVersion):
    newTemplate = pvers.templateList[int(newVersion)-1]
    for k in partDBRecord.keys():
        if k == 'version':
            continue
        elif newTemplate.__contains__(k):
            newTemplate[k] = partDBRecord.get(k)
    return newTemplate

#Change the version of the current record
def changePartVersion(record):
    partDBRecordIndex = partsDB.index(record)
    partDBRecord = partsDB.pop(partDBRecordIndex)
    partVersion = partDBRecord.get('version')
    showVersions()
    print(f'Current version is: {partVersion}')
    newVersion = input('Enter the number of the version you wish to change to: ')
    if int(newVersion) < int(partVersion):
        partDBRecord = changeVersionAndAddFields(partDBRecord, newVersion)
    else:
        partDBRecord = changeVersionAndRemoveFields(partDBRecord, newVersion)
    partsDB.insert(partDBRecordIndex, partDBRecord)

#function for changing the template     
def showRecordOptions(record):
    while True:
        print()
        print('Record Options')
        print('1. Edit fields')
        print('2. Change version')
        print('3. Main Menu')
        choice = input('Enter your choice... ')
        if choice == '1':
            editPart(record)
        elif choice == '2':
            changePartVersion(record)
        elif choice == '3':
            print('Returning to Main Menu...')
            break
        else:
            print('Invalid input...')
            
#formatted print function
def pretty_print(records):
    print('\tPART DATABASE')
    print('\t-------------')
    for i in range(len(records)):
        print(f'Record: {i+1}')
        for k, v in records[i].items():
            print(f'\t{k}: {v}')
        print()
    
#looping menu function for basic UI
def menu():
    while True:
        print('******************************')
        print('\tPART DATABASE')
        print('******************************')
        print('Options: ')
        print('1. Create a record')
        print('2. Delete a record')
        print('3. Search for a record')
        print('4. Print Database records')
        print('5. Exit')
        choice = (input('Insert number corresponding to option: '))
        if choice == '1':
            partsDB.append(createPart())
        elif choice == '2':
            deletePart(partsDB)
        elif choice == '3':
            record = searchPart(partsDB)
            showRecordOptions(record)
        elif choice == '4':
            pretty_print(partsDB)
        elif choice == '5':
            print('Closing program...')
            break
    
menu()