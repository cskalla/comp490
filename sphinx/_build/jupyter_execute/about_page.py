#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ipyleaflet import Map, basemaps, Marker
#enter coordinates of map center
center = (29.9511, -90.0715)
m = Map(basemap=basemaps.OpenStreetMap.Mapnik,center=center, zoom=10)
#m = Map(center=center, zoom=10)
marker = Marker(location=center, draggable=True)
m.add_layer(marker);
display(m)
# Now that the marker is on the Map, you can drag it with your mouse,
# it will automatically update the `marker.location` attribute in Python
# You can also update the marker location from Python, that will update the
# marker location on the Map:
marker.location = (50, 356)
m.save('my_map.html', title='My Map')

