
#   Region.py
#   Handles recursive box framing
#   Jacob Jensen - November 2022

import bisect

from Cutout import Cutout

class Region:
    def __init__( self ):
        self.xPar = [];
        self.yPar = [];
        
        self.xCount = 1;
        self.yCount = 1;
        
        self.subregions = [None];
        self.pieces = [];
        self.horis = [];
        self.verts = [];
        
        # 0 - Bottom
        # 1 - Front
        # 2 - Left
        # 3 - Back
        # 4 - Right
        # 5 - Top
        self.sides = [None] * 6;
    
    def AddVerticalPartition( self, percentage ):
        bisect.insort(self.xPar, percentage);
        self.xCount += 1;
        
        self.subregions = [None] * self.xCount * self.yCount;
    
    def AddHorizontalPartition( self, percentage ):
        bisect.insort(self.yPar, percentage);
        self.yCount += 1;
        
        self.subregions = [None] * self.xCount * self.yCount;
        
    def AddSubregion( self, xInd, yInd, newRegion ):
        self.subregions[xInd * self.yCount +  yInd] = newRegion;
        
    def AddSides(self, x0, dx, y0, dy, height, sides):
    
        self.x0 = x0;
        self.dx = dx;
        
        self.y0 = y0;
        self.dy = dy;
        
        self.he = height;
        
        # 0 - Bottom
        # 1 - Front
        # 2 - Left
        # 3 - Back
        # 4 - Right
        # 5 - Top
        self.sides = sides;
        
    def Negotiate(self):
    
        for x in self.xPar:
            self.sides[1].CutTexture(1, self.x0 + self.dx * x);
            self.sides[3].CutTexture(1, self.x0 + self.dx * (1-x));
            
            s = Cutout(self.dy, self.he);
                
            for y in self.yPar:
                s.CutSlot(0, self.x0 + self.dx * y)
                
            s.Texturize(1,0);
            s.Texturize(3,0);
            
            if ( not ( self.sides[0] is None ) ):
                self.sides[0].CutTexture(1, self.x0 + self.dx * x, self.y0, self.dy);
                s.Texturize(0, 0);
            else:
                s.FlatTexturize(0);
            
            if ( not ( self.sides[5] is None ) ):
                self.sides[5].CutTexture(1, self.x0 + self.dx * (1-x), self.y0, self.dy);
                s.Texturize(2, 0);
            else:
                s.FlatTexturize(2);
                
            self.verts.append(s);
            
            
        for y in self.yPar:
            self.sides[2].CutTexture(1, self.y0 + self.dy * y);
            self.sides[4].CutTexture(1, self.y0 + self.dy * (1-y));
            
            s = Cutout(self.dx, self.he);
                
            for x in self.xPar:
                s.CutSlot(1, self.x0 + self.dx * x)
                
            s.Texturize(1,0);
            s.Texturize(3,0);
            
            if ( not ( self.sides[0] is None ) ):
                self.sides[0].CutTexture(0, self.y0 + self.dy * y, self.x0, self.dx);
                s.Texturize(0, 0);
            else:
                s.FlatTexturize(0);
            
            if ( not ( self.sides[5] is None ) ):
                self.sides[5].CutTexture(0, self.y0 + self.dy * (1-y), self.x0, self.dx);
                s.Texturize(2, 0);
            else:
                s.FlatTexturize(2);
                
            self.horis.append(s);
              
              
        
        newH = [self.sides[1]] + self.horis + [self.sides[3]];
        newV = [self.sides[2]] + self.verts + [self.sides[4]];
        
        newXp = [self.x0] + [self.dx * x - 3 for x in self.xPar] + [self.x0 + self.dx];
        newYp = [self.y0] + [self.dy * y - 3 for y in self.yPar] + [self.y0 + self.dy];
        
        if ((self.xCount > 1) or (self.yCount > 1)):
            
            for vInd in range(self.xCount):
                for hInd in range(self.yCount):
                    scopy = self.sides.copy();
                    scopy[1] = newH[hInd];
                    scopy[2] = newV[vInd];
                    scopy[3] = newH[hInd+1];
                    scopy[4] = newV[vInd+1];
                    
                    if ( not ( self.subregions[vInd * self.yCount + hInd] is None ) ):
                    
                        x1 = self.x0 + newXp[vInd];
                        x2 = self.x0 + newXp[vInd + 1];
                    
                        y1 = self.y0 + newYp[hInd];
                        y2 = self.y0 + newYp[hInd + 1];
                    
                        self.subregions[vInd * self.yCount + hInd].AddSides( x1, (x2 - x1), y1, (y2 - y1), self.he, scopy);
                        self.subregions[vInd * self.yCount + hInd].Negotiate();
            
        
        #recurse subregions

    def DrawAt(self, ostr, x, offset):
        for piece in self.pieces:
            if not ( piece is None ):
                piece.DrawAt(ostr, x, 0);
                x += offset;
        for piece in self.horis:
            if not ( piece is None ):
                piece.DrawAt(ostr, x, 0);
                x += offset;
        for piece in self.verts:
            if not ( piece is None ):
                piece.DrawAt(ostr, x, 0);
                x += offset;
        for reg in self.subregions:
            if not (reg is None):
                x = reg.DrawAt(ostr, x, offset);
        return x;
        