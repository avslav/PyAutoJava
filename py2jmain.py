def initJava(filename: str):
    
    fullFileName = filename + ".java"
    fullFileName.strip()

    
    with open(fullFileName, "w") as jf:
        
        jf.write("public class {}".format(filename))
        jf.write("{")
        jf.write("\n public static void main(String[] args) {")
        jf.close()
    
    return print(f"Created and initialized file {filename}.java successfully!")

def closeJava(filename: str):


    fullFileName = filename + ".java"
    fullFileName.strip()
    
    with open(fullFileName, "a") as jf:
        
        jf.write("}")
        jf.write("}")
        jf.close()
    
    return print(f"Closed the necesarry brackets in file {filename}.java successfully!")


def printJava(filename: str, args):

    try: 
        fullFileName = filename + ".java"
        fullFileName.strip()
    
        with open(fullFileName, "a") as jf:
        
            jf.write(f"System.out.println(\"{args}\");")

        print("Added: System.out.printin({}) to your Java file!".format(args))
    
    except Exception as e:
        print(e)


initJava("test")
printJava("test", "test text")
closeJava("test")