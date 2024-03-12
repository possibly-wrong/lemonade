# LEMONADE for Apple II, directly translated from Applesoft BASIC to Python
# with canonical mode text interface (no lo-res graphics or sound)

#  <<< LEMONADE STAND >>>
#
# FROM AN ORIGINAL PROGRAM
#  BY BOB JAMISON, OF THE
#  MINNESOTA  EDUCATIONAL
#   COMPUTING CONSORTIUM
#         *  *  *
#  MODIFIED FOR THE APPLE
#      FEBRUARY, 1979
#    BY CHARLIE KELLNER

import random
import math

D = 0 # zero-initialize variables at first use
R2 = 0
prompt = " PRESS ENTER TO CONTINUE, CTRL-C TO END..."

def weather_display(SC):
    print()
    print(" " * 7 + " LEMONSVILLE WEATHER REPORT ")
    print()
    if SC == 2:
        print(" " * 17 + " SUNNY ")
    elif SC == 7:
        print(" " * 14 + " HOT AND DRY ")
    elif SC == 10:
        print(" " * 16 + " CLOUDY ")
    elif SC == 5:
        print(" " * 13 + " THUNDERSTORMS! ")

# INTRODUCTION
print()
print("#                                 #     ")
print("#                                 #     ")
print("#    #### ##### #### #### #### #### ####")
print("#    #  # # # # #  # #  #    # #  # #  #")
print("#    #### # # # #  # #  # #### #  # ####")
print("#    #    # # # #  # #  # #  # #  # #   ")
print("#### #### #   # #### #  # #### #### ####")
print()
print("        #####  #               #        ")
print("        #      #               #        ")
print("        #     ### #### #### ####        ")
print("        #####  #     # #  # #  #        ")
print("            #  #  #### #  # #  #        ")
print("            #  #  #  # #  # #  #        ")
print("        #####  #  #### #  # ####        ")
print()
print("  COPYRIGHT 1979    APPLE COMPUTER INC.")

A, L, H, B, S, P, G = [[0] * 30 for I in range(7)]
P9 = 10
S3 = .15
S2 = 30
A2 = 2.00
C9 = .5
C2 = 1

# START OF GAME
# TITLE PAGE
print()
print("HI!  WELCOME TO LEMONSVILLE, CALIFORNIA!")
print()
print("IN THIS SMALL TOWN, YOU ARE IN CHARGE OF")
print("RUNNING YOUR OWN LEMONADE STAND. YOU CAN")
print("COMPETE WITH AS MANY OTHER PEOPLE AS YOU")
print("WISH, BUT HOW MUCH PROFIT YOU MAKE IS UP")
print("TO YOU (THE OTHER STANDS' SALES WILL NOT")
print("AFFECT YOUR BUSINESS IN ANY WAY). IF YOU")
print("MAKE THE MOST MONEY, YOU'RE THE WINNER!!")
print()
print("ARE YOU STARTING A NEW GAME? (YES OR NO)")
while True:
    A_str = input("TYPE YOUR ANSWER AND HIT RETURN ==> ").upper()
    A_str = A_str[0]
    if A_str == 'Y' or A_str == 'N':
        break
while True:
    N = int(input("HOW MANY PEOPLE WILL BE PLAYING ==> "))
    if 1 <= N <= 30:
        break
for I in range(N):
    B[I] = 0
    A[I] = A2
if A_str != 'Y':
    
    # CONTINUE OLD GAME
    print()
    I = 0
    print("HI AGAIN!  WELCOME BACK TO LEMONSVILLE! ")
    print()
    print("LET'S CONTINUE YOUR LAST GAME FROM WHERE")
    print("YOU LEFT IT LAST TIME.  DO YOU REMEMBER ")
    print("WHAT DAY NUMBER IT WAS? ", end='')
    while True:
        A_str = input().upper()
        A_int = 0
        try:
            A_int = int(A_str)
        except ValueError:
            pass
        print()
        if A_int != 0:
            if 1 <= A_int <= 99:
                D = A_int
            break
        A_str = A_str[0]
        if A_str == 'Y':
            print("GOOD!  WHAT DAY WAS IT? ", end='')
            I = I + 1
        elif A_str != 'N' and I == 0:
            print("YES OR NO? ", end='')
            I = I + 1
    print(f"OKAY - WE'LL START WITH DAY NO. {D+1}")
    print()
    for I in range(N):
        print()
        print()
        print(f"PLAYER NO. {I+1}, HOW MUCH MONEY (ASSETS)")
        print()
        A_float = float(input("DID YOU HAVE? "))
        print()
        if A_float < 2:
            print("O.K. - WE'LL START YOU OUT WITH $2.00")
            A_float = 2
        elif A_float > 40:
            print("JUST TO BE FAIR, LET'S MAKE THAT $10.00")
            A_float = 10
        A[I] = int(A_float * 100 + .5) / 100
    print()
    print()
    A_str = input("...READY TO BEGIN? ").upper()
    if A_str[0] == 'N':
        A_str = 'Y'
