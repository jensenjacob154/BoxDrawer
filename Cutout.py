
#   Cutout.py
#   Handles all jointing operations
#   Jacob Jensen - November 2022

from Path import Path

import math
import math

materialThickness = 6; # [mm]
toothWidth = 6; # [mm]
cutWidth = 600; #[mm]

class Cutout:
    def __init__(self, dx, dy, globalXOffset = 0):
        self.dx = dx;
        self.dy = dy;
        self.paths = [];
        self.gbxo = globalXOffset;
        
    def Texturize(self, side, isDominant):
        dim = self.dy;
        yOffset = self.dx;
        yDir = materialThickness;
        xOffset = materialThickness + self.gbxo;
        if (side % 2 == 0):
            dim = self.dx;
            yOffset = self.dy;
            
        toothCount = round((dim-toothWidth - 2*materialThickness) / (2*toothWidth));
        
        if (toothCount < 1):
            toothCount = 1;
            
        atw = (dim - 2*materialThickness) / (2*toothCount+1);
        
        if ((side == 0) or (side == 1)):
            yOffset = 0;
            
        if ((side == 3) or (side == 2)):
            yDir *= -1;
            
        if (not isDominant):
            yDir *= -1;
            yOffset -= yDir;
            
        
        
        xT = [0];
        yT = [yOffset];
        for i in range(toothCount):
            xT.append(i*2*atw + xOffset);
            xT.append(i*2*atw + atw + xOffset);
            xT.append(i*2*atw + atw + xOffset);
            xT.append(i*2*atw + atw * 2 + xOffset);
            
            yT.append(yOffset);
            yT.append(yOffset);
            
            yT.append(yDir + yOffset);
            yT.append(yDir + yOffset);
            
        xT.append(toothCount*2*atw + xOffset);
        xT.append(toothCount*2*atw + atw + 2*xOffset);
        yT.append(yOffset);
        yT.append(yOffset);
    
        if (side % 2 == 0):
            self.paths.append(Path(xT, yT));
        else:
            self.paths.append(Path(yT, xT));
    
    def FlatTexturize(self, side):
        dim = self.dy;
        yOffset = self.dx;
        yDir = materialThickness;
        xOffset = materialThickness + self.gbxo;
        if (side % 2 == 0):
            dim = self.dx;
            yOffset = self.dy;
            
        toothCount = round((dim-toothWidth - 2*materialThickness) / (2*toothWidth));
        
        if (toothCount < 1):
            toothCount = 1;
            
        atw = (dim - 2*materialThickness) / (2*toothCount+1);
        
        
        if ((side == 0) or (side == 1)):
            yOffset = 0;
            
        if ((side == 3) or (side == 2)):
            yDir *= -1;
            
        
        xT = [0];
        yT = [yOffset];
        xT.append(toothCount*2*atw + xOffset);
        xT.append(toothCount*2*atw + atw + 2*xOffset);
        yT.append(yOffset);
        yT.append(yOffset);
    
        if (side % 2 == 0):
            self.paths.append(Path(xT, yT));
        else:
            self.paths.append(Path(yT, xT));
    
    def CutTexture(self, isHorizontal, loca, tOffset = 0, tLength = 0):
    
        dim = self.dy;
        yOffset = self.dx;
        yDir = materialThickness;
        xOffset = materialThickness + self.gbxo;
        if (not isHorizontal):
            dim = self.dx;
            yOffset = self.dy;
        
        
        yOffset = loca - materialThickness / 2;    
        
        if (tLength != 0):
            dim = tLength;
        
        toothCount = round((dim-toothWidth - 2*materialThickness) / (2*toothWidth));
        
        if (toothCount < 1):
            toothCount = 1;
            
        atw = (dim - 2*materialThickness) / (2*toothCount+1);
        xOffset += atw;
        xOffset += tOffset;
        
        for i in range(toothCount):
            xT = [];
            yT = [];
            
            xT.append(i*2*atw + xOffset);
            xT.append(i*2*atw + atw + xOffset);
            xT.append(i*2*atw + atw + xOffset);
            xT.append(i*2*atw + xOffset);
            xT.append(i*2*atw + xOffset);
            
            yT.append(yOffset);
            yT.append(yOffset);
            yT.append(yDir + yOffset);
            yT.append(yDir + yOffset);
            yT.append(yOffset);
    
            if (not isHorizontal):
                self.paths.append(Path(xT, yT));
            else:
                self.paths.append(Path(yT, xT));
    
    def CutSlot2(self, isHorizontal, loca, tOffset = 0, tLength = 0):
    
        dim = self.dy;
        yOffset = self.dx;
        yDir = materialThickness;
        xOffset = materialThickness + self.gbxo;
        if (not isHorizontal):
            dim = self.dx;
            yOffset = self.dy;
        
        
        yOffset = loca - materialThickness / 2;    
        
        if (tLength != 0):
            dim = tLength;
        
        toothCount = round((dim-toothWidth - 2*materialThickness) / (2*toothWidth));
        
        if (toothCount < 1):
            toothCount = 1;
            
        atw = (dim - 2*materialThickness) / (2*toothCount+1);
        xOffset += atw;
        xOffset += tOffset;
        
        for i in range(toothCount):
            xT = [];
            yT = [];
            
            xT.append(i*2*atw + xOffset);
            xT.append(i*2*atw + atw + xOffset);
            xT.append(i*2*atw + atw + xOffset);
            xT.append(i*2*atw + xOffset);
            xT.append(i*2*atw + xOffset);
            
            yT.append(yOffset);
            yT.append(yOffset);
            yT.append(yDir + yOffset);
            yT.append(yDir + yOffset);
            yT.append(yOffset);
    
            if (not isHorizontal):
                self.paths.append(Path(xT, yT));
            else:
                self.paths.append(Path(yT, xT));
    
    def CutSlot(self, isHorizontal, loca):
    
        dim = self.dy;
        yOffset = self.dx;
        yDir = materialThickness;
        xOffset = materialThickness + self.gbxo;
            
        yOffset = loca - materialThickness / 2;    
        
        toothCount = round((dim-toothWidth - 2*materialThickness) / (2*toothWidth));
        
        if (toothCount < 1):
            toothCount = 1;
            
        xOffset = 0;
        if isHorizontal:
            xOffset = dim / 2;
        
        xT = [];
        yT = [];
        
        xT.append(0 + xOffset);
        xT.append(dim / 2 + xOffset);
        xT.append(dim / 2 + xOffset);
        xT.append(0 + xOffset);
        xT.append(0 + xOffset);
        
        yT.append(yOffset);
        yT.append(yOffset);
        yT.append(yDir + yOffset);
        yT.append(yDir + yOffset);
        yT.append(yOffset);

        self.paths.append(Path(yT, xT));
    
    def GetBounds(self):
        return [max(xs), max(ys)];
            
    def OptimizeCuts(self):
        newPaths = [];
    
        roundTrips = [];
        oneWayTrips = [];
        
        for path in self.paths:
            if ((path.xs[0] == path.xs[-1]) and (path.ys[0] == path.ys[-1])):
                roundTrips.append(path);
            else:
                oneWayTrips.append(path);
        
        # Check for null cutout
        if ((len(roundTrips) == 0) and (len(oneWayTrips) == 0)):
            return;
        
        # Start with inner cutouts
        newPaths = newPaths + roundTrips;
        
        if (len(newPaths) == 0):
            # In case no inner cutouts, jump start the optimization with first path
            newPaths.append(oneWayTrips.pop(0));
        
        # Finish with outer cutouts using a greedy distance optimization
        while (len(oneWayTrips) > 0):
            
            lastPath = newPaths[-1];
            lastPoint = [lastPath.xs[-1], lastPath.ys[-1]];
            
            removePath = oneWayTrips[0];
            shortestPath = oneWayTrips[0];
            shortestPoint = [shortestPath.xs[0], shortestPath.ys[0]];
            shortestDist = math.dist(shortestPoint, lastPoint);
            
            for path in oneWayTrips:
                currentPoint = [path.xs[0], path.ys[0]];
                currentPointR = [path.xs[-1], path.ys[-1]];
                if (shortestDist > math.dist(lastPoint, currentPoint)):
                    shortestDist = math.dist(lastPoint, currentPoint);
                    shortestPath = path;
                    removePath = path;
                if (shortestDist > math.dist(lastPoint, currentPointR)):
                    shortestDist = math.dist(lastPoint, currentPointR);
                    shortestPath = path.Reverse();
                    removePath = path;
            
            oneWayTrips.remove(removePath);
            newPaths.append(shortestPath);
    
        # Prioritize paths which start and end at the same point
        # Then 
    
        self.paths = newPaths;
        
    def DrawAt(self, ostr, x0, y0):
        
        self.OptimizeCuts();
        
        for p in (self.paths):
    
            xOut = [x+x0 for x in p.xs];
            yOut = [y+y0 for y in p.ys];
        
            ostr.WritePath(xOut, yOut);
        
