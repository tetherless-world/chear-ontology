This python code uses the Beautiful Soup package to extract codebook values and Semantic Data Dictionary (SDD) starting points from NHANES documents.

To specify which year's variables to extract from, set the starting year on the begin_year variable. As 2013-2014 data is the most up to date and complete at the time of this writing, begin_year has been set to 2013.

The *Val variables are used to store the SDD column values.

columnVal stores the name of the NHANES variable, which is required.
labelVal stores the label associated with the NHANES variable, extracted from "SAS Label"
commentVal stores the comment associated with the NHANES variable, extracted from "English Text"
noteVal stores a note associated with the NHANES variable, extracted from "English Instructions"
targetVal stores the target of the variable, extracted from "Target" . This column is not in the SDD specification, but is included in the extraction for completeness.
attributeVal stores the attribute associated with the variable, using text matching.
attributeOfVal is used to assign a role.
unitVal is used to assign a unit to the variable as extracted from the label or comment.

The following variable are placeholders for future code that can be written to assign values to their associated columns.
timeVal
entityVal 
roleVal
relationVal
inRelationToVal
wasDerivedFromVal
wasGeneratedByVal
hasPositionVal
