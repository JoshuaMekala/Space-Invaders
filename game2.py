from tkinter import *
import time
from Alien import *
from Explosion import Explosion
from SpaceShip import SpaceShip
from Counter import Counter
from Missile import Missile


        
########## global variable
game_over=False

######### Function
def stop_game():
    global game_over
    game_over=True

record = {"blue":0,"green":0,"red":0,"mine":0} # Dictionary used to track kills
    

    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Intialize list of missiles
    missiles=[]
    #Initialize list of Explosions
    booms=[]
    #Initialize list of Aliens
    aliens=[]
    #Initialize counter ammunition
    amunition=Counter(canvas,10)
    amunition.create_text()

    ship=SpaceShip(canvas)
    ship.activate()
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())
    root.bind("<Up>",lambda e:Missile.add_missile(canvas, missiles, ship.xtracker, ship.y))
    root.bind("<Escape>",lambda e:stop_game())

    t=0
    record_list_of_tuple = []
    while not game_over:
        if amunition.value <= 0: # If the score gets to 0 or lower the game ends
            canvas.create_text((canvas.winfo_width()*0.5),(canvas.winfo_width()*0.5)-100,text=str("GAME OVER!"),fill="orange",font=("Courier",25))
            stop_game()
            print(record)
            f1 = open("game2.txt","w")
            for time_step in record_list_of_tuple: # Write in file kill history at individual time steps
                f1.write(str(time_step[2])+" "+str(time_step[0])+" "+str(time_step[1])+" " + str(time_step[3])+"\n")
            f1.close()
        if t%100 == 0: # Spawn alien every second
                Alien.add_alien(canvas,aliens)
                record_list_of_tuple.append((record["blue"],record["green"],record["red"],record["mine"])) # Add a time step to record
        for missile in missiles:
            missile.next() # Move the missiles
        for boom in booms:
            boom.next() # Progress explosions
        for alien in aliens:
            for missile in missiles:
                if alien.is_active() and alien.is_shot(missile.x, missile.y): # Detects if alien and missile collide
                    alien.deactivate()
                    if alien.color == "blue":
                        record["blue"] += 1
                    if alien.color == "green":
                        record["green"] += 1
                    if alien.color == "red":
                        record["red"] += 1
                    if alien.color == "yellow": # Finds alien type killed and adds entry to dictionary
                        record["mine"] += 1
                    missile.deactivate()
                    amunition.increment(alien.value) # Add alien point value to score
                    Explosion.add_explosion(canvas, booms, missile.x, missile.y, 30, alien.color)
            if alien.x > ship.xtracker-(0.5*40): # Detects if alien collides with the ship
                if alien.x < ship.xtracker+(0.5*40):
                    if alien.y > canvas.winfo_height()-100:
                        alien.deactivate()
                        ship.deactivate()
                        amunition.increment(-10) # Subtract 10 points due to being hit by alien
                        Explosion.add_explosion(canvas, booms, ship.xtracker, canvas.winfo_height()-100, 20)
                        ship=SpaceShip(canvas) # Respawn the ship after it dies
                        ship.activate()

            alien.next()
        time.sleep(0.01)     
        root.update() 
        t+=1  # update the graphic (redraw)
    root.mainloop()






if __name__=="__main__":
    main()