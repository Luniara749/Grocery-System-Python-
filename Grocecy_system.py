def InsertNewItem():
    Code=input('Enter code: ')
    Description=input('Enter Description: ')
    Category=input('Enter Category: ')
    Unit=input('Enter Unit: ')
    Price=input('Enter Price: ')
    Quantity=input('Enter Quantity: ')
    Minimum=input('Enter Minimum Price: ')

    ItemList=[Code,Description,Category,Unit,Price,Quantity,Minimum]
    Item = ' '.join(ItemList)
    with open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt','a') as inventorydata:
        inventorydata.write(Item)
        inventorydata.write('\n')
        inventorydata.close()


def UpdateItem():
    inventorydata = open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt')
    Inventory = inventorydata.readlines()
    counter = 0
    newline = None
    print('Your choice available are:- ')
    for item in Inventory:
        item_code=item.split()[0]
        print(item_code)
    UserItem = str(input('Enter a item code that you wish to change: '))
    for item in Inventory:
        item_code=item.split()[0]
        item_description=item.split()[1]
        item_category=item.split()[2]
        item_unit=item.split()[3]
        item_price=item.split()[4]
        item_quantity=item.split()[5]
        item_minimum=item.split()[6]
        if item_code == UserItem:
            print(Inventory[counter])
            break
        
        else:
            counter=counter +1
    Change_category = input(' 1.Item code\n 2.Item description\n 3.Item category\n 4.Item unit\n 5.Item price\n 6.Item quantity\n 7.Item minimum\nEnter a category you wish to change(number): ')
    if int(Change_category) == 1:
        New_itemcode = input('Enter New item code : ')
        newline=(New_itemcode,item_description,item_category,item_unit,item_price,item_quantity,item_minimum, '\n')
    if int(Change_category) == 2:
        New_itemcode = input('Enter New item description : ')
        newline=(item_code,New_itemcode,item_category,item_unit,item_price,item_quantity,item_minimum, '\n')
    if int(Change_category) == 3:
        New_itemcode = input('Enter New item category : ')
        newline=(item_code,item_description,New_itemcode,item_unit,item_price,item_quantity,item_minimum, '\n')
    if int(Change_category) == 4:
        New_itemcode = input('Enter New item unit : ')
        newline=(item_code,item_description,item_category,New_itemcode,item_price,item_quantity,item_minimum, '\n')
    if int(Change_category) == 5:
        New_itemcode = input('Enter New item price(.00): ')
        newline=(item_code,item_description,item_category,item_unit,New_itemcode,item_quantity,item_minimum, '\n')
    if int(Change_category) == 6:
        New_itemcode = input('Enter New item quantity : ')
        newline=(item_code,item_description,item_category,item_unit,item_price,New_itemcode,item_minimum, '\n')
    if int(Change_category) == 7:
        New_itemcode = input('Enter New item minimum : ')
        newline=(item_code,item_description,item_category,item_unit,item_price,item_quantity,New_itemcode, '\n')
    if newline is None:
        print('That is an unvalid category')
    else:
        Inventory[counter]= ' '.join(newline)
        with open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt','w') as file:
            for line in Inventory:
                file.write(line)
        


def RemoveItem():
    inventorydata = open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt')
    Inventory = inventorydata.readlines()
    counter = 0
    RemoveItem = str(input('Enter a item code that you wish to remove: '))
    for item in Inventory:
        item_code=item.split()[0]
        item_description=item.split()[1]
        item_category=item.split()[2]
        item_unit=item.split()[3]
        item_price=item.split()[4]
        item_quantity=item.split()[5]
        item_minimum=item.split()[6]
        if item_code == RemoveItem:
            print(Inventory[counter])
            break
        else:
            counter=counter +1
    Inventory.pop(counter)
    print('This item is removed')
    with open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt','w') as file:
            for line in Inventory:
                file.write(line)


def StockTaking():
    inventorydata = open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt')
    Inventory = inventorydata.readlines()
    counter = 0
    StockTaking = str(input('Enter a item code that you wish to take: '))
    for item in Inventory:
        item_code=item.split()[0]
        item_description=item.split()[1]
        item_category=item.split()[2]
        item_unit=item.split()[3]
        item_price=item.split()[4]
        item_quantity=item.split()[5]
        item_minimum=item.split()[6]
        if item_code == StockTaking:
            print(Inventory[counter])
            print('There are',item_quantity,'stock(s) availble')
            break
        else:
            counter=counter +1
    UserChoice = int(input('Do you wish to take stock?\n1.Yes\n2.No\nEnter your choice(number): '))
    if UserChoice == 1:
        QuantityChanges = input('How many item do you wish to take?(number): ')
        NewQuantity = int(item_quantity) - int(QuantityChanges)
        if NewQuantity < 0:
            print('The item of quantity cannot be less than 0')
        else:
            newline=(item_code,item_description,item_category,item_unit,item_price,str(NewQuantity),item_minimum, '\n')
            Inventory[counter]= ' '.join(newline)
            with open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt','w') as file:
                for line in Inventory:
                    file.write(line)        
    if UserChoice == 2:
        print('No stock is taken')


