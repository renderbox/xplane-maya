import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import sys
from io import XPlaneOBJReader

# Initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerCommand( kPluginCmdName, cmdCreator )
    except:
        sys.stderr.write( "Failed to register command: %s\n" % kPluginCmdName )
        raise

def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand( kPluginCmdName )
    except:
        sys.stderr.write( "Failed to unregister command: %s\n" % kPluginCmdName )
        raise


class scriptedCommand(OpenMayaMPx.MPxCommand):

    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    def doIt(self, argList):
        print argList
        print "ARG LIST ABOVE"

        xpreader = XPlaneOBJReader()
        geoObj = xpreader.read("")      #PATH TO FILE FROM ARGS

        outputMesh = maya.OpenMaya.MObject()
        numFaces = len( geoObj.polyList )
        numVertices = len( geoObj.vertexList )

        print "VERT COUNT: %d" % numVertices
        print "FACE COUNT: %d" % numFaces

        UVSetNames = ['map1', 'other']

        points = maya.OpenMaya.MFloatPointArray()
        uArray = maya.OpenMaya.MFloatArray()
        vArray = maya.OpenMaya.MFloatArray()

        # CONVERT THE POINTS TO MAYA FORMAT
        print "CREATING VERTICIES"
        for vertex in geoObj.vertexList:
            p = maya.OpenMaya.MFloatPoint( vertex.x, vertex.y, vertex.z )
            points.append(p)
            uArray.append(vertex.u)
            vArray.append(vertex.v)

        # vertex connections per poly face in one array of indexs into point array given above
        faceConnects = maya.OpenMaya.MIntArray()
        for point in geoObj.pointList:
            faceConnects.append(point)

        # an array to hold the total number of vertices that each face has
        faceCounts = maya.OpenMaya.MIntArray()
        for poly in geoObj.polyList:
            faceCounts.append( len( poly.points ) )

        meshFS = maya.OpenMaya.MFnMesh()
        #newMesh = meshFS.create(numVertices, numFaces, points, faceCounts, faceConnects, outputMesh)
        newMesh = meshFS.create(numVertices, numFaces, points, faceCounts, faceConnects, uArray, vArray, outputMesh)    # ADDING THE UVs TO THE MESH AT THE SAME TIME
        meshFS.updateSurface()
        nodeName = meshFS.name()
        print 'Mesh node name is: %s' % nodeName

        # CREATE THE UV SET                             # TRYING TO REPLACE THIS WITH THE create METHOD ABOVE
        #meshFS.createUVSetWithName( UVSetNames[1] )
        #meshFS.setUVs(uArray, vArray, UVSetNames[1] )

        #assign new mesh to default shading group
        maya.cmds.sets(nodeName, e=True, fe='initialShadingGroup')



