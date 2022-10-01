
#A class defining a Part
class Part():
    def __init__(self):
        self.partsDB = []
        self.totalParts = 0

    #function to create a part item from user input and return it
    def createPart(self):
        partAttr = ['Company Part #', 'Manufacturer\'s Part #', 'Description', 'Cost', 'Amt On Hand', 'Amt Needed', 'Lead Time']
        parts = []
        for attrib in partAttr:
            item = input(f'{attrib}: ')
            parts.insert(partAttr.index(attrib), item)
        print()

        return parts

    def addPartToDB(self, part):
        self.partsDB.append(part.copy())
        print(self.partsDB)

p = Part()
item = p.createPart()
p.addPartToDB(item)