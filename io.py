

# File IO

from component import Geometry

class WOBJWriter(class):
    '''Take a Geormetry Object and writes it out in Wavefront OBJ Format'''

    def __init__(self, geo):
        self.geo = geo

    def write(self, dest_file, otype="wobj"):
        '''Writes out a Wavefront OBJ by default'''
        if otype == "wobj":
            self.write_wobj(dest_file)

    def write_wobj(self, dest_file):
        '''Write out the object as a Wavefront OBJ file'''
        # SETUP THE DATA
        output_lines.extend([ v.wobj_vertex() for v in self.geo.vertexList ])
        output_lines.extend([ v.wobj_texture() for v in self.geo.vertexList ])
        output_lines.extend([ v.wobj_normals() for v in self.geo.vertexList ])
        output_lines.extend([ p.wobj_face_full() for p in self.geo.polyList ])

        # WRITE
        outfile = file(dest_file,'w')
        outfile.write('\n'.join([line for line in output_lines if line]))
        outfile.close()


class XPlaneOBJReader(object):
    '''Creates a Geormetry Object from an XPlane OBJ file'''

    def __init__(self):
        self.geo = None

    def read(self, src_file):
        '''Will read in the file from the given model path'''
        self.geo = Geometry     # RESET IT TO NEW EVERYTIME IT'S READ TO MAKE SURE IT IS A CLEAN READ

        f = open(src_file)
        self.geo.rawdata = [x.strip() for x in f.readlines()]
        f.close()
        self.geo.vertexList = []
        self.geo.pointList = []
        self.geo.polyList = []
        self.geo.output_lines = ["g default"]

        # LOAD THE VERTECIES, UVs AND INDEXES
        for line in self.geo.rawdata:
            parts = line.split()

            if not parts:
                continue

            if parts[0] == 'VT':
                args = [float(x) for x in parts[1:]]
                self.geo.vertexList.append(Vertex(*args))

            if parts[0][:3] == 'IDX':
                self.geo.pointList.extend([int(x) for x in parts[1:] ])

        # LOAD THE POLYGONS
        i = 0
        while i<len(pointList):
            self.geo.polyList.append( Polygon( [ x+1 for x in pointList[i:i+3]] ) )
            i += 3  # ASSUMES 3-POINT POLYS

        return self.geo
