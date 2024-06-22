import random

# initializing the matrix
map_treasure = [[" " for _ in range(3)] for _ in range(3)]

row_pos_treasure = random.randint(0, 2)
column_pos_treasure = random.randint(0, 2)

print("\n----- Your treasure is hidden in a map of 3 rows and 3 columns -----\n")

while True:
    try:
        row_user = int(input("Enter the position of the row you think is the treasure: 0 -> 2: "))
        column_user = int(input("Enter the position of the row you think is the treasure: 0 -> 2: "))
        if 2 >= (row_user and column_user) >= 0:
            break
    except ValueError:
        print("Invalid input. Try again!")

# putting the treasure in a pseudo random position
map_treasure[row_pos_treasure][column_pos_treasure] = "Treasure"


# function to print the matrix in a more readable way
def print_matrix(matrix):
    print("       0         1         2    ")
    print("  +---------+---------+---------+")

    for i, row in enumerate(matrix):
        row_str = f"{i} | "
        for cell in row:
            if cell == "Treasure":
                row_str += f"{cell:^8}"
            else:
                row_str += f"{cell:^7}"
            row_str += " | "
        print(row_str)
        print("  +---------+---------+---------+")


print("\nThe map is")
print_matrix(map_treasure)

if row_user == row_pos_treasure and column_user == column_pos_treasure:
    print("Congratulations! You found the treasure!")
else:
    print(f"Sorry, the treasure was at ({row_pos_treasure}, {column_pos_treasure}).")
