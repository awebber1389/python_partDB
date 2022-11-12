
#Dictionaries containing part versions with default values
#All versions will have Company Part Number attribute

#Version with all possible attributes
version1 = {
    "version": "1",
    "Company Part #": "NONE",
    "Manufacturer Part #": "NONE",
    "Description": "NONE",
    "Cost": "0.00",
    "Amount on Hand": "0",
    "Amount Needed": "0",
    "Lead Time": "0"
}

#Version without description field
version2 = {
    "version": "2",
    "Company Part #": "NONE",
    "Manufacturer Part #": "NONE",
    "Cost": "0.00",
    "Amount on Hand": "0",
    "Amount Needed": "0",
    "Lead Time": "0"
}

#Version with company part number, manufacturer part number,
#and cost
version3 = {
    "version": "3",
    "Company Part #": "NONE",
    "Manufacturer Part #": "NONE",
    "Cost": "0.00"
}

templateList = [version1, version2, version3]