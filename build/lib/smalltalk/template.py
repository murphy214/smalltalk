import os

def make_template():
	template = '''



<html><head>
  <meta charset="utf-8">
  <title>mbview - vector</title>
  <meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
  <script src="https://rawgit.com/murphy214/99ce4a53429faff47981267e5fd26aae/raw/616cec8830390332c3e3ad6d17cd956cc7c02428/mapbox-gl.js"></script>
  <link href="https://api.tiles.mapbox.com/mapbox-gl-js/v0.42.0/mapbox-gl.css" rel="stylesheet">
  <link href="https://www.mapbox.com/base/latest/base.css" rel="stylesheet">

  <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>

  <style>
    body { margin:0; padding:0; }
    #map { position:absolute; top:0; bottom:0; width:100%; }
    .mbview_popup {
      color: #333;
      display: table;
      font-family: "Open Sans", sans-serif;
      font-size: 10px;
    }

    .mbview_feature:not(:last-child) {
      border-bottom: 1px solid #ccc;
    }

    .mbview_layer:before {
      content: '#';
    }

    .mbview_layer {
      display: block;
      font-weight: bold;
    }

    .mbview_property {
      display: table-row;
    }

    .mbview_property-value {
      display: table-cell;

    }

    .mbview_property-name {
      display: table-cell;
      padding-right: 10px;
    }
  </style>
</head>
<body>

<style>
#menu {
  position: absolute;
  top:10px;
  right:10px;
  z-index: 1;
  color: white;
  cursor: pointer;
}
#menu-container {
  position: absolute;
  display: none;
  top: 50px;
  right: 10px;
  z-index: 1;
  background-color: white;
  padding: 20px;
}
</style>

<div id="menu"><span class="icon menu big"></span></div>

<div id="menu-container">
  <h4>Filter</h4>
  <div id="menu-filter" onchange="menuFilter()" class="rounded-toggle short inline">
    <input id="filter-all" type="radio" name="rtoggle" value="all" checked="checked">
    <label for="filter-all">all</label>
    <input id="filter-polygons" type="radio" name="rtoggle" value="polygons">
    <label for="filter-polygons">polygons</label>
    <input id="filter-lines" type="radio" name="rtoggle" value="lines">
    <label for="filter-lines">lines</label>
    <input id="filter-pts" type="radio" name="rtoggle" value="pts">
    <label for="filter-pts">points</label>
  </div>
  <h4>Popup</h4>
  <div id="menu-popup" onchange="menuPopup()" class="rounded-toggle short inline">
    <input id="show-popup" type="checkbox" name="ptoggle" value="all" '="">
    <label for="show-popup">show attributes</label>
  </div>
</div>

<script>
    

// Show and hide hamburger menu as needed
var menuBtn = document.querySelector("#menu");
var menu = document.querySelector("#menu-container");
menuBtn.addEventListener('click', function() {
  popup.remove();
  if (menuBtn.className.indexOf('active') > -1) {
    //Hide Menu
    menuBtn.className = '';
    menu.style.display = 'none';
  } else {
    //Show Menu
    menuBtn.className = 'active';
    menu.style.display = 'block';

  }
}, false);

//Menu-Filter Module
function menuFilter() {
  if (document.querySelector("#filter-all").checked) {
    paint(layers.pts, 'visible');
    paint(layers.lines, 'visible');
    paint(layers.polygons, 'visible');
  } else if (document.querySelector("#filter-pts").checked) {
    paint(layers.pts, 'visible');
    paint(layers.lines, 'none');
    paint(layers.polygons, 'none');
  } else if (document.querySelector("#filter-lines").checked) {
    paint(layers.pts, 'none');
    paint(layers.lines, 'visible');
    paint(layers.polygons, 'none');
  } else if (document.querySelector("#filter-polygons").checked) {
    paint(layers.pts, 'none');
    paint(layers.lines, 'none');
    paint(layers.polygons, 'visible');
  }

  function paint(layers, val) {
    layers.forEach(function(layer) {
      map.setLayoutProperty(layer, 'visibility', val)
    });
  }
}

function menuPopup() {
  wantPopup = document.querySelector("#show-popup").checked;
}

</script>


<div id="map" class="mapboxgl-map"><div class="mapboxgl-canvas-container mapboxgl-interactive"><canvas class="mapboxgl-canvas" tabindex="0" aria-label="Map" width="1600" height="1250" style="position: absolute; width: 800px; height: 625px;"></canvas></div><div class="mapboxgl-control-container"><div class="mapboxgl-ctrl-top-left"></div><div class="mapboxgl-ctrl-top-right"></div><div class="mapboxgl-ctrl-bottom-left"><div class="mapboxgl-ctrl"><a class="mapboxgl-ctrl-logo" target="_blank" href="https://www.mapbox.com/" aria-label="Mapbox logo"></a></div></div><div class="mapboxgl-ctrl-bottom-right"><div class="mapboxgl-ctrl mapboxgl-ctrl-attrib"><a href="https://www.mapbox.com/about/maps/" target="_blank"> Mapbox</a> <a href="http://www.openstreetmap.org/about/" target="_blank"> OpenStreetMap</a> <a class="mapbox-improve-map" href="https://www.mapbox.com/map-feedback/#/0/26.038248889032054/13" target="_blank">Improve this map</a></div></div></div></div>

<script>var center = [-85.0,40.0253597813];

mapboxgl.accessToken = 'xxxxxyyyyyy';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/dark-v9',
  center: center,
  zoom: 5,
  hash: true,
  maxZoom: 30
});
map.showTileBoundaries = true

var layers = {
  pts: [],
  lines: [],
  polygons: []
}

var lightColors = [
  'FC49A3', // pink
  'CC66FF', // purple-ish
  '66CCFF', // sky blue
  '66FFCC', // teal
  '00FF00', // lime green
  'FFCC66', // light orange
  'FF6666', // salmon
  'FF0000', // red
  'FF8000', // orange
  'FFFF66', // yellow
  '00FFFF'  // turquoise
];

function randomColor(colors) {
  var randomNumber = parseInt(Math.random() * colors.length);
  return colors[randomNumber];
}

map.on('load', function () {
  var message = `{"type":"FeatureCollection","features":[{"id":12,"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[-95.76396,29.71558],[-95.76295,29.71596],[-95.76289,29.71728],[-95.76258,29.71741],[-95.76253,29.71569],[-95.76378,29.71536],[-95.76396,29.71558]]]},"properties":{"area":14373,"id":115686174,"kind":"basin","name":"ArborBendLake","sort_key":200,"source":"openstreetmap.org"}},{"id":4,"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[-95.78149,29.72456],[-95.78142,29.72489],[-95.78081,29.72505],[-95.7809,29.72455],[-95.78067,29.72432],[-95.77994,29.72409],[-95.77896,29.72425],[-95.77887,29.72402],[-95.7793,29.72389],[-95.77952,29.72342],[-95.78108,29.72451],[-95.78149,29.72456]]]},"properties":{"area":14093,"id":115686663,"kind":"basin","name":"LakeH","sort_key":200,"source":"openstreetmap.org"}}]}`

    
  function Add_Geojson(message) {
    map.addSource('a.geojson', {
      type:'geojson',
      maxzoom:14,
      data:JSON.parse(message),
    });

    var layerColor = '#' + randomColor(lightColors);

    map.addLayer({
      'id': 'county-polygons',
      'type': 'fill',
      'source': 'a.geojson',
      'filter': ["==", "$type", "Polygon"],
      'layout': {},
      'paint': {
        'fill-opacity': 0.1,
        'fill-color':  {'type': 'identity',
                'property': 'COLORKEY'}
      }
    });

    map.addLayer({
      'id': 'county-polygons-outline',
      'type': 'line',
      'source': 'a.geojson',
      'filter': ["==", "$type", "Polygon"],
      'layout': {
        'line-join': 'round',
        'line-cap': 'round'
      },
      'paint': {
        'line-color':  {'type': 'identity',
                'property': 'COLORKEY'},
        'line-width': 1,
        'line-opacity': 0.75
      }
    });

    map.addLayer({
      'id': 'county-lines',
      'type': 'line',
      'source': 'a.geojson',
      'filter': ["==", "$type", "LineString"],
      'layout': {
        'line-join': 'round',
        'line-cap': 'round'
      },
      'paint': {
        'line-color': {'type': 'identity',
                'property': 'COLORKEY'},
        'line-width': 1,
        'line-opacity': 0.75
      }
    });

    map.addLayer({
      'id': 'county-pts',
      'type': 'circle',
      'source': 'a.geojson',
      'filter': ["==", "$type", "Point"],
      'paint': {
        'circle-color':  {'type': 'identity',
                'property': 'COLORKEY'},
        'circle-radius': 2.5,
        'circle-opacity': 0.75
      }
    });

    layers.polygons.push('county-polygons');
    layers.polygons.push('county-polygons-outline');
    layers.lines.push('county-lines');
    layers.pts.push('county-pts');
  }

  Add_Geojson(message)

  function GetBounds() {
    var mb_bound = map.getBounds()
    var ne = mb_bound._ne
    var sw = mb_bound._sw
  
    var n = ne.lat
    var s = sw.lat
    var e = ne.lng
    var w = sw.lng
    var bounds = {'n':n,'s':s,'e':e,'w':w}
    return JSON.stringify(bounds)
  
  }
  var boolval = false
  
  function init() {
    // Connect to Web Socket
    ws = new WebSocket("ws://localhost:9001/");
    // Set event handlers.
    ws.onopen = function() {
      console.log("onopen");
      ws.send("Ready for Data!");
    };
    
    ws.onmessage = function(e) {
      // e.data contains received string.
      if (e.data.length == 4) { 
        ws.send(GetBounds());
      } else if (e.data.length == 3) {
        boolval = true
      } else if (boolval == true) {
        map.jumpTo(JSON.parse(e.data))
        boolval = false
      } else {
        map.getSource('a.geojson').setData(JSON.parse(e.data))

      }
    };
    
    ws.onclose = function() {
      console.log("onclose")
    };
    ws.onerror = function(e) {
      output("onerror");
      console.log(e)
    };
  }

  function onCloseClick() {
    ws.close();
  }

  init()






  
});


function displayValue(value) {
  if (typeof value === 'undefined' || value === null) return value;
  if (typeof value === 'object' ||
      typeof value === 'number' ||
      typeof value === 'string') return value.toString();
  return value;
}

function renderProperty(propertyName, property) {
  return '<div class="mbview_property">' +
    '<div class="mbview_property-name">' + propertyName + '</div>' +
    '<div class="mbview_property-value">' + displayValue(property) + '</div>' +
    '</div>';
}

function renderLayer(layerId) {
  return '<div class="mbview_layer">' + layerId + '</div>';
}

function renderProperties(feature) {
  var sourceProperty = renderLayer(feature.layer['source-layer'] || feature.layer.source);
  var typeProperty = renderProperty('$type', feature.geometry.type);
  var properties = Object.keys(feature.properties).map(function (propertyName) {
    return renderProperty(propertyName, feature.properties[propertyName]);
  });
  return [sourceProperty, typeProperty].concat(properties).join('');
}

function renderFeatures(features) {
  return features.map(function (ft) {
    return '<div class="mbview_feature">' + renderProperties(ft) + '</div>';
  }).join('');
}

function renderPopup(features) {
  return '<div class="mbview_popup">' + renderFeatures(features) + '</div>';
}

var popup = new mapboxgl.Popup({
  closeButton: false,
  closeOnClick: false
});

var wantPopup = false;

console.log('layers', layers);
map.on('mousemove', function (e) {
  // set a bbox around the pointer
  var selectThreshold = 3;
  var queryBox = [
    [
      e.point.x - selectThreshold,
      e.point.y + selectThreshold
    ], // bottom left (SW)
    [
      e.point.x + selectThreshold,
      e.point.y - selectThreshold
    ] // top right (NE)
  ];

  var features = map.queryRenderedFeatures(queryBox, {
    layers: layers.polygons.concat(layers.lines.concat(layers.pts))
  }) || [];
  map.getCanvas().style.cursor = (features.length) ? 'pointer' : '';

  if (!features.length || !wantPopup) {
    popup.remove();
  } else {
    popup.setLngLat(e.lngLat)
      .setHTML(renderPopup(features))
      .addTo(map);
  }
});

</script>



</body></html>






'''.replace('xxxxxyyyyyy',os.environ['MAPBOX_ACCESS_TOKEN'])

	with open('index.html','wb') as f:
		f.write(template)