def ReplenishList():
    inventorydata = open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt')
    Inventory = inventorydata.readlines()
    counter = 0
    check = 0
    for item in Inventory:
        item_quantity=item.split()[5]
        item_minimum=item.split()[6]
        if int(item_minimum) > int(item_quantity) :
            print(Inventory[counter])
            check= check +1
        counter=counter+1
        
            
    if check == 0:
        print('All stock are replenished')
    else:
        print('The stock above need to be replenish')
    
def StockReplenishment():
    inventorydata = open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt')
    Inventory = inventorydata.readlines()
    counter = 0
    StockRep = str(input('Enter a item code that you wish to replenish: '))
    for item in Inventory:
        item_code=item.split()[0]
        item_description=item.split()[1]
        item_category=item.split()[2]
        item_unit=item.split()[3]
        item_price=item.split()[4]
        item_quantity=item.split()[5]
        item_minimum=item.split()[6]
        if item_code == StockRep:
            print('Your are replenishing this stock，',Inventory[counter])
            break
        else:
            counter=counter +1
    print('There are',item_quantity,'stock(s) availble')
    StockAdded = input('How many stock do you want to replenish?(number): ')
    StockAddeds = int(item_quantity)+int(StockAdded)
    newline=(item_code,item_description,item_category,item_unit,item_price,str(StockAddeds),item_minimum, '\n')
    Inventory[counter]= ' '.join(newline)
    with open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt','w') as file:
        for line in Inventory:
            file.write(line)

def SearchItem():
    inventorydata = open (r'C:\Users\user\Desktop\Assignment Python\inventory.txt')
    Inventory = inventorydata.readlines()
    counter = 0
    check= 0
    Choice = int(input('How would you like to search a item?\n1.Search item by description\n2.Search item by code range\n3.Search items in a specific category\n4.Search items in a specific price range\nYour choice is(number): '))
    if Choice == 1:
        print('Your choice available are:- ')
        for item in Inventory:
            item_description=item.split()[1]
            print(item_description)
            
        SearchDescription = input('Enter the description you wish to search: ')
        for item in Inventory:
            item_description=item.split()[1]
            if item_description == SearchDescription:
                print(Inventory[counter])
                check=check+1
            counter=counter+1
        if check == 0:
            print('No item found')
        else:
            print(check,'item(s) is found')
    if Choice == 2:
        CodeRange1 = int(input('Enter the first code range(number):'))
        CodeRange2 = int(input('Enter the second code range(number):'))
        for item in Inventory:
            item_code=item.split()[0]
            if int(item_code) in range(CodeRange1,CodeRange2):
                print(Inventory[counter])
                check = check+1
            counter=counter+1
        if check == 0:
            print('No item found')
        else:
            print(check,'item(s) is found')
    if Choice == 3:
        print('Your choice available are:- ')
        for item in Inventory:
            item_category=item.split()[2]
            print(item_category)

        SearchCategory = input('Enter the category you wish to search:')
        for item in Inventory:
            item_category=item.split()[2]
            if item_category == SearchCategory:
                print(Inventory[counter])
                check=check+1
            counter=counter+1
        if check == 0:
            print('No item found')
        else:
            print(check,'item(s) is found')
    if Choice == 4:
        PriceRange1 = int(input('Enter the first price range(number):'))
        PriceRange2 = int(input('Enter the second price range(number):'))
        for item in Inventory:
            item_price=item.split()[4]
            if float(item_price) in range(PriceRange1,PriceRange2):
                print(Inventory[counter])
                check = check+1
            counter=counter+1
        if check == 0:
            print('No item found')
        else:
            print(check,'item(s) is found')
        
    else:
        print('You enter a valid number')

UserChoice = int(input('-------------GROCERY STORE INVENTORY SYSTEM---------\nSelect a number below to run the function\n1.Insert a New item\n2.Update a Item\n3.Remove a item\n4.Stock Taking\n5.View Replenish List\n6.Stock Replenishment\n7.Search Item\nYour Choice is(number):'))
if UserChoice == 1:
    InsertNewItem()
if UserChoice == 2:
    UpdateItem()
if UserChoice == 3:
    RemoveItem()
if UserChoice == 4:
    StockTaking()
if UserChoice == 5:
    ReplenishList()
if UserChoice == 6:
    StockReplenishment()
if UserChoice == 7:
    SearchItem()
    
    

