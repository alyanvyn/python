#fungsi
def get_choices():
    #variabel
    player_choice = input("enter a (rock, paper, scissors): ") #input user
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice} #dict{"..": ".."}
    return choices #pengembalian

choices = get_choices() #panggil fungsi
print(choices)