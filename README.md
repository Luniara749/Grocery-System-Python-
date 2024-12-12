# Grocery-System-Python-
Features

1. Insert New Item

Allows the user to add a new item to the inventory by providing:

Code

Description

Category

Unit

Price

Quantity

Minimum Stock Level

2. Update Item

Enables the user to modify specific details of an existing item in the inventory, such as:

Code

Description

Category

Unit

Price

Quantity

Minimum Stock Level

3. Remove Item

Removes an item from the inventory based on the item's code.

4. Stock Taking

Displays the current stock level of a specific item and allows the user to adjust the quantity.

5. View Replenish List

Lists all items that have quantities below the minimum stock level.

6. Stock Replenishment

Allows the user to increase the stock level of a specific item.

7. Search Item

Provides multiple options to search for items:

By description

By code range

By category

By price range

How to Use

1.Run the script in a Python environment.

2.Follow the menu prompts to choose an operation.

3.Provide the necessary inputs as prompted by the system.

File Storage

The inventory is stored in a text file located at:
C:\Users\user\Desktop\Assignment Python\inventory.txt

Each line in the file represents an item, with details separated by spaces.

Requirements

Python 3.x

A writable file located at C:\Users\user\Desktop\Assignment Python\inventory.txt

Notes

Ensure the text file exists at the specified path before running the program.

The program performs basic input validation but assumes correct file structure.

Limitations

The inventory file format uses space-separated values, which may cause issues if descriptions or other fields contain spaces.

No GUI or database integration; all data is stored in a plain text file.

Future Improvements

Use a CSV or database for better data storage and management.

Add more robust input validation.

Implement a graphical user interface for easier usability.
