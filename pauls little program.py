# a program to do something nonsensical

import time

print('hello. Today we are going to play a little game.')
time.sleep(1)
print('you ready?')
ready=input()
if ready=='yes':
    print('Good. I like your attitude')
else:
    print('you\re not going to enjoy this much then...')
time.sleep(1)
print('how old are you today?')
age=input()
if int(age)>99:
    print('you\'re being naughty and telling a little white lie')
elif int(age)<5:
        print('you\'re itty bitty fingers are going to get you far in life')
print('Nice to meet you ' + age + ' year old human.')
time.sleep(1)
print('I know that i\'m a computer and all but do you want to hear me stutter?')
stutter=input()
if stutter=='yes' or stutter=='Yes' or stutter=='YES':
    print('great')
    time.sleep(1)
    print('what would you like me to try to say?')
    theWord=input()
else:
    print('you\'re no fun.')
    theWord='mister ' + age  + ' year old ain\'t no fun'
if theWord:
    print('how bad of a stutter should i be?')
    time.sleep(1)
    print('bad?')
    time.sleep(.5)
    print('really bad?')
    time.sleep(.5)
    print('or really, really, really, let\'s get on with it bad?')
howBad=input()
if howBad != 'bad' or 'really bad':
    howBad='reallyreallybad'
stutter=len(howBad)
for i in range(stutter): 
        print(theWord[:3],end='')
print(theWord)
print()
time.sleep(2)
print('this little program used the following functions: print(), input(), len(), int(), range(), and time()')
print('and the following statements: if, else, elif, and assignments')
print('and the boolean operator \'or\'')
time.sleep(1)
print()
print('we\'re done here.')
      
