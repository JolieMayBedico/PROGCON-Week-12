import random


def user_turn(boxes):
    while True:
        print(f"\n{boxes[0]} | {boxes[1]} | {boxes[2]}")
        choice = int(input("Choose a box (1-3): "))

        if choice in (1, 2, 3) and boxes[choice - 1] == "":
            boxes[choice - 1] = "O"
            return
        else:
            print("That box is already filled or invalid. Try again.")


def computer_turn(boxes):
    empty_boxes = [i for i in range(3) if boxes[i] == ""]
    choice = random.choice(empty_boxes)
    boxes[choice] = "X"
    print(f"Computer chose box {choice + 1}.")


def check_winner(boxes):
    if boxes[0] == boxes[1] == boxes[2] and boxes[0] != "":
        if boxes[0] == "O":
            return "User"
        else:
            return "Computer"
    return ""


def main():
    boxes = ["", "", ""]
    winner = ""
    turn = random.randint(1, 2)

    print("Tic-Tac-Toe Game")
    print("User = O")
    print("Computer = X")

    while winner == "":
        if all(box != "" for box in boxes):
            winner = "Draw"
            break

        if turn == 1:
            user_turn(boxes)
            turn = 2
        else:
            computer_turn(boxes)
            turn = 1

        winner = check_winner(boxes)

    print(f"\n{boxes[0]} | {boxes[1]} | {boxes[2]}")

    if winner == "Draw":
        print("The game is a draw!")
    else:
        print(winner + " wins!")


if __name__ == "__main__":
    main()
