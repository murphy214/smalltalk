# smalltalk - Mapping in the terminal!


# What it does 

Smalltalk is designed to be used in something like a python ide where you can interface with data. Smalltalk uses nlgeojson and their representive dataframes to represent geometric datasets (there are conversion functions from geopandas to these dfs) the reason nlgeojson does this is that it can parse geojson from said dataframes 50x quicker than serialization. Big difference! So smalltalk accepts a variadic argument being a set of nlgeojson dataframes, sends it through a websocket to gl-js, gl-js removes the existing layer and puts new one on the map. Styling is either chosen randomly from a bright colorset and applied to the entire dataframe or is denoted by a COLORKEY field in the dataframe. Pretty simple really. 

# Install 
```
pip install git+https://github.com/murphy214/smalltalk
```
# Usage 

To use small talk is really simple. (See caveats on dataframes though) Just import the Map class from small talk, set an instance of that class on some variable and send dataframes to it! **It should be noted things won't work write in a script this is for an interface remember. (terminal,jupyter,etc.)**

```python
>>>from smalltalk import Map
>>>a = Map() # opens up map 
>>>data = pd.read_csv(csvfilename)
>>>a.send(data)
>>>a.send(data,data) # send two dataframes
```
