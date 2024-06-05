def generate_team_names(base_name):
    team_name = base_name + " United"

    team_name2 = "FC " + base_name

    # in Python, you can return multiples values
    # In this case, the return is a tuple
    return team_name, team_name2


user_input = str(input("Enter a base name for your football team: "))
size_of_string = len(user_input)

team1, team2 = generate_team_names(user_input)
print(f"Length of the input: {size_of_string}")
print(f"Suggestions:\nTeam1: {team1}\nTeam2: {team2}")
