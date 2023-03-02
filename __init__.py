import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class LocationKoi:
    def __init__(self):
        self.data_dict = []
        with open('./reverse_geocode_bd/small_bangladesh_geojson_adm4_5160_unions_thanas.json') as f:
            data = json.load(f)
        features = data['features']
        for feature in features:
            geometry = feature['geometry']
            properties = feature['properties']
            division = properties['ADM1_EN']
            district = properties['ADM2_EN']
            upazila = properties['ADM3_EN']
            union = properties['ADM4_EN']
            poly = self.get_poly(geometry)
            self.data_dict.append(
                {'district': district, 'division': division, 'upazila': upazila, 'union': union, 'poly': poly})

    def find(self, x, y):
        ret = {}
        point = Point(x, y)
        for region in self.data_dict:
            poly = region['poly']
            polygon = Polygon(poly)
            if point.within(polygon):
                ret['division'] = region['division']
                ret['district'] = region['district']
                ret['upazila'] = region['upazila']
                ret['union'] = region['union']
        return ret

    def get_poly(self, geometry):
        poly = []
        for c1 in geometry['coordinates']:
            for c2 in c1:
                for c3 in c2:
                    if type(c2[0]) == float:
                        poly.append(c2)
                    else:
                        for c4 in c3:
                            poly.append(c3)
        return poly


def search(x, y):
    loc = LocationKoi()
    return loc.find(x, y)
