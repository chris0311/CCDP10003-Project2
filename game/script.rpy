define y = Character('You', color="#c8ffc8")
define mary = Character('Mary', color="#c8c8ff")
define maud = Character('Maud', color="#ffc8c8")
define h = Character('Harold', color="#c8c8c8")

label start:

    scene bg afternoon_beach
    with fade

    "On a suuny day, you and Mary are out at a beach..."

    show mary angry at left
    mary "I'm sorry, but I'm looking for somebody a bit more brave and helpful. 
        Somebody who faces his fears head on and help somebody out."
    
    show you emotionless at right
    menu:
        y "I..."

        "I am such a person!":
            jump continue_start

        "I'm sorry...":
            jump continue_start

label continue_start:
    scene bg afternoon_beach
    with fade

    show mary angry at left
    mary "I don't want to hear from you anymore!"

    show mary emotionless at left
    mary "I'm sorry. I just don't feel excited by this relationship anymore."

    hide mary
    show you cry at right
    "You sat down, looking defeated."

    jump at_night


label at_night:

    scene bg night_street
    with fade
    show harold cry at left
    show you emotionless at right

    y "Is everything okay?"
    h "I'm afraid not."
    y "What's wrong?"
    h " It's ... a crazy person ... I saw a crazy person eating a bunch of people!"

    show you shocked at right
    y "What?!"
    y "That's horrible!"
    
    menu:
        "But let's stay out of it.":
            jump at_ninght_do_nothing
        "Let's do something":
            jump at_night_final


label at_ninght_do_nothing:
    scene bg night_street
    with fade
    show harold angry at left

    h "You are such a coward!"
    h "Did you remember what Mary said to you?"
    
    hide harold angry
    show you thinking at right
    "Mary...Right, she likes people that are brave..."

    show you happy at right
    y "You are right. We've got to do something."

    jump at_night_final


label at_night_final:
    show harold smile at left
    h "Yes, I agree."

    show harold defau at left
    h "but I don't know where to start."
    show you thinking at right
    y "You can start by teling me where it happened"

    show harold cry2 at left
    h "I'm not sure I want to go back there."
    y "Come on, we've got to do something."
    y "where did it happen?"
    h "It was in the park! Thats where I saw it!"
    y "Let's go there!"

    hide you thinking
    hide harold cry2
    "You and Harold began to run."
    jump at_park


label at_park:
    show bg night_park2
    with fade
    show maud crazy at left

    maud "Haha, who else can I eat"
    hide maud

    "You, closely followed by Harold, rushes towards Maud, but suddenly stops in her tracks."

    show harold angry at left
    h "What is it? What's wrong?"
    show you shocked at right
    y "That's not just any crazy perosn, that's Maud Pitt!"
    h "Who's Maud Pitt?"
    y "Who's Maud Pitt? Who's Maud Pitt? The most evil person in the world!"
    h "We're going to need some help if we're going to stop the most evil perosn in the universe!"
    
    hide harold angry
    show maud crazy at left
    maud "Hey, we meet again!"
    hide maud crazy
    show harold shocked at left
    h "You've met?"
    show you emoless at right
    y "Yes, it was a long, long tiem ago."
    y "He's a game enthusiast..."

    hide maud crazy
    hide harold shocked
    hide you emoless
    jump back_in_time


label back_in_time:
    show bg library
    with fade

    show maud young at left
    maud "I really wanted to make my own visual novel, but I can't draw..."
    show you young at right
    y "You should really try and attend some drawing lessons"
    maud "I don't have the money and time for that"
    maud "I wish I could draw when I was born..."
    maud "I tried to learn by my own, but it doesn't work"
    maud "I tried really hard. But I just can't draw... I can't draw!!!"
    maud "WHYYYYYYY"
    hide maud young
    hide you young

label back_to_present:
    show bg night_park2
    with fade

    show maud sad at left
    maud "I can't draw back then; I can't draw right now..."
    maud "I tried drawing for 20 years, but I still can't draw..."
    maud "I'm such a useless person"
    maud "I really want to create my own game..."
    maud "I can't control myself from eating people when I get frustrated..."

    show you thinking at right
    menu:
        y "Well... but..."

        "Have you tried using AI to draw?":
            jump using_ai
        
        "You should accept the truth":
            jump accept_truth

label using_ai:
    show bg night_park2
    with fade

    show you happy at right
    y "You may have failed back them, but you won't right now!"
    y "You can fulfill your dream now, with AI!"
    y "You can use AI to draw for you!"
    show maud crazy at left
    maud "AI? Haugh, I don't believe in that!"
    maud "The drawing must be weird and crappy!"
    y "No, it's not!"
    y "I've seen it myself!"
    y "You should defininately try it!"
    y "Let me show you!"

    jump showing_ai_demo


label showing_ai_demo:
    show bg night_park2
    with fade

    "You showed Maud this game"
    show you happy at right
    y "Look! The pictures of the game we are in are all made by AI! 
        AI paintings are brilliant! Making visual novels nowadays might not require drawing skills anymore!"

    show maud happy at left
    maud "Holy... I can't believe this! I think I can make my own game now!"
    y "Absolutely can! Let's calm down, get home, and make your game!"
    maud "that's a great idea!"
    y "Let's go!"

    hide maud happy
    hide you happy
    jump good_ending


label good_ending:
    show bg sunset_beach
    with fade
    "One day you are waling on the beach, and suddenly you see Mary."
    
    show mary happy at left
    mary "Heyyyyyyy"
    mary "Is it true? Did you just help and stop Maud?"
    mary "Is everyone safe now?"
    show you happy at right
    y "Well...it does seem that way!"
    mary "I'm really sorry what I said before. I was just being selfish."
    mary "I'm really glad you helped Maud."
    mary "You are such a brave and helpful person!"
    mary "You're my hero!"

    hide mary happy
    hide you happy
    show bg sunset_beach_kissing
    "YOU SAVED THE WORLD"
    "THE END"

    menu:
        "Play again":
            jump start

        "See what happens if you let Maud accept the truth":
            jump accept_truth

        "Quit":
            return


label accept_truth:
    show bg night_park2
    with fade

    show you angry2 at right
    y "Well... that's the truth."
    y "You should accept the truth -- you can't draw; you can't make your own game."
    y "Forget it and have another dream instead"
    show maud crazy at left
    maud "NOOOOOOOO!!!!"
    maud "I can't accept this!"
    maud "It's not possible..."
    maud "I can't be a useless person..."
    maud "I can't be a failure..."
    maud "It can't be..."
    maud "AAAAAAHHHHH"

    hide you angry2
    "MAUD WENT CRAZY AND ATE YOU"
    "YOU DIED AND THE WORLD IS IN DANGER"
    "THE END"

    menu:
        "Play again":
            jump start

        "See what happens if you introduce AI to Maud":
            jump using_ai

        "Quit":
            return


    

