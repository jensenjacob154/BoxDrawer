
#   IOStream.py
#   Handles all read/write operations for svg files
#   Jacob Jensen - November 2022

class OutputStream:
    def __init__(self, filename):
        filename = filename;
        prefix = open("Prefix.txt", "r");
    
        self.ostr = open(filename, "w");
        self.ostr.write(prefix.read());
        self.currentPath = 1;
    
    def Close(self):
        suffix = open("Suffix.txt", "r");
        self.ostr.write(suffix.read());
        
    def WritePath(self, xs, ys):
        self.ostr.write('    <path\n');
        self.ostr.write('       style="fill:none;stroke:#000000;stroke-width:0.8"\n');
        self.ostr.write('       d="M ');
        
        i = 1
        for x,y in zip(xs, ys):
            if (i == 0):
                self.ostr.write(f'{x},{y} ');
            else:
                self.ostr.write(f'{x},{y} ');
            i = 1
        
        self.ostr.write('"\n');
        self.ostr.write(f'       id="path{self.currentPath}"\n');
        self.currentPath = self.currentPath + 1;
        
    def DrawBox(self, x, y, w, h):
        xs = [x, x+w, x+w,   x, x];
        ys = [y,   y, y+h, y+h, y];
        self.WritePath(xs, ys);
