output_first_template_for_clf = '''Given the classification task definition and the class labels, generate an input that corresponds to each of the class labels.

Task: extract topic
Dialogue:
Speaker 1 : "Say, Jim, How about going for a few beers after dinner?"
Speaker 2 : "You know that is tempting but is really not good for our fitness."
Speaker 1 : "What do you mean? It will help us to relax."
Speaker 2 : "Do you really think so? I don't. It will just make us fat and act silly. Remember last time?"
Speaker 1 : "I guess you are right. But what shall we do? I don't feel like sitting at home."
Speaker 2 : "I suggest a walk over to the gym where we can play singsong and meet some of our friends."
Speaker 1 : "That's a good idea. I hear Mary and Sally often go there to play pingpong. Perhaps we can make a foursome with them."
Speaker 2 : "Sounds great to me! If they are willing, We could ask them to go dancing with us. That is excellent exercise and fun, Too."
Speaker 1 : "Good. Let's go now." 
Speaker 2 : "All right.”
Class label: friends will go gym after dinner and meet their friends
Dialogue:
Speaker 1 : "Can you do push-ups?"
Speaker 2 : "Of course I can. It's a piece of cake! Believe it or not, I can do 30 push-ups a minute."
Speaker 1 : "Really? I think that's impossible!"
Speaker 2 : "You mean 30 push-ups?"
Speaker 1 : "Yeah!" 
Speaker 2 : "It's easy. If you do exercise everyday, You can make it, Too.”
Class label: they talks about push-ups

Task: extract information of Speaker 1
Dialogue:
Speaker 1 : "Can you study with the radio on?"
Speaker 2 : "No, I listen to background music."
Speaker 1 : "What is the difference?"
Speaker 2 : "The radio has too many comercials."
Speaker 1 : "That's true, But then you have to buy a record player.”
Class label: Speaker 1 suggests studying with radio and Speaker 1 thinks studying with radio is same with listening background music while studying
Dialogue:
Speaker 1 : "Are you all right?"
Speaker 2 : "I will be all right soon. I was terrified when I watched them fall from the wire."
Speaker 1 : "Don't worry. He is an acrobat"
Speaker 2 : "I see.”
Class label: Speaker 1 relieve Speaker 2's anxiety by saying that someone is an acrobat

Task: extract feelings of Speaker 1
Dialogue:
Speaker 1 : "Hey Lydia, What are you reading?",
Speaker 2 : "I'm looking at my horoscope for this month! My outlook is very positive. It says that I should take a vacation to someplace exotic, And that I will have a passionate summer fling!",
Speaker 1 : "What are you talking about? Let me see that... What are horoscopes?",
Speaker 2 : "I'm looking at my horoscope for this month! My outlook is very positive. It says that I should take a vacation to someplace exotic, And that I will have a passionate summer fling!",
Speaker 1 : "It's a prediction of your month, Based on your zodiac sign. You have a different sign for the month and date you were born in. I was born on April 15th, So I'm an Aries. When were you born?",
Speaker 2 : "January 5th.",
Speaker 1 : "Let's see... You're a Capricorn. It says that you will be feeling stress at work, But you could see new, Exciting developments in your love life. Looks like we'll both have interesting summers!",
Speaker 2 : "That's bogus. I don't feel any stress at work, And my love life is practically nonexistent. This zodiac stuff is all a bunch of nonsense."
Class label: suspicious
Dialogue: 
Speaker 1 : "Hello, Jack. It's Mary. What are you doing in your office?",
Speaker 2 : "I am working. I often work late on Thursdays. I am busy this week.",
Speaker 1 : "Would you like to come and have dinner with us on Friday?",
Speaker 2 : "Tomorrow? No, I'm afraid I wouldn't be able to. I'm going out of the town on business.",
Speaker 1 : "What about Saturday?",
Speaker 2 : "Sorry, I never go out on Saturday evening. I always watch football on Saturday evening.",
Speaker 1 : "Will you come round next Tuesday?",
Speaker 2 : "Next Tuesday? Just a moment! It will be the 21st of May. Oh, Dear. Arm... I promised my aunt I would be at her birthday party.",
Speaker 1 : "What do you say to next Wednesday then?"
Class label: disappointed

Task:'''

