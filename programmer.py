epic_programmer_dict= {'tim berners-lee' : ['tbl@gmail.com', 111],
                       'guido van rossum' : ['gvr@gmail.com',222],
                       'linus torvalds' : ['lt@gmail.com', 333],
                       'larry page' : ['lp@gmail.com', 444],
                       'tim berners-lee' : ['sb@gmail.com',555],
                       }

def searchPeople(x):
    try:
        personsInfo = epic_programmer_dict[x]
        print 'Name: ' + x.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])  
    except:
        print 'No information found for that name'

userWantsMore = True
while userWantsMore == True:
    personsName = raw_input('Please enter a name: ').lower()
    searchPeople(personsName)
    searchAgain = raw_input ('Search again? (y/n)')
    if searchAgain == 'y':
        userWantsMore = True
    elif searchAgain == 'n':
        userWantsMore = False
    else:
        print 'I dont understand what you mean, quitting'
        userWantsMore = False
        
