# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.1.0
# 15:33:48  May 24, 2020
# ----------------------------------------------
import ScriptEnv
import math
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project8")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
selected_faces = oEditor.GetSelections()

for face_name in selected_faces:
    face_id = int(face_name[4:])
    vids = oEditor.GetVertexIDsFromFace(face_id)
    locations = []
    for v in vids:
        locations.append([float(i) for i in oEditor.GetVertexPosition(v)])

    pt0, pt1, pt2 = locations[0:3]

    u = [j-i for i,j in zip(pt1, pt0)]
    v = [j-i for i,j in zip(pt2, pt1)]
    s1 = u[1]*v[2] - u[2]*v[1]
    s2 = u[2]*v[0] - u[0]*v[2]
    s3 = u[0]*v[1] - u[1]*v[0]
    x = math.sqrt(s1*s1 + s2*s2 + s3*s3)
    s = [s1/x, s2/x, s3/x]
    AddWarningMessage(str(s))