input_first_template_for_gen = '''Come up with examples for the following tasks. Try to generate multiple examples when possible.

Task: extract topic
Class label: friends will go gym after dinner and meet their friends
Dialogue:
Speaker 1 : "Say, Jim, How about going for a few beers after dinner?"
Speaker 2 : "You know that is tempting but is really not good for our fitness."
Speaker 1 : "What do you mean? It will help us to relax."
Speaker 2 : "Do you really think so? I don't. It will just make us fat and act silly. Remember last time?"
Speaker 1 : "I guess you are right. But what shall we do? I don't feel like sitting at home."
Speaker 2 : "I suggest a walk over to the gym where we can play singsong and meet some of our friends."
Speaker 1 : "That's a good idea. I hear Mary and Sally often go there to play pingpong. Perhaps we can make a foursome with them."
Speaker 2 : "Sounds great to me! If they are willing, We could ask them to go dancing with us. That is excellent exercise and fun, Too."
Speaker 1 : "Good. Let's go now." 
Speaker 2 : "All right.”
Class label: they talks about push-ups
Dialogue:
Speaker 1 : "Can you do push-ups?"
Speaker 2 : "Of course I can. It's a piece of cake! Believe it or not, I can do 30 push-ups a minute."
Speaker 1 : "Really? I think that's impossible!"
Speaker 2 : "You mean 30 push-ups?"
Speaker 1 : "Yeah!" 
Speaker 2 : "It's easy. If you do exercise everyday, You can make it, Too.”

Task: extract information of Speaker 1
Class label: Speaker 1 suggests studying with radio and Speaker 1 thinks studying with radio is same with listening background music while studying
Dialogue:
Speaker 1 : "Can you study with the radio on?"
Speaker 2 : "No, I listen to background music."
Speaker 1 : "What is the difference?"
Speaker 2 : "The radio has too many comercials."
Speaker 1 : "That's true, But then you have to buy a record player.”
Class label: Speaker 1 relieve Speaker 2's anxiety by saying that someone is an acrobat
Dialogue:
Speaker 1 : "Are you all right?"
Speaker 2 : "I will be all right soon. I was terrified when I watched them fall from the wire."
Speaker 1 : "Don't worry. He is an acrobat"
Speaker 2 : "I see.”

Task: extract feelings of Speaker 1
Dialogue:
Speaker 1 : "Hey Lydia, What are you reading?",
Speaker 2 : "I'm looking at my horoscope for this month! My outlook is very positive. It says that I should take a vacation to someplace exotic, And that I will have a passionate summer fling!",
Speaker 1 : "What are you talking about? Let me see that... What are horoscopes?",
Speaker 2 : "I'm looking at my horoscope for this month! My outlook is very positive. It says that I should take a vacation to someplace exotic, And that I will have a passionate summer fling!",
Speaker 1 : "It's a prediction of your month, Based on your zodiac sign. You have a different sign for the month and date you were born in. I was born on April 15th, So I'm an Aries. When were you born?",
Speaker 2 : "January 5th.",
Speaker 1 : "Let's see... You're a Capricorn. It says that you will be feeling stress at work, But you could see new, Exciting developments in your love life. Looks like we'll both have interesting summers!",
Speaker 2 : "That's bogus. I don't feel any stress at work, And my love life is practically nonexistent. This zodiac stuff is all a bunch of nonsense."
Class label: suspicious
Dialogue: 
Speaker 1 : "Hello, Jack. It's Mary. What are you doing in your office?",
Speaker 2 : "I am working. I often work late on Thursdays. I am busy this week.",
Speaker 1 : "Would you like to come and have dinner with us on Friday?",
Speaker 2 : "Tomorrow? No, I'm afraid I wouldn't be able to. I'm going out of the town on business.",
Speaker 1 : "What about Saturday?",
Speaker 2 : "Sorry, I never go out on Saturday evening. I always watch football on Saturday evening.",
Speaker 1 : "Will you come round next Tuesday?",
Speaker 2 : "Next Tuesday? Just a moment! It will be the 21st of May. Oh, Dear. Arm... I promised my aunt I would be at her birthday party.",
Speaker 1 : "What do you say to next Wednesday then?"
Class label: disappointed
Task:'''