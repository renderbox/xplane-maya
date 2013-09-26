import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import sys

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
        print "Hello World!"
        print argList
        print "ARG LIST ABOVE"


# import maya.OpenMaya

# def pk_makePolyPlane(width=10.0,length=10.0,subX=15,subZ=15):
#     '''pk_makePolyPlane(width=10.0,length=10.0,subX=15,subZ=15)
#     is a python script in the file
#     C:\Documents and Settings\Paul\My Documents\maya\2008\python\pythonlearning.py
#     Creates a poly plane centered at the origin of the world space. '''

#     outputMesh = maya.OpenMaya.MObject()

#     nRows = subX + 1
#     nCols = subZ + 1

#     numFaces = subX * subZ
#     numVertices = nRows * nCols
#     # point array of plane vertex local positions
#     points = maya.OpenMaya.MFloatPointArray()
#     for x in range(0,nRows,1):
#         for z in range(0,nCols,1):
#             px = width*(x/float(subX)) - width/2.0
#             py = 0.0
#             pz = length*(z/float(subZ)) - length/2.0
#             p = maya.OpenMaya.MFloatPoint( px, py, pz )
#             #print 'point:: %f, %f, %f' % (p.x, p.y, p.z)
#             points.append(p)

#     # vertex connections per poly face in one array of indexs into point array given above
#     faceConnects = maya.OpenMaya.MIntArray()
#     for row in range(0,subX,1):
#         for col in range(0,subZ,1):
#             #fID = (row * subX) + (col % subZ)
#             #print 'row:%i, col:%i, polyFaceID:%i' % (row,col,fID) 
#             index0 = ((row % nRows) * nCols) + (col % nCols)
#             faceConnects.append(index0)
#             index1 = ((row % nRows) * nCols) + ((col+1) % nCols)
#             faceConnects.append(index1)
#             index2 = (((row+1) % nRows) * nCols) + ((col+1) % nCols)
#             faceConnects.append(index2)
#             index3 = (((row+1) % nRows) * nCols) + (col % nCols)
#             faceConnects.append(index3)
#             #print 'face vertex ID: %i, %i, %i, %i' % (index0,index1,index2,index3)

#     # an array to hold the total number of vertices that each face has
#     faceCounts = maya.OpenMaya.MIntArray()
#     for c in range(0,numFaces,1):
#         faceCounts.append(4)

#     #create mesh object using arrays above and get name of new mesh
#     meshFS = maya.OpenMaya.MFnMesh()
#     newMesh = meshFS.create(numVertices, numFaces, points, faceCounts, faceConnects, outputMesh)
#     meshFS.updateSurface()
#     nodeName = meshFS.name()
#     print 'Mesh node name is: %s' % nodeName

#     #assign new mesh to default shading group
#     maya.cmds.sets (nodeName, e=True, fe='initialShadingGroup')
#     return nodeName


# pk_makePolyPlane(width=10.0,length=10.0,subX=15,subZ=15)
