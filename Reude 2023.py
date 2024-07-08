# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:19:05 2024

@author: cdepaor
"""

import math
#%%
#constants#
##environment##
gravityEarth = 9.8 #[m/s^2]
specificImpulse = 310 #[s]
structureRatio = 0.15 #[-]
##modules##
commandModule = 3190 #[kg]
lunarModule = 2445 #[kg]
descentStage = 1530 #[kg]
##deltaV##
EarthtoLEO = 9300 #[m/s]
LEOtoMO = 4000 #[m/s]
LEOtoMoon = 5900 #[m/s]
MOtoMoon = 1900 #[m/s]
MoontoMO = 1900 #[m/s]
MOtoLEO = 4000 #[m/s]
MoontoLEO = 5900 #[m/s]
LEOtoEarth = 0 #[m/s]
##mission elements##
DepartureEarth = 1-0.0022 #Booster_Crew
DepartureMoon = 1-0.0005 #Lunar_Ascent
AssemblyEarth = 1-0.0040 #LEO_Dock
AssemblyMoon = 1-0.0026 #Lunar_Ascent_Docking
SeparationEarth = 1-0.0000 #Lunar_Orbit_Maneuvers
SeparationMoon = 1-0.0000 #Lunar_Orbit_Maneuvers
ArrivalOrbit = 1-0.0004 #EDLS
ArrivalEarth = 1-0.0004 #EDLS
ArrivalMoon = 1-(0.0010*0.0100) #Lunar_Landing*Lunar_Descent
CoastMoon = 1-0.0100 #CEV_System_to Moon
CoastEarth = 1-0.0058 #CEV_Return
CaptureMoon = 1-0.0011 #Lunar_Capture_Crew
BoostMoon = 1-0.0025 #Lunar_Departure

BoostEarth = 1-0.0017 #EDS_Cargo
SeparationStage = 0.9975
#candidates#
direct = [DepartureEarth, SeparationStage,
          ArrivalOrbit, BoostEarth, SeparationStage,
          CoastMoon, ArrivalMoon, DepartureMoon,
SeparationStage, BoostMoon, CoastEarth,
SeparationStage, CoastEarth, ArrivalEarth]

Lor = [DepartureEarth, SeparationStage,
ArrivalOrbit, BoostEarth, SeparationStage,
CoastMoon, ArrivalOrbit, SeparationMoon,
ArrivalMoon, DepartureMoon, AssemblyMoon,
BoostMoon, CoastEarth, SeparationStage,
CoastEarth, ArrivalEarth]

Eor = [DepartureEarth, SeparationStage,
ArrivalOrbit, DepartureEarth,
SeparationStage, ArrivalOrbit, AssemblyEarth, BoostEarth, SeparationStage, CoastMoon,
ArrivalMoon, DepartureMoon, SeparationStage,
BoostMoon, CoastEarth, SeparationStage,
CoastEarth, ArrivalEarth]

LorAndEor = [DepartureEarth, SeparationStage,
ArrivalOrbit, DepartureEarth,
SeparationStage, ArrivalOrbit, AssemblyEarth, BoostEarth, SeparationStage, CoastMoon,
ArrivalOrbit, SeparationMoon, ArrivalMoon,
DepartureMoon, SeparationStage, BoostMoon,
CoastEarth, SeparationStage, CoastEarth,
ArrivalEarth]
#functions#
##mission success probability##
def successProbability(candidate): #[-]
    r = 1
    for i in candidate: 
        r = r*i
        r = int(round(r*10000))/10000
    return r
##initial mass to low earth orbit##
def tsiolkovsky(massFinal, deltaV): #[kg]
    massInitial = int(massFinal*((math.exp(deltaV/(
    gravityEarth*specificImpulse)))))
    return massInitial
#calculations#
##direct##
directSuccessProbability = successProbability(direct)
flow1 = commandModule
flow1 = tsiolkovsky(flow1, LEOtoMoon)
flow1 += descentStage
flow1 = tsiolkovsky(flow1, MoontoLEO)
##LOR##
LorSuccessProbability = successProbability(Lor)
flow3 = commandModule
print(flow3)
flow3 = tsiolkovsky(flow3, MOtoLEO)
print(flow3)
flow4 = lunarModule
print(flow4)
flow4 = tsiolkovsky(flow4, MoontoMO)
print(flow4)
flow4 += descentStage
print(flow4)
flow4 = tsiolkovsky(flow4, MOtoMoon)
print(flow4)
flow3 += flow4
print(flow3)
flow3 = tsiolkovsky(flow3, LEOtoMO)
print(flow3)
##EOR##
EorSuccessProbability = successProbability(Eor)
flow2 = commandModule
flow2 = tsiolkovsky(flow2, MoontoLEO)
flow2 += descentStage
flow2 = tsiolkovsky(flow2, LEOtoMoon)
##EOR+LOR##
EorAndLorSuccessProbability = successProbability(LorAndEor)
flow5 = commandModule
flow5 = tsiolkovsky(flow5, MOtoLEO)
flow6 = lunarModule
flow6 = tsiolkovsky(flow6, MoontoMO)
flow6 += descentStage
flow6 = tsiolkovsky(flow6, MOtoMoon)
flow5 += flow6
flow5 = tsiolkovsky(flow5, LEOtoMO)
#print#
print("direct:R(total)="+str(directSuccessProbability)+",ImLEO="+str(flow1)+"kg")
print("EOR:R(total)="+str(LorSuccessProbability)+",ImLEO="+str(flow2)+"kg")
print("LOR:R(total)="+str(EorSuccessProbability)+",ImLEO="+str(flow3)+"kg")
print("EOR+LOR:R(total)="+str(EorAndLorSuccessProbability)+",ImLEO="+str(flow5)+"kg")
#Listing 2: Terminal Results
# R(total) = 0.9614, ImLEO = 165779 kg
# R(total) = 0.9609, ImLEO = 165779 kg
# R(total) = 0.9526, ImLEO = 86930 kg
# R(total) = 0.9523, ImLEO = 86930 kg
