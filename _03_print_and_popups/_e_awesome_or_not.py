from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    number = random.randint(0, 3)
    # 2. Print your variable to the console
    A1 = simpledialog.askstring(title= 'Greeter', prompt="Tell me something that you think is awesome")
    # 3. Get the user to enter something that they think is awesome
    if number==1:
        messagebox.showinfo(message="wow that is very cool")
    if number==2:
        messagebox.showinfo(message="that is kinda mid")
    if number==3:
        messagebox.showinfo(message="ain't nobody gaf lil bro who asked")
    if number==0:
        messagebox.showinfo(message="shut up")


    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
        
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
