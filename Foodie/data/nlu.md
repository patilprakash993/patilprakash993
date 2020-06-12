## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely
- okay
## intent:goodbye
- bye
- Bye!
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- See you later
- Bye bot
- Goodbye friend
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:out_of_scope
- please help with my ice cream it's dripping
- no wait go back i want a dripping ice cream but a cone that catches it so you can drink the ice cream later
- i want a non dripping ice cream
- someone call the police i think the bot died
- show me a picture of a chicken
- neither
- I want french cuisine
- i am hungry
- restaurant
- can i be shown a gluten free restaurant
- i don't care!!!!
- i do not care how are you
- again?
- oh wait i gave you my work email address can i change it?
- hang on let me find it
- stop it, i do not care!!!
- how come?
- I changed my mind
- what?
- did i break you
- that link doesn't work!
- you already have that
- this is a really frustrating experience
- no stop
- give me food
- i want food
- Can I ask you questions first?
- is it a wasteland full of broken robot parts?
- can we keep chatting?
- talk to me
- who is your favourite robot?
- can you help me to build a bot

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hello
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- good afternoon
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- hi
- gm
- ga
- GM
- GA
- GE

## intent:inform	
- [Ahmedabad](location)
- [Bangalore](location)
- [Chennai](location)
- [Delhi](location)
- [Hyderabad](location)
- [Kolkata](location)
- [Mumbai](location)
- [Pune](location)

## intent:Pricing
- I want to eat at a place between 300 and 700
- I am fine with an expensive place
- I am looking for a dinner place at less than 300
- Lesser than Rs. 300
- Rs. 300 to 700
- More than 700
## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:Asian
- asian fusion

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
