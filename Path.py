
#   Path.py
#   Data storage buffers for paths
#   Jacob Jensen - November 2022

class Path:
    def __init__(self, xs, ys):
        self.xs = xs;
        self.ys = ys;
        
    def Reverse(self):
        x = list(reversed(self.xs));
        y = list(reversed(self.ys));
        return Path(x, y);
