# Basic Components for Polygons

class Vertex(object):
    ''' XPlane 10 Vertex '''
    def __init__(self, x, y, z, nx, ny, nz, u, v, w=None):
        self.x = x
        self.y = y
        self.z = z
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.u = u
        self.v = v
        self.w = w

    def wobj_vertex(self):
        return "v %f %f %f" % (self.x, self.y, self.z)

    def wobj_texture(self):
        return "vt %f %f" % (self.u, self.v)

    def wobj_normals(self):
        return "vn %f %f %f" % (self.nx, self.ny, self.nz)


class Polygon(object):
    '''Polygon object for Managing poly surfaces'''

    def __init__(self, points):
        self.points = points

    def wobj_face(self):
        return "f %s" % ' '.join(self.points)

    def wobj_face_full(self):
        return "f %s" % ' '.join( ["%d/%d/%d" % (x, x, x) for x in self.points] )


class Geometry(object):
    '''Geometry Object for managing Collections of Polys'''
    
    def __init__(self):
        self.rawdata = []
        self.vertexList = []
        self.pointList = []
        self.polyList = []

    def vertex_count(self):
        return len( self.vertexList )

    def poly_count(self):
        return len( self.polyList )
