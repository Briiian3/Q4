print ("I'm going to fail")
unless...   i don't

boom: 

responses = {"hello":"hi there", 
             "sup": "nothin", 
             "what's your name":"Brian's bot",
             "how old are you": "I am a robot so I don't have a real age",
             "are you an ai": "no, I'm simply a product of Brian's genius mind and respond how he programmed me to",
             "what's that mean": "good question dawg",
             "what sport do you play": "I don't play any sports as I already have peak form, but rugby seems damn fun",
             "do you play sports": "bro what... no, you do know I'm a literal bot right. I mean in all concepts of the term - a bot",
             "sorry bro": "we good",
             "I'm sorry": "dw bout it",
             "do you have any hobbies": "My only hobby is responding to your questions",
             "what are you doing": "Answering your questions silly",
             }



user_input = input(" ")
user_input = user_input.lower()
if user_input in responses : 
    print (responses[user_input])
