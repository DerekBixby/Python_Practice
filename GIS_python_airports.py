# getFeatures function references all features in a layer, this iterates through all features in a layer to get the name and airport code
for f in layer.getFeatures():
  print(f['name'], f['iata_code'])

# This creates a text file containing name, aiport code, and x and y coordinates for each feature in the layer variable
with open('E:/Geo/Airports/project/airports.txt', 'w') as file:
  for f in layer.getFeatures():
    geom = f.geometry()
    line = '{},{},{:.2f},{:.2f}\n'.format(f['name'], f['iata_code'], geom.asPoint().y(), geom.asPoint().x())
    file.write(line)