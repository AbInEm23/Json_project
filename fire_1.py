import json
import plotly

infile = open('US_fires_9_1.json', 'r')
outfile = open('redeable_us_fires_9_1.json', 'w')

fire = json.load(infile)
json.dump(fire,outfile, indent=4)

brightness = []
lons = []
lats = []
hover_text = []

for i in fire:
    Br = i["brightness"]
    lon = i["longitude"]
    lat = i["latitude"]
    if Br >= 450:
        brightness.append(Br)
        lons.append(lon)
        lats.append(lat)

print(lons[:5])
print(lats[:5])
print(brightness[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

data =  [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [0.04 * Br for Br in brightness],
            "color": Br,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]




my_layout = Layout(title= 'US fires - 9/1/2020 through 9/13/2020 ')
fig = {'data':data,'layout':my_layout}

offline.plot(fig,filename= 'fire1.html')


print()


