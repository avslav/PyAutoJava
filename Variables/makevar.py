class MakeVar:
    def __init__(self, filename):
        self.filename = filename
    
    # Make String
    def makeStr(self, filename, vname, *, value: str):
            
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
    
    # Make Int
    def makeInt(self, filename, vname, *, value: int):

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

    # Make Float   
    def makeFloat(self, filename, vname, *, value: float):

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
    
    # Make Double
    def makeDouble(self, filename, vname, *, value: float):

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
    
    # Make Bool
    def makeBool(self, filename, vname, *, value: bool):

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
    
    # Create Char
    def makeChar(self, filename, vname, *, value: str):
        
        i = 0
            
        for letter in value:
            i = i+1

        if "" not in value or '' not in value:
            print("Error: Expecting char value for makeChar().")
        elif i > 1:
            print("Error: Single character expected for variable of type \"char\"")
        else:
            pass

        try: 
            if filename.endswith(".java"):
                    fullFileName = self.filename
                
            else:
                    fullFileName = filename + ".java"
                    fullFileName.strip()
                
            with open(fullFileName, "a") as jf:
                jf.write(f"\nchar {vname} = \'{value}\';\n")
                jf.close()
        
        except Exception as e:
            print(e)
    
    
