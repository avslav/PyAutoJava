def initJava(filename: str, *, create_main:bool=True):
        
        fullFileName = filename + ".java"
        fullFileName.strip()

        
        with open(fullFileName, "w") as jf:

            if create_main:
            
                jf.write("public class {}".format(filename))
                jf.write("{")
                jf.write("\n public static void main(String[] args) {")
            
            else:
                jf.write("public class {}".format(filename))
                jf.write("{")

            jf.close()
        
        return print(f"Created and initialized file {filename}.java successfully!")

def closeJava(filename: str, *, close_main: bool):


    fullFileName = filename + ".java"
    fullFileName.strip()
        
    with open(fullFileName, "a") as jf:

        if close_main:
            jf.write("}")
            jf.write("}")
            print(f"Closed the superclass and the main function in file {filename}.java successfully!")
        
        else:
            jf.write("}")
            print(f"Closed the superclass in file {filename}.java successfully!")
        
        jf.close()
        
        




class Java:
    
    def __init__(self, filename):
        self.filename = filename
    
    def printJava(self, args):

        try: 
            if filename.endswith(".java"):
                fullFileName = self.filename
            else:
                fullFileName = filename + ".java"
                fullFileName.strip()
        
            with open(fullFileName, "a") as jf:
            
                jf.write(f"System.out.println(\"{args}\");")

            print("Added: System.out.printin({}) to your Java file!".format(args))
        
        except Exception as e:
            print(e)

    ##################### VARIABLE CREATION ##################################
    
    def createStr(self, filename, vname, *, value: str):
        
        if "" not in value:
            print("Error: Expecting string value for createStr().")
        else:
            pass

        try: 
            if filename.endswith(".java"):
                fullFileName = self.filename
            
            else:
                fullFileName = filename + ".java"
                fullFileName.strip()
            
            with open(fullFileName, "a") as jf:
                jf.write(f"\nString {vname} = \"{value}\";\n")
                jf.close()
       
        except Exception as e:
            print(e)

    def createInt(self, filename, vname, *, value: int):

        try: 
            if filename.endswith(".java"):
                fullFileName = self.filename
            
            else:
                fullFileName = filename + ".java"
                fullFileName.strip()
            
            with open(fullFileName, "a") as jf:
                jf.write(f"\nint {vname} = {value};\n")
                jf.close()
        
        except Exception as e:
            print(e)
    
    def createFloat(self, filename, vname, *, value: float):

        try: 
            if filename.endswith(".java"):
                fullFileName = self.filename
            
            else:
                fullFileName = filename + ".java"
                fullFileName.strip()
            
            with open(fullFileName, "a") as jf:
                jf.write(f"\nfloat {vname} = {value}f;\n")
                jf.close()
        
        except Exception as e:
            print(e)
    
    def createDouble(self, filename, vname, *, value: float):

        try: 
            if filename.endswith(".java"):
                fullFileName = self.filename
            
            else:
                fullFileName = filename + ".java"
                fullFileName.strip()
            
            with open(fullFileName, "a") as jf:
                jf.write(f"\ndouble {vname} = {value};\n")
                jf.close()
        
        except Exception as e:
            print(e)
    
    def createBool(self, filename, vname, *, value: bool):

        try: 
            if filename.endswith(".java"):
                fullFileName = self.filename
            
            else:
                fullFileName = filename + ".java"
                fullFileName.strip()
            
            with open(fullFileName, "a") as jf:
                
                if value:
                    jf.write(f"\nboolean {vname} = true;\n")
                else: 
                    jf.write(f"\nboolean {vname} = false;\n")
   
                jf.close()
        
        except Exception as e:
            print(e)

#################### Meth Creation ###########################

    
                

#################### TESTING #########################

# Init
initJava("test", create_main=True)
j = Java("test.java")

# Functions
j.printJava("hello")

# Variables
j.createStr("test", "testStr", value="this is a string")
j.createInt("test", "testInt", value=60)
j.createBool("test", "testBool", value=True)
j.createFloat("test", "testFloat", value=2.0)
j.createDouble("test", "testDouble", value=6.5)

# Close
closeJava("test", close_main=True)