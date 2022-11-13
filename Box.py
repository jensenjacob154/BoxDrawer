
#   Box.py
#   Handles macro scale box operations
#   Jacob Jensen - November 2022

from Cutout import Cutout
from Region import Region

materialThickness = 6; # [mm]
toothWidth = 12; # [mm]
cutWidth = 600; #[mm]

class Box:
    def __init__(self, width, length, height):
        self.w = width;
        self.l = length;
        self.h = height;
        
        # 0 - Bottom
        # 1 - Front
        # 2 - Left
        # 3 - Back
        # 4 - Right
        # 5 - Top
        self.sides = [None] * 6;
        
    def AddSides(self):
        self.sides[1] = Cutout(self.w, self.h);
        self.sides[2] = Cutout(self.l, self.h);
        self.sides[3] = Cutout(self.w, self.h);
        self.sides[4] = Cutout(self.l, self.h);
        
    def AddBottom(self):
        self.sides[0] = Cutout(self.w, self.l);
        
    def AddTop(self):
        self.sides[5] = Cutout(self.w, self.l);
        
    def AddRegions(self, regs):
    
        regs.AddSides( 0, self.w, 0, self.l, self.h, self.sides);
        self.regs = regs;
        
    def Negotiate(self):
            
        self.sides[1].Texturize(1, 1);
        self.sides[1].Texturize(3, 1);
        self.sides[3].Texturize(1, 1);
        self.sides[3].Texturize(3, 1);
            
        self.sides[2].Texturize(1, 0);
        self.sides[2].Texturize(3, 0);
        self.sides[4].Texturize(1, 0);
        self.sides[4].Texturize(3, 0);
    
        if ( not (self.sides[0] is None) ):
            self.sides[0].Texturize(0, 0);
            self.sides[0].Texturize(1, 0);
            self.sides[0].Texturize(2, 0);
            self.sides[0].Texturize(3, 0);
            
            self.sides[1].Texturize(0, 1);
            self.sides[2].Texturize(0, 1);
            self.sides[3].Texturize(0, 1);
            self.sides[4].Texturize(0, 1);
        else:
            self.sides[1].FlatTexturize(0);
            self.sides[2].FlatTexturize(0);
            self.sides[3].FlatTexturize(0);
            self.sides[4].FlatTexturize(0);
    
        if ( not (self.sides[5] is None) ):
            self.sides[5].Texturize(0, 0);
            self.sides[5].Texturize(1, 0);
            self.sides[5].Texturize(2, 0);
            self.sides[5].Texturize(3, 0);
            
            self.sides[1].Texturize(2, 1);
            self.sides[2].Texturize(2, 1);
            self.sides[3].Texturize(2, 1);
            self.sides[4].Texturize(2, 1);
        else:
            self.sides[1].FlatTexturize(2);
            self.sides[2].FlatTexturize(2);
            self.sides[3].FlatTexturize(2);
            self.sides[4].FlatTexturize(2);
            
        if (not (self.regs is None)):
            self.regs.Negotiate();
            
    
    def Draw(self, ostr):
        i = 0;
        
        dim = self.w;
        if self.h > dim:
            dim = self.h;
        if self.l > dim:
            dim = self.l;
        
        
        
        for side in self.sides:
            if not ( side is None ):
                side.DrawAt(ostr, i, 0);
                i += dim + 10;
                
        if (not (self.regs is None)):
            i = self.regs.DrawAt(ostr, i, dim + 10);
            
