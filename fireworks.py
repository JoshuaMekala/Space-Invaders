from tkinter import *
import time,random
from Explosion import Explosion
from Missile import Missile

        
       
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        
        my_image=PhotoImage(file="umass_campus.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h) # create a canvas width*height

        canvas.create_image(10,10,anchor=NW,image=my_image)
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        colors =["red", "green", "blue", "yellow", "orange", "purple","rainbow"] #colors that will be used in the firework

        #Initialize list of Explosions
        booms=[]
        #Initialize list of Missiles
        missiles=[]
        
        t=0
        while True:
                #picks a random place for the explosion to occur, with random colors and types of explosions. 
                for missile in missiles:
                        active = missile.is_active()
                        missile.next()
                        if active and not missile.is_active():
                                random_color = colors[random.randint(0, len(colors)-1)]
                                random_size = random.randint(100,300)
                                Explosion.add_explosion(canvas, booms, missile.x, missile.y, random_size,color=random_color)
                
                for boom in booms:
                        boom.next()
                # determines where the missile will explode with random speeds and places to detonate
                if t%50 == 0:
                        rand_x = random.uniform(0, w)
                        rand_ceiling = random.uniform(h//4, 3*h//4)
                        random_speed = random.uniform(0,7)
                        Missile.add_missile(canvas, missiles, rand_x, h, rand_ceiling, pixel_increment=random_speed)
        
                # update the graphic and wait time        
                root.update()   # update the graphic (redraw)
                time.sleep(0.01)  # wait 0.01 second  
                t=t+1      # increment time







        

if __name__=="__main__":
    main()

