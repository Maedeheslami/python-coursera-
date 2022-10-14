Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> largest = None
... smallest = None
... 
... while True:
...     
...     val = input("Enter a number: ")
...     
...     if val == "done":
...         break
...         
...     try:
...         val = int(val)
...         
...         if largest is None or val > largest:
...             largest = val
...         elif smallest is None or smallest > val:
...             smallest = val
...             
...     except:
...         
...         print("Invalid input")
...         continue
...         
... print("Maximum is", largest)
... print("Minimum is", smallest)
SyntaxError: multiple statements found while compiling a single statement
