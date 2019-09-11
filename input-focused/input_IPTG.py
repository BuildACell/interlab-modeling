##### Creating a membrane model for IPTG transport####

from subsbml import *

IPTG = createNewSubsystem()

model = IPTG.createNewModel('input_IPTG','second','mole','substance')
simpleModel = SimpleModel(model)
per_second = simpleModel.createNewUnitDefinition('per_second',libsbml.UNIT_KIND_SECOND,-1,0,1)
substance = simpleModel.createNewUnitDefinition('substance',libsbml.UNIT_KIND_DIMENSIONLESS, 1, 0, 1)

simpleModel.createNewCompartment('external','external',1,'litre',True)


simpleModel.createNewSpecies( 'IPTG','external',100000,False,'substance')


# Write to XML file 
libsbml.writeSBML(IPTG.getSBMLDocument(),'models/input_IPTG.xml')
