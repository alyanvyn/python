import random #import library random

#fungsi
def get_choices():
    #variabel
    player_choice = input("Enter a (rock, paper, scissors): ") #input user
    options = ["rock", "paper", "scissors"] #list pilihan
    computer_choice = random.choice(options) #pilihan komputer secara acak
    choices = {"player": player_choice, "computer": computer_choice} #dictionary untuk menyimpan pilihan
    return choices #pengembalian


def check_winner(player, computer):
    print(f"You chose {player}, Computer chose {computer}") #tampilkan pilihan
    if player == computer:
        return "It's a tie!" #jika seri
    elif player == "rock":
        if computer == "scissors":
            return "you win!"
        else:
            return "You lose!" #jika kalah
    elif player == "paper":
        if computer == "rock":
            return "you win!"
        else:
            return "You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "you win!"
        else:
            return "You lose!"

choices = get_choices() #panggil fungsi
result = check_winner(choices["player"], choices["computer"]) #panggil fungsi
print(result) #Print hasil

while True: #looping
    play_again = input("\nDo you want to play again? (yes/no): ").lower() #input user
    if play_again != "yes": #jika tidak
        print("Thanks for playing!") #tampilkan pesan
        break #keluar dari loop

    choices = get_choices() #panggil fungsi
    result = check_winner(choices["player"], choices["computer"]) #panggil fungsi
    print(result) #Print hasil