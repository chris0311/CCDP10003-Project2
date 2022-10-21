# define characters
define y = Character('You', color="#c8ffc8")
define mary = Character('Mary', color="#c8c8ff")
define maud = Character('Maud', color="#ffc8c8")
define h = Character('Harold', color="#c8c8c8")

# define images
image maud_happy = "ai_discuss/maud_happy.png"
image maud_sad = "ai_discuss/maud_sad.png"
image maud_serious = "ai_discuss/maud_serious.png"


label start:
    play music "audio/Memories of Those Distant Days.mp3"
    scene bg afternoon_beach
    with fade

    "On a sunny day, you and Mary are out at a beach..."

    show mary angry at left
    mary "I'm sorry, but I'm looking for somebody a bit more brave and helpful. 
        Somebody who faces his fears head-on and helps somebody out."
    
    show you emoless at right
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
    play music "audio/JINBAO - YourSmile.mp3"
    scene bg night_street
    with fade

    "You are walking on the street after dinner and see your friend, Harold"

    show harold cry at left
    show you emoless at right

    y "Is everything okay?"
    h "I'm afraid not."
    y "What's wrong?"
    h " It's ... a crazy person ... I saw a crazy person eating a bunch of people!"

    show you shocked at right
    y "What?!"
    y "That's horrible!"

    menu:
        "But let's stay out of it. I don't wanna die...":
            play music "audio/angry.mp3"
            jump at_ninght_do_nothing
        "Let's do something":
            play music "audio/angry.mp3"
            jump at_night_final


label at_ninght_do_nothing:
    scene bg night_street
    with fade
    show harold angry at left

    h "You are such a coward!"
    h "Do you remember what Mary said to you?"
    
    hide harold angry
    show you thinking at right
    "Mary...Right, she likes brave people..."

    show you happy at right
    y "You are right. We've got to do something."

    jump at_night_final


label at_night_final:
    show harold smile at left
    h "Yes, I agree."

    show harold defau at left
    h "But I don't know where to start."
    show you thinking at right
    y "You can start by telling me where it happened"

    show harold cry2 at left
    h "I'm not sure I want to go back there."
    y "Come on, we've got to do something."
    y "Where did it happen?"
    h "It was in the park! That's where I saw it!"
    y "Let's go there!"

    play music "<from 4>audio/Two Steps From Hell,Thomas Bergersen - El Dorado (Dubstep Remix).mp3"
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

    "You, closely followed by Harold, rushes towards Maud but suddenly stop in her tracks."

    show harold angry at left
    h "What is it? What's wrong?"
    show you shocked at right
    y "That's not just any crazy person. That's Maud Pitt!"
    h "Who's Maud Pitt?"
    y "Who's Maud Pitt? Who's Maud Pitt? The evilest person in the world!"
    h "We're going to need some help if we're going to stop the evilest person in the universe!"
    
    hide harold angry
    show maud crazy at left
    maud "Hey, we meet again!"
    hide maud crazy
    show harold shocked at left
    h "You've met?"
    show you emoless at right
    y "Yes, it was a long, long time ago."
    y "He's a game enthusiast..."

    hide maud crazy
    hide harold shocked
    hide you emoless
    jump back_in_time


label back_in_time:
    play music "audio/Memories of Those Distant Days.mp3"
    show bg library
    with fade

    show maud young at left
    maud "I really wanted to make my own visual novel, but I can't draw..."
    show you young at right
    y "You should really try and attend some drawing lessons"
    maud "I don't have the money and time for that"
    maud "I wish I could draw when I was born..."
    maud "I tried to learn on my own, but it doesn't work"
    maud "I tried really hard. But I just can't draw... I can't draw!!!"
    maud "WHYYYYYYY"
    hide maud young
    hide you young

label back_to_present:
    play music "<from 10>audio/Two Steps From Hell,Thomas Bergersen - El Dorado (Dubstep Remix).mp3"
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
    y "You can fulfill your dream now with AI!"
    y "You can use AI to draw for you!"
    show maud crazy at left
    maud "AI? Haugh, I don't believe in that!"
    maud "The drawing must be weird and crappy!"
    y "No, it's not!"
    y "I've seen it myself!"
    y "You should definitely try it!"
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
    maud "That's a great idea!"
    y "Let's go!"

    hide maud happy
    hide you happy
    jump good_ending


