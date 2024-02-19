secret_word = input("Enter a word: ")

while secret_word != "chupacabra":
    
    secret_word = input("Enter a word: ")
    
    if secret_word == "chupacabra":
        break
    
print("You've successfully left the loop.")
