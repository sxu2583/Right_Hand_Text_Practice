#This will be a random sentence generator
import random

def sentence_maker():
    #The full list of words
    checker = []
    wordCount = 0
    
    #Lets read through this textfile
    with open('book.txt', 'r', encoding="utf8") as f:
        for line in f:
            for word in line.split():
                wordCount += 1
                checker.append(word)
                

    #Now lets set the size of the printed sentence
    """
    The random value tells where the sentence will start from
    if it wasnt random then we'd be writing the same sentence 
    """
    rand = random.randint(1 , wordCount)
    sentence = ""
    first_value = rand

    """
    I want a limit of 20 words so I have to check the random
    values distance from the actual count if rand is greater than
    wordCount - 20  then we want to decrease the rand value we use by
    another 20 just in case
    """
    if rand > (wordCount - 20):
        first_value = first_value - 20

    """
    Done so we have our range add it to the sentence variable
    """
    for x in range(first_value, rand + 20 ):
        sentence += checker[x]
        sentence += " "
        
    print(sentence)


def main():
    print("-----------------------------------------------")
    print("If you want to keep going press space else quit")
    print("-----------------------------------------------")
    print(" ")
    go = True
    while go:
        sentence_maker()
        response = input("")
        if response == "quit":
            break
            
if __name__ == "__main__":
    main()

