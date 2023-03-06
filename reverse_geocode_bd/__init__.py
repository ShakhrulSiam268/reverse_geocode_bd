import json
import os


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def onLine(l1, p):
    # Check whether p is on the line or not
    if (
        p.x <= max(l1.p1.x, l1.p2.x)
        and p.x <= min(l1.p1.x, l1.p2.x)
        and (p.y <= max(l1.p1.y, l1.p2.y) and p.y <= min(l1.p1.y, l1.p2.y))
    ):
        return True
    return False

def direction(a, b, c):
    val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)
    if val == 0:
        # Colinear
        return 0
    elif val < 0:
        # Anti-clockwise direction
        return 2
    # Clockwise direction
    return 1

def isIntersect(l1, l2):
    # Four direction for two lines and points of other line
    dir1 = direction(l1.p1, l1.p2, l2.p1)
    dir2 = direction(l1.p1, l1.p2, l2.p2)
    dir3 = direction(l2.p1, l2.p2, l1.p1)
    dir4 = direction(l2.p1, l2.p2, l1.p2)

    # When intersecting
    if dir1 != dir2 and dir3 != dir4:
        return True

    # When p2 of line2 are on the line1
    if dir1 == 0 and onLine(l1, l2.p1):
        return True

    # When p1 of line2 are on the line1
    if dir2 == 0 and onLine(l1, l2.p2):
        return True

    # When p2 of line1 are on the line2
    if dir3 == 0 and onLine(l2, l1.p1):
        return True

    # When p1 of line1 are on the line2
    if dir4 == 0 and onLine(l2, l1.p2):
        return True

    return False

def checkInside(poly, p):
    n = len(poly)-1
    # When polygon has less than 3 edge, it is not polygon
    if n < 3:
        return False

    # Create a point at infinity, y is same as point p
    exline = line(p, Point(9999, p.y))
    count = 0
    i = 0
    while True:
        # Forming a line from two consecutive points of poly
        side = line(poly[i], poly[(i + 1) % n])
        if isIntersect(side, exline):
            # If side is intersects ex
            if (direction(side.p1, p, side.p2) == 0):
                return onLine(side, p);
            count += 1

        i = (i + 1) % n;
        if i == 0:
            break

    # When count is odd
    return count & 1;



class ReverseGeoBD:
    def __init__(self):
        self.data_dict = []
        filename = 'small_bangladesh_geojson_adm4_5160_unions_thanas.json'
        json_path = os.path.join(os.getcwd(), os.path.dirname(__file__), filename)
        with open(json_path) as f:
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
            polygon = self.get_polygon(poly)
            self.data_dict.append(
                {'district': district, 'division': division, 'upazila': upazila, 'union': union, 'polygon': polygon})

    def find(self, x, y):
        rets = []
        
        point = Point(y, x)
        for region in self.data_dict:
            ret = {}
            polygon = region['polygon']
            if(checkInside(polygon, point)):
                ret['division'] = region['division']
                ret['district'] = region['district']
                ret['upazila'] = region['upazila']
                ret['union'] = region['union']
            if ret!={}:
                rets.append(ret)
        # return rets
        if len(rets) > 0:
            return rets[0]
        else:
            return rets

    def get_poly(self, geometry):
        if geometry['type'] == 'Polygon':
            poly = geometry['coordinates'][0]
        elif geometry['type'] == 'MultiPolygon':
            poly = geometry['coordinates'][-1][0]
        return poly

    def get_polygon(self, poly):
        ret = []
        for p in poly:
            ret.append((Point(p[0], p[1])))
        return ret


def search(x, y):
    loc = ReverseGeoBD()
    val = loc.find(x, y)
    return val