if A_str == 'Y':
    
    # NEW BUSINESS
    print()
    print("TO MANAGE YOUR LEMONADE STAND, YOU WILL ")
    print("NEED TO MAKE THESE DECISIONS EVERY DAY: ")
    print()
    print("1. HOW MANY GLASSES OF LEMONADE TO MAKE")
    print("   (ONLY ONE BATCH IS MADE EACH MORNING)")
    print("2. HOW MANY ADVERTISING SIGNS TO MAKE")
    print("   (THE SIGNS COST FIFTEEN CENTS EACH)  ")
    print("3. WHAT PRICE TO CHARGE FOR EACH GLASS  ")
    print()
    print("YOU WILL BEGIN WITH $2.00 CASH (ASSETS).")
    print("BECAUSE YOUR MOTHER GAVE YOU SOME SUGAR,")
    print("YOUR COST TO MAKE LEMONADE IS TWO CENTS ")
    print("A GLASS (THIS MAY CHANGE IN THE FUTURE).")
    print()
    input(prompt)
    print()
    print("YOUR EXPENSES ARE THE SUM OF THE COST OF")
    print("THE LEMONADE AND THE COST OF THE SIGNS. ")
    print()
    print("YOUR PROFITS ARE THE DIFFERENCE BETWEEN ")
    print("THE INCOME FROM SALES AND YOUR EXPENSES.")
    print()
    print("THE NUMBER OF GLASSES YOU SELL EACH DAY ")
    print("DEPENDS ON THE PRICE YOU CHARGE, AND ON ")
    print("THE NUMBER OF ADVERTISING SIGNS YOU USE.")
    print()
    print("KEEP TRACK OF YOUR ASSETS, BECAUSE YOU  ")
    print("CAN'T SPEND MORE MONEY THAN YOU HAVE!   ")
    print()
    input(prompt)
    print()
