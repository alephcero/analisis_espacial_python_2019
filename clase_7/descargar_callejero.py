import osmnx as ox
G = ox.graph_from_place('Buenos Aires, Argentina', network_type='drive')
ox.save_graph_shapefile(G, filename='caba_red',folder='../carto')
ox.save_graphml(G, filename='caba_callejero.graphml',folder='../carto')
