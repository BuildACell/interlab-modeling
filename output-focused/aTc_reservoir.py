##### Creating a membrane model for aTc transport####

from subsbml import *

aTc = createNewSubsystem()

model = aTc.createNewModel('aTc_reservoir','second','mole','substance')
simpleModel = SimpleModel(model)
per_second = simpleModel.createNewUnitDefinition('per_second',libsbml.UNIT_KIND_SECOND,-1,0,1)
substance = simpleModel.createNewUnitDefinition('substance',libsbml.UNIT_KIND_DIMENSIONLESS, 1, 0, 1)

simpleModel.createNewCompartment('external','external',1,'litre',True)


simpleModel.createNewSpecies( 'aTc','external',100000,False,'substance')


# Write to XML file 
libsbml.writeSBML(aTc.getSBMLDocument(),'models/aTc_reservoir.xml')
