import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.GetActiveEditor()


oModule = oDesign.GetModule("OutputVariable")
val1=oModule.GetOutputVariableValue("Im(Y(Port1,Port2))", "Freq=['All']", "LinearFrequency", "Standard",
    [
        "NAME:Context",
        "SimValueContext:="    , [3,0,2,0,False,False,-1,1,0,1,1,"",0,0]
    ])
AddWarningMessage(str(val1))
