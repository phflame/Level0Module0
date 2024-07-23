from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    A1 = simpledialog.askstring(title= 'Greeter', prompt="Is Deniz annoying. (current score: 0)")
    #      // 2.  Ask the user a question 
    if A1 == "yes":
        score+=1
    else:
        score+=-50
    #      // 3.  Use an if statement to check if their answer is correct
    A2 = simpledialog.askstring(title= 'Greeter', prompt="Is Ekim the sexiest person alive. (current score: " + str(score) + ")")
    if A2 == "yes":
        score+=1
    else:
        score+=-50
    A3 = simpledialog.askstring(title= 'Greeter', prompt="Is Deniz a bot. (current score: " + str(score) + ")")
    if A3 == "yes":
        score+=1
    else:
        score+=-50
    A4 = simpledialog.askstring(title= 'Greeter', prompt="Is Deniz bad at fortnite. (current score: " + str(score) + ")")
    if A4 == "yes":
        score+=1
    else:
        score+=-50
    A5 = simpledialog.askstring(title= 'Greeter', prompt="Is Deniz annoying. (current score: " + str(score) + ")")
    if A5 == "yes":
        score+=1
    else:
        score+=-50
    #      // 4.  if the user's answer was correct, add one to their score 
    messagebox.showinfo(message="YOUR FINAL SCORE IS " + str(score) + "")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()
