from IOStream import OutputStream
from Box import Box
from Region import Region

mainRegion = Region();

mainRegion.AddVerticalPartition(0.25);
mainRegion.AddVerticalPartition(0.50);
mainRegion.AddVerticalPartition(0.75);

mainRegion.AddHorizontalPartition(0.33);
mainRegion.AddHorizontalPartition(0.66);

#mainRegion.AddSubregion(0, 1, silverware);

b = Box(50*4+6*5, 50*3+6*4, 50);
#b.AddBottom();
b.AddSides();
b.AddRegions(mainRegion);
b.Negotiate();

out = OutputStream("Generated Files/generated.svg")

b.Draw(out);

#out.DrawBox(10, 10, 20, 10);
#out.DrawBox(30, 10, 10, 20);

out.Close();

'''
Todos:
    Add cut order optimization to cutout
    Add command line arguments for input files / Maybe a gui
'''

''' 475x475mm '''

''' 290x330mm '''