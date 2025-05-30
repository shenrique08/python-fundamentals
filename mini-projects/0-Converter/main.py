

def converter(miles):
    return miles * 1.60934



if __name__ == '__main__':
    user_input = int(input("Enter a distance in miles: "))
    print(f"{user_input} miles is {converter(user_input)} kilometers! ")
