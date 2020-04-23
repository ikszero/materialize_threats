#from svg.path import CubicBezier
#from svg.path import parse_path
from .Curve import Curve


class CurveFactory:
    def __init__(self, coords):
        super(CurveFactory, self).__init__()
        self.coords = coords

    def from_xml(self, xml):
        geometry = xml.find('mxGeometry')
        points = geometry.findall('mxPoint')

        for point in points:
            x = int(point.get('x'))
            y = int(point.get('y'))
            
            if point.get('as') == 'sourcePoint':
                start = complex(x, y)
            elif point.get('as') == 'targetPoint':
                end = complex(x, y)

        if start and end:
            return Curve(start=start, end=end, cb=None)
'''
    def from_svg(self, svg_path):
        path = parse_path(svg_path)
        start = self.coords.complex_translate(path[0].start)
        end = self.coords.complex_translate(path[1].end)
        cb = None
        if isinstance(path[1], CubicBezier):
            # TODO: needs to account for multiple bezier in path
            points = [path[1].start, path[1].control1, path[1].control2, path[1].end]
            if not Curve.is_linear(points):
                cb = [self.coords.complex_translate(p) for p in points]
        return Curve(start=start, end=end, cb=cb)
'''