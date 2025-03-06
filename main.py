#Return a list of all the avilable tables
#Empty List
#Check if [row][column] is equal to o
#If so, append the table to the list of availabe tables
def get_free_tables(tables, time):
    available = []
    for i in range(1, len(tables[0])):
        if tables[time][i] == 'o':
            available.append(tables[0][i])
    return available


#Return the table and timeslot that is available
#Takes every table and checks if it is available and large enough
def find_table_for_party(tables, size, time):
    for i in range(1, len(tables[0])):
        table = tables[0][i]
        capacity = int(table.split('(')[1].split(')')[0])
        if capacity >= size and tables[time][i] == 'o':
            return table

#Return every table in the timeslot
#Takes every table and checks if it is available and large enough
def find_all_tables_for_party(tables, size, time):
    all_tables = []
    for i in range(1, len(tables[0])):
        table = tables[0][i]
        capacity = int(table.split('(')[1].split(')')[0])
        if capacity >= size and tables[time][i] == 'o':
            all_tables.append(table)
    return all_tables

#Returns the two adjacent tables that are greater or equal to the party's size
#Checks every table and their adjacent tables and returns the first instance of an approved table combo
def combined_tables(tables, size, time):
    combo = []
    for i in range (1, len(tables[0]) - 1):
        table1 = tables[0][i]
        capacity1 = int(table1.split('(')[1].split(')')[0])
        table2 = tables[0][i + 1]
        capacity2 = int(table2.split('(')[1].split(')')[0])
        if tables[time][i] == 'o' and capacity1 >= size:
            combo.append([table1])
        if (tables[time][i] == 'o' and tables[time][i + 1] == 'o' and capacity1 + capacity2 >= size):
            combo.append([table1, table2])
    return combo
    



table_one = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]

#Testing things

print(f"Tables {get_free_tables(table_one, 1)} are open at time 1")
print("-----------------------------")
print(f"Table for one at time 1 at table {find_table_for_party(table_one, 1, 1)}")
print("-----------------------------")
print(f"These are all of the available tables for a party of one:\n{find_all_tables_for_party(table_one, 1, 1)}")
print("-----------------------------")
print(f"Tables {combined_tables(table_one, 5, 1)} can be combined to sit a party of 5 ")