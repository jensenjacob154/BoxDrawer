from IOStream import OutputStream
from Box import Box
from Region import Region

mainRegion = Region();
silverware = Region();

silverware.AddVerticalPartition(0.35);
silverware.AddVerticalPartition(0.65);

mainRegion.AddHorizontalPartition(0.3);
mainRegion.AddSubregion(0, 1, silverware);

b = Box(70, 80, 60);
b.AddBottom();
b.AddSides();
b.AddRegions(mainRegion);
b.Negotiate();

out = OutputStream("generated.svg")

b.Draw(out);

#out.DrawBox(10, 10, 20, 10);
#out.DrawBox(30, 10, 10, 20);

out.Close();

'''
Todos:
    Add cut order optimization to cutout
    Add command line arguments for input files / Maybe a gui
'''