# Imports may vary depending on your directory structure
import src.init
from src.init import javaInit
import Variables.makevar 
from Variables.makevar import MakeVar
from init import javaInit

# Declare a variable for your file name
myfile = "example_output"

# Create an instance of the initJava class to get started
f = javaInit(myfile)

# Create and Initialize the Java file, and create a main function 
f.initJava(myfile, create_main=True)

# Create an instance of MakeVar class to declare Java variables, and pass in the file name
j = MakeVar(myfile)

# Declaring variables
j.makeStr(myfile, "testStr", value="this is a string")
j.makeInt(myfile, "testInt", value=60)
j.makeBool(myfile, "testBool", value=True)
j.makeFloat(myfile, "testFloat", value=2.0)
j.makeDouble(myfile, "testDouble", value=6.5)
j.makeChar(myfile, "testChar", value="A")

# Closing your Java files, and the main function
f.closeJava(myfile, close_main=True)

### HEAD TO EXAMPLE_OUTPUT.JAVA TO SEE THE EXACT OUTPUT GENERATED BY THIS SCRIPT ###
