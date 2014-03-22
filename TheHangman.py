__author__ = 'Raven'
def body(word):
    tries = 6
    hint='m'
    while hint =='m':
        hint=raw_input("Do you need a hint? y/n ")
        if hint=='y':
            answer=''
            for i in range(0,len(word)):
                if word[i]==word[0]:
                    answer+=word[i]
                else:
                    answer+='-'
        elif hint == 'n':
            answer='-'*len(word)
        else:
            print "repeat!"
            hint='m'
    print answer
    were=''
    while tries>0:
        print "%d tries left" %tries
        guess=raw_input("Your letter: ")
        while guess not in letters:
            print 'Enter English letter(small)'
            guess=raw_input("Your letter: ")
        if guess in answer or guess in were:
            print "This letter has been already guessed"
        elif guess in word:
            print "Yep!"
            ans=''
            for i in range(len(word)):
                if word[i]==guess and answer[i] == '-':
                    ans+=guess
                else:
                    ans+=answer[i]
            answer=ans
            if '-' not in answer:
                print 'Congratulations! You win!'
                tries=0
            print ans
        elif tries==6:
            print "The Hangman is starter to build (- 1 try)"
            tries-=1
            print answer
        elif tries==5:
            print "The Hangman is built (- 1 try)"
            tries-=1
            print answer
        elif tries==4:
            print "The rope is hung (- 1 try)"
            tries-=1
            print answer
        elif tries==3:
            print "The Hanger is here (- 1 try)"
            tries-=1
            print answer
        elif tries==2:
            print "You are in a chair(Last try)"
            tries-=1
            print answer
        elif tries==1:
            print "The chair have been kicked out! You lose!"
            tries-=1
            print "The word was %s" %word
        were+=guess
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
words=['investigation','automobile','paper','flower','shop','telephone','window','garden','leopard','water']
print "Welcome to The Hangman!"
print
raw_input("Press Enter")
print "The rule of this game are very similar - guess the word by letters."
print "You'll have 6 tries"
raw_input("Press Enter")
print "\n"*5
print "Let's start!"
print
from random import randint
yn='y'
while yn=='y':
    key=raw_input('Enter 1 if you want to create word for smb else or enter 2 if you want to guess one of my word: ')
    if key == '1':
        word=raw_input('Enter the word: ')
        while len(word)<2:
            word=raw_input('Enter the word: ')
            for i in word:
                if i not in letters:
                    word=''
        print '\n'*50
        print "The game is starting..."
        body(word)
    elif key == '2':
        i=randint(0,len(words)-1)
        word=words[i]
        print '\n'*50
        print "The game is starting..."
        body(word)
    else:
        print "repeat!"
    yn=raw_input('Do you want to start again? y/n ')
print "Thank you for playing"