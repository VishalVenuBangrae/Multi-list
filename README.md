## Multi-List Database System
Project Overview
This project implements a many-to-many relationship between "supplier" and "part" objects using a multi-list data structure. The system manages relationships where a supplier can provide multiple parts, and a part can be supplied by multiple suppliers. The implementation involves reading data from files, constructing a multi-list structure, and persisting updates back to the files.

### Files Structure
Database.py: The main program file that handles the user interface and integration of the multi-list system. It reads input data, processes user commands, and writes updates back to the files.
SupplierNode.py: Defines the SupplierNode class representing a node in the multi-list for suppliers.
Suppliers.py: Manages the list of suppliers and associated operations such as adding or removing suppliers.
PartNode.py: Defines the PartNode class representing a node in the multi-list for parts.
Parts.py: Manages the list of parts and associated operations such as adding or removing parts.
SupplyNode.py: Defines the SupplyNode class representing a node in the multi-list for supply relationships.
Supply.py: Manages the list of supplies and operations on the supply relationships.
How to Run the Program
Ensure that Python 3.x is installed on your system.
Prepare three data files in a directory:
suppliers.txt for suppliers data
parts.txt for parts data
supplies.txt for supply relationships data
Clone or download this repository to your local machine.
Navigate to the project directory in the command line or terminal.
Run the program using the command:

python Database.py <data_folder>
Replace <data_folder> with the path to the folder containing your data files.
Commands Supported
add supplier <supplier_id> <name>: Adds a new supplier.
add part <part_id> <name>: Adds a new part.
add supply <supplier_id> <part_id>: Adds a new supply relationship.
delete supplier <supplier_id>: Removes a supplier and all associated supplies.
delete part <part_id>: Removes a part and all associated supplies.
delete supply <supplier_id> <part_id>: Removes a specific supply relationship.
list suppliers: Lists all suppliers.
list parts: Lists all parts.
list supplies: Lists all supply relationships.
exit: Exits the program and saves the current state to the files.
