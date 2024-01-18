import string
import printNumber
import alphabetLower
import alphabetUpper
import ansciFirst
import ansciSecond
import ansciThird
import ansciFourth
import ansciFifth

# Kindly follow and Subscribe to us, on our various social media accounts: 

# YouTube: https://www.youtube.com/@fixitgearware
# Rumble1: https://rumble.com/c/c-5553012
# Rumble2: https://rumble.com/c/c-5553183
# GitHub:  https://github.com/fixitgearware
# LinkedIn: https://www.linkedin.com/company/fixitgearware-security/
# X (former-Twitter): https://twitter.com/fixitgearware
# Instagram: https://www.instagram.com/fixit.gearware/
# Facebook: https://www.facebook.com/fixitgearware.sec
# Discord:  https://discord.com/invite/XGSczQaDR8
# Telegram: https://t.me/fixitgearwareSecurity


# Sequence of the code file is 
# file 1: Prints number payload 'printNumber.py'
# file 2: prints alphabet in smaller letters 'alphabetLower.py'
# file 3: prints alphabet in higher letters 'alphabet.Upper.py' 
# file 4: prints ascii characters within 32 - 48 'ansciiFirst.py'
# file 5: prints ascii characters within 57 - 65 'ansciSecond.py'
# file 6: prints ascii characters within 90 - 97  'ansciThird.py'
# file 7: prints ascii characters within 122 - 127 'ansciFourth.py'
# file 8: prints ascii characters within 160 -256  'ansciFifth.py'
# file 9: 'main.py' the file to run, to generate the necessary payload. 





# Code Line 41 to 55 prints on screen instruction & receive users input to generate the specific payload character.
print("\n")
print("You can generate all your payloads for password brute-forcing automation.\n")
print(
    "The Following options are available:\n\n"+
    " Press 1 to Print payload for Numbers in range of 1-50 e.g '1','2', etc.\n"+
    " Press 2 to print payload for Alphabet in Lower case. e.g 'a','b', etc.\n"+
    " Press 3 to print payload for Alphabet in Upper case. e.g 'A','B', etc.\n"+
    " Press 4 to print payload for First ASCII characters within the range of 32-48.\n"+
    " Press 5 to print payload for Second ASCII characters within the range of 57-65.\n"+
    " Press 6 to print payload for Third ASCII characters within the range of 90-97.\n"+
    " Press 7 to print payload for Fourth ASCII characters within the range of 122-127.\n"+
    " Press 8 to print payload for Fifth ASCII characters within the range of 160-256.\n\n"
    )
var1 = int(input("Kindly Enter the Option of Payload to Generate:\t"))
print("Your Selection is:\t"+ "'"+str(var1)+"'")


# Code Line 59 to 67 conditional statement to generate 'Number' payloads between 1 to 50. 
if var1 == 1:
    
    
    print("Your selected payload '1' which generates number between 1-50. will now be printed.")
    print("\n")
    printNumber.num_print()
    print("\n")
    print("Numbers payload generating is completed. Program will now exit.")
    print("\n")

# Code Line 70 to 78 conditional statement to generate small letter alphabets a to z.
elif var1 == 2:

   
    print("Your selected payload '2' which is generating alphabet a-z in small letters will now be printed.")
    print("\n")
    alphabetLower.alphabet_lower()
    print("\n")
    print("Lowercase Alphabet payload generating is completed. Program will now exit.")
    print("\n")

# Code Line 81 to 89 conditional statement to generate Capital letter alphabets A to Z.
elif var1 == 3:

    
    print("Your selected payload '3' which is generating alphabet A-Z in Capital letters will now be printed.")
    print("\n")
    alphabetUpper.alphabet_upper() # There are
    print("\n")
    print("Uppercase Alphabet payload generating is completed. Program will now exit.")
    print("\n")

# Code Line 92 to 100 conditional statement to generate first ASCII characters between 32 to 48.
elif var1 == 4:

    print("\n")
    print("Your selected payload '4' which is generating first Ascii characters b/w 32-48.")
    print("\n")
    ansciFirst.ansci_first()
    print("\n")
    print("Ascii characters between 32-48 payload generating is completed. Program will now exit.")
    print("\n")


# Code Line 104 to 112 conditional statement to generate second ASCII characters between 58 to 65.
elif var1 == 5:

    print("\n")
    print("Your selected payload '5' which is generating second Ascii characters b/w 58-65.")
    print("\n")
    ansciSecond.ansci_second()
    print("\n")
    print("Ascii characters between 57-65 payload generating is completed. Program will now exit.")
    print("\n")


# Code Line 117 to 126 conditional statement to generate third ASCII characters between 90 to 97.

elif var1 == 6:

    print("\n")
    print("Your selected payload '6' which is generating third Ascii characters b/w 90-97.")
    print("\n")
    ansciThird.ansci_third()
    print("\n")
    print("Ascii characters between 90-97 payload generating is completed. Program will now exit.")
    print("\n")



# Code Line 131 to 139 conditional statement to generate fourth ASCII characters between 123 to 129.

elif var1 == 7:

    print("\n")
    print("Your selected payload '7' which is generating fourth Ascii characters b/w 123-129.")
    print("\n")
    ansciFourth.ansci_fourth()
    print("\n")
    print("Ascii characters between 123-129 payload generating is completed. Program will now exit.")
    print("\n")




# Code Line 145 to 153 conditional statement to generate Fifth ASCII characters between 160 to 256.
elif var1 == 8:

    print("\n")
    print("Your selected payload '8' which is generating fifth Ascii characters b/w 160-256.")
    print("\n")
    ansciFifth.ansci_fifth()
    print("\n")
    print("Ascii characters between 160-256 payload generating is completed. Program will now exit.")
    print("\n")



# Code Line 158 to 160, conditional statement if invalid input was selected. 
else:
    print("Invalid input/selection. Run 'main.py' again, and follow onscreen instructions.")
    print("\n")
    
