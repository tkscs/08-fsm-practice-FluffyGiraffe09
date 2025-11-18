# write code to implement a turnstile

current_balance=5

current_state="locked"


print(f"you currently have {current_balance} coins")

while True:
    if current_state == "locked" and current_balance>0:
        response=input ("insert a coin to unlock. Please type (c) to insert a coin before you push (p)")
        if response=="p":
            current_state="locked"
            print("(currently locked)")
            print("you did not insert a coin, so you may not go through")
            print(f"you currently have {current_balance} coin(s)")
        elif response=="c" and current_balance>0:
            current_state="unlocked"
            current_balance=current_balance-1
            print("(currently unlocked)")
            print(f"you currently have {current_balance} coin(s)")
            push_response=input("you may now (p) push and go through")
            if push_response=="p":
                current_state="locked"
                print("you have gone through.")
                print(f"you currently have {current_balance} coin(s)")
                print("(currently locked)")
            if push_response=="c":
                current_state="unlocked"
                print("your coin has been rejected")
                print(f"you currently have {current_balance} coin(s)")
                print("(currently unlocked)")
            
        else:
            print("please type one of the two options")
    elif current_state == "locked" and current_balance==0:
        print("you have run out of money")
        break