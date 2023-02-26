# P1Tool
code should be located together with excel file (pandas module handle it) (CarConfig.xlsx , attached here)

it should make gui with "open file" , "save file" in upper bar and groups of radiobuttons in main body :

each group has label of unique "Parameter name" from excel file. Each group has unique "id" and "Offset"
Each button in the group is labeled with text from "Text Data" column belongs to same group

When user hits "open file" button, script should ask for .bin file. Then check for file lenght is at least 0xEBC0B+17 . Then check if values in adresses 
0xEBC0B == 89 and 0xEBC0C == 86. Then load file to a buffer. 
Every group has own unique "id" , "offset" and "Parameter name" in excel file and coresponded buffer adress. 
Our work area starts with adress is 0EBD00 which coresponds to "offset" 0 and "id" = 331675  of excel file.
And end adress is  0EBD8D which correspons with "id" 331775 and offset" 808
Bin file example attached (1K79XFLASH.BIN)

so far doesnt work:

scrollbar

pre-selected radiobuttons: 
script should compare bin file values with column "value" in excel file in rows with "id" coresponded to every button group 
then should selsct radiobutton in each group with "text data" from a row with same "value" as in bin file adress coresponded with "id" in this row

later:

when user selects any radiobutton , script should do oposite manouver: 
save value from "value" column of row with selected "text data" to buffer adress coresponded with current group "id"

When user select "save file" button, script should prompt "Are you sure" and then save buffer to .bin file, but add something to file name (e.g. "_1)
