define d = Character('Dizzy', color="#37851A")
define k = Character('Kepler', color="#6195A8")
label start:

    d "Hey are you listening?"

    k "Huh..?"

    "I come back to reality and see a familiar face. One I know all too well.."

    k "I-Im sorry what were you saying?"

    d "Its okay, do you have an extra pencil?"

    "I quickly start to rummage through my bag and pull out a black pen"
    pause
    "\"Shit. I only have a pen\""

    k "Is a pen okay? Its all I have"

    d "Yes thats perfect thank you!"

    "Think about Dizzy?"

menu:

    "Focus on the Lesson":
        # Lesson > Enter
        jump Lesson

    "YES!":
        # Think > Leave
        jump Think

label Lesson:

    "I focus on the lesson instead of getting distracted!"
    "+ 1 Intelligence!"

    jump Enter

label Think:

    "\"Dizzy.. The most beautiful man in the world.. His antennas twitch when he thinks too hard.\""
    "\"Hes using MY pen! KYAA!! Im the luckiest man in the world!!\""
    "\"I hope he takes it home and then I can talk to him tomorrow about it! Maybe he'll invite me over to his house and then id know more about him. And when he talks to me about himself i will drop my pen near his feet and as i get up my face is inches away from his face, i lean in.. and i-\""

    d "Heres your pen!"
    pause
    "\"damnit..\""

    jump Leave


label Leave:

    "The bell rings and the class rushes out the door. Lunch time!"
    "Instead of going to the cafeteria Kepler secretly trails behind Dizzy."
    "They both arrive at a empty classroom."
    "Realizing it could be risky to just stand outside and watch through the small window Kepler has to make a choice."
    pause
    "Kepler decides to leave in case he gets caught."
    pause


label Enter:
    
    "The bell rings and the class rushes out the door. Lunch time!"
    "Instead of going to the cafeteria Kepler secretly trails behind Dizzy."
    "They both arrive at a empty classroom."
    "Realizing it could be risky to just stand outside and watch through the small window Kepler has to make a choice."
    pause
    "You decide to enter the classroom"
    d "Oh! Sorry I didnt realize this room was already in use! Ill leave now!"
    "Dizzy looks visibly scared, worried he will be in trouble."
    k "\"Theres no need!\"You spit out before he can leave." 
    k "I was just dropping off my project before class starts."
    "It was a lie but Dizzy didnt need to know that. You place a scrap piece of paper on the desk to sell it to him."
    d "Oh okay!"
    pause
    k "Youre Dizzy right? Were in the same class, you borrowed my pen!"
    d "Oh yeah! Do you want it back? I never got to catch your name"
    k "Im Kepler! And nah you can keep it, ive got plenty at home"
    d "Thanks! . . . Hey want to eat with me?"
    "\"AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\""
    k "Sure!!"
    
    