### INIT JAVA FILE SRC CODE ###
import Variables.makevar
from Variables.makevar import MakeVar

# Init class
class javaInit:
    def __init__(self, filename):
        self.filename = filename

    def initJava(self, filename: str, *, create_main:bool=True):
        
        # Cleaning up the filename
        fullFileName = filename + ".java"
        fullFileName.strip()

        
        with open(fullFileName, "w") as jf:
            
            # Create main function if create_main bool is set to true
            if create_main:
            
                jf.write("public class {}".format(filename))
                jf.write("{")
                jf.write("\n public static void main(String[] args) {")
            
            else:
                jf.write("public class {}".format(filename))
                jf.write("{")

            jf.close()
        
        return print(f"Created and initialized file {filename}.java successfully!")

    def closeJava(self, filename: str, *, close_main: bool):


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
        
    # Print function 
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

   
