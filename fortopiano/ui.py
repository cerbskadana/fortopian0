import pygame as pg 

class Button:
    def __inint__ (self, x ,y,width ,height, sounds_path ,color = (255,255,255)):
        self.rect = pg.Rect(x,y,width ,height)
        self.color = color 
        self.orignal_color =color 
        self.sound = pg.mixer.Sound(self.sound)

    def draw(self,surface):
        pg.draw.rect(surface, self.color ,self.rect,border_radius=15)
        pg.draw.rect (surface, (0,0,0), self.rect,2,border_radius=15)
    def handel_event(self,event):
        if event.type == pg.NOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.sound.play()
            self.color = (220.220,220)
            return True
        if event.type == pg.MOUSEBUTTONUP:
            self.color = self.original_color
            
        return False
class Slider:
    def __init__(self,x,y,w,h,val=0.5):
        self.rect = pg.Rect(x,y,w,h)
        self.circle_x = x + int(w * val)
        self.val = val
        self.dragging = False
    
    def draw(self,surface):
        pg.draw.Line(surface, (0,0,0),
                     (self.rect.x,self.rect.centery),
                     (self.rect.right, self.rect.centery),4)
        pg.draw.circle(surface, (100,149,237),
                       (self.circle_x,self.rect.centery),10)
    
    def handle_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN and(
            (event.pos[0]- self.circle_x) ** 2 + (
                event.pos[1] - self.rect.centery) ** 2) ** 0.5 < 15:
            self.dragging = True
        elif event.type ==  pg.MOUSEBUTTONUP:
            self.dragging = False
        
        if self.dragging and event.type == pg.MOUSEMOTION:
            self.circle_x = max(self.rect.left,min(event.pos[0],self.rect.right))
            self.val = (self.circle_x - self.rect.x)/ self.rect.width
            return True
        return False
        
