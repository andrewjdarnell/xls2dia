xls2dia - A tool to produce diagrams from simple excel/csv files
================================================================

The file needs a header row which describes the columns, the column headers are case insensitive.


Column Headers - must be on the top line

id      -       A short name for the item - examples include arrow4, 56, DecisionColour
shape   -       describes which type of shape or item that this is
From    -       for lines and arrows this is the source (and the beginning of the arrow)
To      -       The end item for lines and arrows (the arrow tip)

Title   -       This is the human readable short name for an item
Detail  -       This is the longer human readable description for an item - typically the text will appear in the body
Comments -      A text field that is just for the diagram designers use.

Blank lines are ignored
Columns can be in any order as long as they are identified by the Headers


Shapes supported

Box     -       A rectangular autosized box with a title, and description, has a hidden id, if title is not specified then id is used

Line    -       A line from one object to another with a name and description to identify it.
Arrow   -       Arrow is a directed line from one object to another with an arrow head at the 'to' point
BiArrow -       A bidirectional arrowhead from one object to another with a name and description
Start   -       A flowchart start symbol
End     -       A flowchart end symbol



