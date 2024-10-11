import random
def janken():
    hands=["グー","チョキ","パー"]
    a=random.randint(0,2);b=random.randint(0,2)
    if a==b:
        print("引き分け")
    elif (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0):
        print(f"Aの手{hands[a]} bの手{hands[b]}->Aの勝ち")
    else:
        print(f"Aの手{hands[a]} bの手{hands[b]}->Bの勝ち")
    
janken()
janken()