label good_ending:
    play music "audio/Jeremy Kim - happy digital anthem.mp3"
    show bg sunset_beach
    with fade
    "One day you are walking on the beach, and suddenly you see Mary."
    
    show mary grin at left
    mary "Heyyyyyyy"
    mary "Is it true? Did you just help and stop Maud?"
    mary "Is everyone safe now?"
    show you happy at right
    y "Well...it does seem that way!"

    show mary shy at left
    mary "I'm really sorry for what I said before. I was just being selfish."
    mary "I'm really glad you helped Maud."
    mary "You are such a brave and helpful person!"
    show mary grin at left
    show you shy at right
    mary "You're my hero!"

    hide mary grin
    hide you shy
    show bg sunset_beach_kissing
    "YOU SAVED THE WORLD"
    "THE END"

    menu:
        "Play again":
            jump start

        "See what happens if you let Maud accept the truth":
            play music "<from 10>audio/Two Steps From Hell,Thomas Bergersen - El Dorado (Dubstep Remix).mp3"
            jump accept_truth

        "See more discussion on AI Drawing":
            jump ai_drawing_discussion_start


label accept_truth:
    hide you thinking
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
    
    stop music
    play sound "audio/scream.mp3"

    hide you angry2
    "MAUD WENT CRAZY AND ATE YOU"
    "YOU DIED, AND THE WORLD IS IN DANGER"
    "THE END"
    hide maud crazy
    stop sound
    menu:
        "Play again":
            jump start

        "See what happens if you introduce AI to Maud":
            play music "<from 10>audio/Two Steps From Hell,Thomas Bergersen - El Dorado (Dubstep Remix).mp3"
            jump using_ai

        "See more discussion on AI Drawing":
            jump ai_drawing_discussion_start


label ai_drawing_discussion_start:
    play music "<from 30>audio/limitless.mp3"
    show bg bedroom
    with fade
    "After knowing AI Drawing, Maud began to make his game."
    "However, Maud found some problems..."
    "Look at the problems Maud encountered:"
    menu:
        "Barriers of using":
            jump difficult_to_use
        "Poor drawing quality":
            jump poor_drawing_quality
        "No copyright":
            jump no_copyright

label difficult_to_use:
    show bg maud_working
    with fade

    show maud_serious at left
    maud "Why is this thing so difficult to use?"
    maud "I need to read through pages and pages of manuals to use it properly!"
    maud "That's horrible..."
    hide maud_serious
    "When Maud can finally be able to start and use it..."
    show maud_sad at left
    maud "Oh no..."
    maud "I still need to remember all the commands and keywords..."
    maud "that is another pages of manuals to read..."
    hide maud_sad

    "Maud is at the edge of getting crazy again..."
    
    "Continue to explore:"
    menu:
        "Poor drawing quality":
            jump poor_drawing_quality
        "No copyright":
            jump no_copyright
        "See some benefits":
            jump benefits_start
        "Back to the story":
            jump start
        "Quit":
            return

label poor_drawing_quality:
    show bg maud_working
    with fade
    show maud_happy at left
    maud "Finally... I can start to draw my own picture!"
    maud "Let me start by drawing one person jumping on the street happily!"
    "Maud typed in: \"one person happily jumping on the street in the morning\" as the command."
    hide maud_happy
    "Around 20 seconds later..."
    show maud_sad at left
    show bg bad_quality1
    maud "Why my picture quality is so bad?"
    maud "The person is three stories tall with fingers being cut off!"
    maud "The face is so ugly!"
    show bg bad_quality2
    maud "And the picture is so blurry... I can barely use it for my visual novel!"

    "Maud is at the edge of getting crazy again..."
    hide maud_sad

    "Continue to explore:"
    menu:
        "Barriers of using":
            jump difficult_to_use
        "No copyright":
            jump no_copyright
        "See some benefits":
            jump benefits_start
        "Back to the story":
            jump start
        "Quit":
            return

