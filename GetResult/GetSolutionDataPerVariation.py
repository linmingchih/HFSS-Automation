# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.1.0
# 7:49:51  May 25, 2020
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()

oModule = oDesign.GetModule("ReportSetup")
arr = oModule.GetSolutionDataPerVariation("Standard", 'LinearFrequency', ['Domain:=', 'Sweep'], ['Freq:=', ['All']], ["Y(Port1,Port2)"])

AddWarningMessage(str(arr[0].GetImagDataValues("Y(Port1,Port2)")))
