value = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

keyboard= []

for key in value:
    keyboard.append(key)



def Displayboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

    turn = 'X'
    count = 0
    print("\n")
    print("----------------")
    print("TIC TAC TOE GAME")
    print("----------------")
    print("\n")

    for i in range(10):
        Displayboard(value)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if value[move] == ' ':
            value[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

         
        if count >= 5:
            if value['7'] == value['8'] == value['9'] != ' ': 
                Displayboard(value)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif value['4'] == value['5'] == value['6'] != ' ': 
                Displayboard(value)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif value['1'] == value['2'] == value['3'] != ' ': 
                Displayboard(value)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif value['1'] == value['4'] == value['7'] != ' ':
                Displayboard(value)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif value['2'] == value['5'] == value['8'] != ' ': 
                Displayboard(value)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif value['3'] == value['6'] == value['9'] != ' ': 
                Displayboard(value)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif value['7'] == value['5'] == value['3'] != ' ': 
                Displayboard(value)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif value['1'] == value['5'] == value['9'] != ' ':
                Displayboard(value)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

       #invalid input
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        #changing player
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again? \n (y->Yes/n->No)")
    if restart == "y" or restart == "Y":  
        for key in keyboard:
            value[key] = " "

        game()

if __name__ == "__main__":
    game()