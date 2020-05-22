from ..io.CurveFactory import CurveFactory
from ..models.Edge import Edge


class EdgeFactory:
    def __init__(self, coords):
        super(EdgeFactory, self).__init__()
        self.curve_factory = CurveFactory(coords)

    def from_xml(self, xml, value):
        return Edge(
            sid=xml.get('id'),
            gid=xml.get('parent'),
            value=value,
            fr=xml.get('source'),
            to=xml.get('target'),
            curve=self.curve_factory.from_xml(xml)
        )
'''
    def from_svg(self, g):
        gid = SVG.get_title(g).replace("--", "->")
        fr, to = gid.split("->")
        curve = None
        if SVG.has(g, "path"):
            path = SVG.get_first(g, "path")
            if "d" in path.attrib:
                curve = self.curve_factory.from_svg(path.attrib["d"])
        return Edge(sid=g.attrib["id"], gid=gid, fr=fr, to=to, curve=curve)
'''