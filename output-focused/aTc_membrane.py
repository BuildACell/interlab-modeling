##### Creating a membrane model for aTc transport####

from subsbml import *

MB = createNewSubsystem()

model = MB.createNewModel('aTc_membrane','second','mole','substance')
simpleModel = SimpleModel(model)
per_second = simpleModel.createNewUnitDefinition('per_second',libsbml.UNIT_KIND_SECOND,-1,0,1)
substance = simpleModel.createNewUnitDefinition('substance',libsbml.UNIT_KIND_DIMENSIONLESS, 1, 0, 1)

simpleModel.createNewCompartment('internal','internal',1,'litre',True)
simpleModel.createNewCompartment('external','external',1,'litre',True)


simpleModel.createNewSpecies( 'aTc','external',0,False,'substance')
simpleModel.createNewSpecies( 'aTc','internal',0,False,'substance')
simpleModel.createNewSpecies( 'complexL*','internal',0,False,'substance')
simpleModel.createNewSpecies( 'aTc:complexL*','internal',0,False,'substance')

simpleModel.createNewParameter( 'kb',2,False,'per_second')
simpleModel.createNewParameter( 'kd',1,False,'per_second')

r1 = SimpleReaction(model.createReaction())
r1.setId('r1')
r1.setReversible(True)
r1.createNewReactant('aTc',False,1)
r1.createNewReactant('xxcomplexL', False, 1)
r1.createNewProduct('xxaTc_complexL', False, 1)
math_r1 = r1.createMath('kb * aTc * xxcomplexL - kd * xxaTc_complexL')
r1.createRate(math_r1)

r2 = SimpleReaction(model.createReaction())
r2.setId('r2')
r2.setReversible(True)
r2.createNewReactant('xxaTc_complexL',False,1)
r2.createNewProduct('aTc_1',False,1)
r2.createNewProduct('xxcomplexL',False,1)
math_r2 = r2.createMath('kd * xxaTc_complexL - kb * aTc_1 * xxcomplexL')
r2.createRate(math_r2)



# Write to XML file 
libsbml.writeSBML(MB.getSBMLDocument(),'models/aTc_membrane.xml')
