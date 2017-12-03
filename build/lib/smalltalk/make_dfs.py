#import nlgeojson as nl
import random
import nlgeojson as nl

# determines wheter coords are polygons or liens
def determine_coord_type(coords):
	breakbool = False
	count = 0
	inds = '0123456789-'
	for i in coords:
		if '[' == i and breakbool == False:
			count += 1
		else:
			for ind in inds:
				if ind == i:
					breakbool = True
	if count == 2:
		return 'lines'
	if count == 3:
		return 'polygons'




def determine_type(data):
	coordbool,coordheader = False,''
	latbool,latheader = False,''
	longbool,longheader = False,''

	for i in data.columns.values:
		if i.lower() == 'coords':
			coordbool = True
			coordheader = i
		if 'lat' in i.lower():
			latheader = i
			latbool = True
		if 'lon' in i.lower():
			longheader = i
			longbool = True

	if longbool == True and latbool == True:
		return 'points'

	if coordbool == True:
		coords = data[coordheader].iloc[0]
		return determine_coord_type(coords)

# gets a random color
def random_color():
	lightcolors = [
	  '#FC49A3', 
	  '#CC66FF', 
	  '#66CCFF', 
	  '#66FFCC', 
	  '#00FF00', 
	  '#FFCC66', 
	  '#FF6666', 
	  '#FF0000', 
	  '#FF8000', 
	  '#FFFF66', 
	  '#00FFFF' 
	]
	return lightcolors[random.randint(0,len(lightcolors)-1)]

def create_geojson(*dfs):
	totals = []
	count = 0
	for i in dfs:
		if len(i) == 2:
			i,typedf = i
		else:
			typedf = determine_type(i)
		colorkeybool = len([ii for ii in i.columns.values if ii == 'COLORKEY']) > 0
		print colorkeybool
		if colorkeybool == False:
			i['COLORKEY'] = random_color()
		if typedf == 'points':
			totals.append(nl.make_points(i,'',raw=True))
		if typedf == 'lines':
			totals.append(nl.make_lines(i,'',raw=True))
		if typedf == 'polygons':
			totals.append(nl.make_polygons(i,'',raw=True))
		
		count += 1
	return '{"type": "FeatureCollection", "features": [%s]}' % ','.join(totals)








