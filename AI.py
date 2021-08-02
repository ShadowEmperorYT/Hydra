def assistant():
    #LIBRARYS
    import wikipedia
    import os
    import time
    import pyttsx3
    import string
    import webbrowser
    import datetime
    #LIBRARYS <END>


    engine = pyttsx3.init()#SPEAKING VOICE


    #COMMANDS
    qus =  input("Hello how can i help you (type '?' or wikipedia) : ") 

    yt = ['open youtube' ,'Open YouTube', 'Open Youtube']
    wikki = ['wikipedia']
    mail = ['sent a mail','open mail','open gmail','sent a gamil']
    music = ['play a song','play music','play song','play']
    time = ['what time is it now','time','tell me the time','what is the time']
    hep = ['?']
    
    #COMMANDS <END>



        
    if qus in wikki:
        question = input("Type any name")
        ls = question.replace('wikipedia','')
        print ("searching...")
        
        result = wikipedia.summary(ls)
        print(result)
        engine.say(result)
        engine.runAndWait()

       
        
    elif qus in yt:
        webbrowser.open("https://www.youtube.com")
        engine.say("Opening youtube")
        engine.runAndWait()

    elif qus in mail:
        webbrowser.open("https://www.mail.google.com")
        engine.say("Opening gmail")
        engine.runAndWait()

    elif qus in music:

         webbrowser.open("https://www.spotify.com")
         engine.say("Opening spotify")
         engine.runAndWait()

    elif qus in time:
        current_time = datetime.datetime.now() 
        
        # Printing value of now. 
        print ("Time now is : "
                                    , end = "") 
        print (current_time)

        engine.say(current_time)
        engine.runAndWait()

    elif qus in hep:
         print("type'wikipedia' to open Search then type 'wikipedia <anyname>' to get summary for that topic")
         print ("type 'open youtube' to open yt")
         print ("type 'play' to open spotify")
         print ("type 'what time is it now' to know the time")
         print ("type 'sent a mail' to open gmail")
         print ("type '?' to show the list of commands")


    else:
        print("Invalid command type '?' for help or check you network connection")
    assistant()

assistant()