while True:
    
    # WEATHER REPORT
    SC = random.random()
    if SC < .6:
        SC = 2
    elif SC < .8:
        SC = 10
    else:
        SC = 7
    if D < 3:
        SC = 2
    weather_display(SC)
    print()

    # START OF NEW DAY
    D = D + 1
    print(f"ON DAY {D}, THE COST OF LEMONADE IS ", end='')
    C = 2
    if D > 2:
        C = 4
    if D > 6:
        C = 5
    print(f"$.0{C}")
    print()
    C1 = C * .01
    R1 = 1

    # CURRENT EVENTS
    if D == 3:
        print("(YOUR MOTHER QUIT GIVING YOU FREE SUGAR)")
    elif D == 7:
        print("(THE PRICE OF LEMONADE MIX JUST WENT UP)")
        
    # AFTER 2 DAYS THINGS CAN HAPPEN
    if D > 2:
        
        # RANDOM EVENTS
        if SC == 10:
            J = 30 + int(random.random() * 5) * 10
            print(f"THERE IS A {J}% CHANCE OF LIGHT RAIN,")
            print("AND THE WEATHER IS COOLER TODAY.")
            R1 = 1 - J / 100
            X1 = 1
        elif SC == 7:
            X4 = 1
            print("A HEAT WAVE IS PREDICTED FOR TODAY!")
            R1 = 2
        elif random.random() < .25:
            print("THE STREET DEPARTMENT IS WORKING TODAY.")
            print("THERE WILL BE NO TRAFFIC ON YOUR STREET.")
            rnd_bug = True # RND(-1) should be RND(1); change bug=False to fix
            if rnd_bug or random.random() < .5:
                R1 = .1
            else:
                R2 = 2
            X2 = 1

    # INPUT VALUES
    redo = True
    while redo:
        redo = False
        for I in range(N):
            print()
            A[I] = A[I] + .000000001
            G[I] = 1
            H[I] = 0
            print(f"LEMONADE STAND {I+1}         ASSETS ${A[I]:.2f}")
            print()
            if B[I] != 0:
                print("YOU ARE BANKRUPT, NO DECISIONS")
                print("FOR YOU TO MAKE.")
                # if N == 1 and A[0] < C: # unreachable (also should be C / 100)
                #     quit()
            else:
                while True:
                    print("HOW MANY GLASSES OF LEMONADE DO YOU")
                    L[I] = int(input("WISH TO MAKE ?"))
                    if L[I] < 0 or L[I] > 1000:
                        print("COME ON, LET'S BE REASONABLE NOW!!!")
                        print("TRY AGAIN")
                    elif L[I] * C1 > A[I]:
                        print(f"THINK AGAIN!!!  YOU HAVE ONLY ${A[I]:.2f}")
                        print(f"IN CASH AND TO MAKE {L[I]} GLASSES OF")
                        print(f"LEMONADE YOU NEED ${L[I]*C1:.2f} IN CASH.")
                    else:
                        break
                while True:
                    print()
                    print(f"HOW MANY ADVERTISING SIGNS ({S3*100:.0f} CENTS")
                    S[I] = int(input("EACH) DO YOU WANT TO MAKE ?"))
                    if S[I] < 0 or S[I] > 50:
                        print("COME ON, BE REASONABLE!!! TRY AGAIN.")
                    elif S[I] * S3 > A[I] - L[I] * C1:
                        print()
                        print(f"THINK AGAIN, YOU HAVE ONLY ${A[I]-L[I]*C1:.2f}")
                        print("IN CASH LEFT AFTER MAKING YOUR LEMONADE.")
                    else:
                        break
                while True:
                    print()
                    print("WHAT PRICE (IN CENTS) DO YOU WISH TO")
                    P[I] = int(input("CHARGE FOR LEMONADE ?"))
                    if P[I] < 0 or P[I] > 100:
                        print("COME ON, BE REASONABLE!!! TRY AGAIN.")
                    else:
                        break
            print()
            A_str = input("WOULD YOU LIKE TO CHANGE ANYTHING?").upper()
            if A_str[0] == 'Y':
                redo = True
                break
    print()
    if SC == 10 and random.random() < .25:

        # THUNDERSTORM!
        X3 = 1
        R3 = 0
        SC = 5
        weather_display()
        print()
        print("WEATHER REPORT:  A SEVERE THUNDERSTORM")
        print("HIT LEMONSVILLE EARLIER TODAY, JUST AS")
        print("THE LEMONADE STANDS WERE BEING SET UP.")
        print("UNFORTUNATELY, EVERYTHING WAS RUINED!!")
        for J in range(N):
            G[J] = 0
    else:
        print("$$ LEMONSVILLE DAILY FINANCIAL REPORT $$")
        print()
        
        # CALCULATE PROFITS
        if R2 == 2:
            print("THE STREET CREWS BOUGHT ALL YOUR")
            print("LEMONADE AT LUNCHTIME!!")
        # elif R3 == 3: # unreachable
        #     goto 2350
    for I in range(N):
        if A[I] < 0:
            A[I] = 0
        if R2 != 2:
            if P[I] < P9:
                N1 = (P9 - P[I]) / P9 * .8 * S2 + S2
            else:
                N1 = ((P9 ** 2) * S2 / P[I] ** 2)
            W = - S[I] * C9
            V = 1 - (math.exp(W) * C2)
            N2 = R1 * (N1 + (N1 * V))
            N2 = min(int(N2 * G[I]), L[I])
        else:
            N2 = L[I]
        M = N2 * P[I] * .01
        E = S[I] * S3 + L[I] * C1
        P1 = M - E
        A[I] = A[I] + P1
        # if H[I] == 1: # unreachable
        #     goto 2300
        print()
        if B[I] == 1:
            print(f"STAND {I+1}   BANKRUPT")
            print()
            input(prompt)
        else:
            print(f"   DAY {D:2}                    STAND {I+1}")
            print()
            print(f"{N2:4}  GLASSES SOLD")
            print()
            print(f"${P[I]/100:.2f} PER GLASS           INCOME ${M:.2f}")
            print()
            print(f"{L[I]:4}  GLASSES MADE")
            print()
            print(f"{S[I]:4}  SIGNS MADE        EXPENSES ${E:.2f}")
            print()
            print(f"               PROFIT  ${P1:.2f}")
            print()
            print(f"               ASSETS  ${A[I]:.2f}")
            print()
            input(prompt)
            if A[I] <= C / 100:
                print()
                print("  ...YOU DON'T HAVE ENOUGH MONEY LEFT")
                print(" TO STAY IN BUSINESS  YOU'RE BANKRUPT!")
                B[I] = 1
                print()
                input(prompt)
    if min(B) == 1:
        break
    R1 = 1
    R2 = 0
