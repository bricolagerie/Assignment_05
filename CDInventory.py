#--------------------------------------------------------------------------------#
# Title: CDInventory.py
# Desc: Assignment 05 - Updated CD Inventory Script
# Change Log: (Who, When, What)
# BAnson, 2020-Aug-08, Created File
# BAnson, 2020-Aug-08, Update internal data to dictionary type
# BAnson, 2020-Aug-08, Added load from file, add data, display inventory, save
# BAnson, 2020-Aug-11, Added code for "delete" menu option
# BAnson, 2020-Aug-12, Added:
#                            "continue" options to add data sequence
#                            "are you sure?" to exit sequence
#                            error message to delete sequence
#                            existing ID check in "add CD" sequence
#--------------------------------------------------------------------------------#


# Declare variables

strChoice = '' # User input
dictTbl = []  # list of dictionaries to hold data
dictRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

    
# Get user Input
print('The Magic CD Inventory\n')

while True:
    # Display menu allowing the user to choose:
    print('\n[l] Load inventory from file\n[a] Add CD\n[i] Display current inventory')
    print('[d] Delete CD from inventory\n[s] Save inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':  # exit the program
        choice = input('Are you sure you want to exit? Choose \'y\' or \'n\': ') # prevent exiting accidentally
        if choice.lower() == 'y':
            break
        else:
            continue
    
    
    if strChoice == 'l':  # load existing data from file
        loadChoice = input('Loading data from file will replace the table data currently in memory. \nDo you want to proceed? Choose \'y\' or \'n\': ')
        if loadChoice.lower() == 'n':
            continue
        else:
            dictTbl.clear() # clears existing table data in memory before loading data from file
            objFile = open(strFileName, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                dictRow = {'id': lstRow[0], 'artist': lstRow[1], 'title': lstRow[2]}
                dictTbl.append(dictRow)
            objFile.close()
            print('\nData loaded from file.')
    
    
    elif strChoice == 'a':  # add data to the table
        print('Enter new data, or type \'c\' to clear and return to menu: ')
        strID = input('Enter an ID: ')
        if strID == 'c':  # option to clear data at each stage of entry to prevent writing to memory
            continue
        # Check if entered ID already in inventory
        idInv = []
        for row in dictTbl:
            if strID in row.values():
                idInv.append('T')
        if 'T' in idInv:          
            print('Error: that ID already exists in the inventory.')
            continue

        strArtist = input('Enter the Artist\'s Name: ')
        if strArtist == 'c':
            continue
        strTitle = input('Enter the CD\'s Title: ')
        if strTitle == 'c':
            continue
        dictRow = {'id': strID, 'artist': strArtist, 'title': strTitle}
        dictTbl.append(dictRow)
        
        
    elif strChoice == 'i':  # Display current inventory in memory     
        print('{:<4} | {:<30} | {:<40} |'.format('ID', 'ARTIST', 'ALBUM'))
        for row in dictTbl:
            lstRow = []  # create a list to populate with dictionary values
            for item in row.values():
                lstRow.append(item)
            print('{:<4} | {:<30} | {:<40} |'.format(lstRow[0], lstRow[1], lstRow[2]))
            
            
    elif strChoice == 'd':
        delID = input('enter the ID of the entry you want to delete: ')
        
        # Sequence to check each row for the entered ID
        # There is probably a better way to set this up
        chkLst = []  
        for row in dictTbl:
            if delID in row.values():
                idChck = 'T'
            else:
                idChck = 'F'
            chkLst.append(idChck)
        if 'T' not in chkLst:   # Checks if entered ID doesn't exist
            print('\nSorry, that ID is not in the inventory.')  
            
        else: 
            for row in dictTbl:  
                if delID in row.values():
                    dictTbl.remove(row)
            print('\nItem deleted.')
             
    
    elif strChoice == 's':     
        objFile = open(strFileName, 'w')  # save to file (this overwrites existing file data)
        for row in dictTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
        
    else:
        print('Please choose either l, a, i, d, s or x!')

