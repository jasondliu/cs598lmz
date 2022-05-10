import bz2
bz2.decompress(open('elonmusk.json.bz2', 'rb').read())

#%% [markdown]
# ## 2. Using `pygal.maps.world.World`
# 
# Next, we will use `pygal.maps.world.World()`.
# 
# The map is currently centered on the US and looks like this:
# 
# ![](https://i.imgur.com/n1mf4q3.png)
# 
# The first step is to center this map on the Atlantic Ocean.
# In order to do this, we will use `map.set_view()`.
# It takes 4 values:
# - `latitude`
# - `longitude`
# - (optional) `delta_latitude`
# - (optional) `delta_longitude`
# 
# To get a feel for how this works, first use `map.set_view()` to rearange the map
# to show only the US:
# 
# - `latitude` should be between 30 and 50
# - `longitude