label no_copyright:
    show bg maud_working
    with fade
    show maud_happy at left
    maud "Finally... I finished drawing all my pictures via AI!"
    hide maud_happy
    "Maud's game is ready to be published..."
    "However, Maud starts to find controversies around AI Drawings..."
    show maud_serious at left
    maud "Oh no..."
    show bg protest1 with fade
    maud "People are protesting against AI Drawings because they think AI is stealing their work"
    show bg protest2
    maud "People say AI drawings are trained based on other people's drawings without seeking authorization before using them..."
    maud "Should I use them in my game?"
    hide maud_serious
    "Unfortunately, no one can answer Maud's question at this moment as there are still a lot 
    of controversies around this issue"
    "Maud is at the edge of getting crazy again..."

    "Continue to explore:"
    menu:
        "Barriers of using":
            jump difficult_to_use
        "Poor drawing quality":
            jump poor_drawing_quality
        "See some benefits":
            jump benefits_start
        "Back to the story":
            jump start
        "Quit":
            return

label quit:
    play music "audio/end_music.mp3" fadein 1.0
    show bg forest1
    with fade
    "My last thoughts:"
    "Sorry for the dumb plot and any errors you've encountered. This is my first time making a visual novel."
    "What happened to Maud is what I encountered when I created this game."
    "But it made me realize how fast AI is evolving -- AI paintings are not usable at all when I'm doing my project 1..."
    show bg forest2
    with fade
    "And let's not forget that it is the need for visual novels that made AI drawing available. Games made the world invent innovative things; games are reshaping the world!"
    "There are undoubtedly many problems with AI Drawing, but I still think it is  an excellent tool to help, especially for those like me who are poor at drawing"
    show bg city_night2
    "Thank you for watching"
    return

label benefits_start:
    play music "audio/upbeat.mp3" fadein 1.0
    show bg city_night1
    with fade

    "See some benefits of AI Drawing:"
    "Chose one to explore"
    menu:
        "Revolute the visual novel industry":
            jump revolute
        "Can be used in many other aspects":
            jump various_usage
        "Back to the story":
            jump start

label revolute:
    show bg office
    with fade
    "Drawing used to be a labor-intensive job in the past -- you need to draw every single picture by yourself, which is time-consuming and expensive."
    "Also, drawing skills might have stopped many enthusiasts from creating their own visual novels (like maud)."
    show bg cyberpunk
    "With this new technology, theoretically, in the future, anyone with a plot in their mind can create their own visual novel without drawing skills."
    "Meanwhile, drawers can use AI to increase their drawing speed as well as provide inspiration."

    "See other benefits of AI Drawing:"
    menu:
        "Can be used in many other aspects":
            jump various_usage
        "Back to the story":
            jump start  
        "View current issues with AI Drawing":
            jump ai_drawing_discussion_start
        "Quit":
            return

label various_usage:
    show bg classroom
    with fade

    "AI Drawing can be used in many other aspects, other than creating a visual novel for entertainment (although it is why AI drawing is created)."
    "As it is proven that more interactive or less rigid ways of learning can help people learn better, AI drawings can help."
    show bg classroom_happy1 with fade
    "Teachers can, instead of using boring slides that show white background and black print, use AI drawings to enhance their presentations."
    "Moreover, teachers can potentially transfer their contents into a story and use AI drawings to create a visual novel to help students learn better."
    show bg classroom_happy2 with fade
    "Students, on the other hand, can use AI drawings to create their projects, for example, creating a game to demonstrate their knowledge, which will make projects more fun to make. 
    (AI coding is also potentially a very good tool to help students and teachers to build their games/novels, but that's another story.)"

    "See other benefits of AI Drawing:"
    menu:
        "Revolute the visual novel industry":
            jump revolute
        "Back to the story":
            jump start  
        "View current issues with AI Drawing":
            jump ai_drawing_discussion_start
        "Quit":
            return
