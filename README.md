# CSV-TXT-to-XML-converter-Factory-pattern-
The created program will be used by users to transform csv or txt tab delimited or “,” delimited to either a tab separated csv or an xml with a customized output.

The pattern basically works as shown in this uml diagram:

![Capture](https://user-images.githubusercontent.com/72697259/190620102-c9c22ede-64a3-4947-b8ce-2fb00b6ce50f.PNG)

The classes in this case are:
FILE : defines the interface for objects that will be created by the factory method.
XML_converter : Implements the FILE interface.
CSV_converter : Implements the FILE interface.
FileFactory: Creates the objects.
Exectue_file : returns a FILE object, created either and XML_converter or a CSV_converter object by creating a FileFactory object. May be called the main() of our program.

Program Interface: 

![Capture](https://user-images.githubusercontent.com/72697259/190620921-4a8c41dc-a40e-4828-9c3f-d0e3b3c6c94f.PNG)
