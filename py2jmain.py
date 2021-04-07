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

class Java:
    def __init__(self, filename):
        self.filename = filename
    def printJava(self, args):

        try: 
            if filename.endswith(".java"):
                global fullFileName
                fullFileName = self.filename
            else:
                fullFileName = filename + ".java"
                fullFileName.strip()
        
            with open(fullFileName, "a") as jf:
            
                jf.write(f"System.out.println(\"{args}\");")

            print("Added: System.out.printin({}) to your Java file!".format(args))
        
        except Exception as e:
            print(e)

    def math(self, op, *nums):
        nums = list(nums)
        ffn = fullFileName
        with open(ffn, "a") as jf:
            towrite = []
            for num, n in enumerate(nums):
                if n != len(nums):
                    towrite.append(f"{num} {op}")
                elif n == len(nums):
                    towrite.append(f"{num}")
            written = towrite.join()
            jf.write(written)
            print("Added some math to your Java!")
        



initJava("test")
j = Java("test.java")
j.printJava("hoho old chummy chum chum")
j.math("+", 99, 1)
closeJava("test")