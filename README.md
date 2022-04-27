# SBConverter
SB conversion utilities (MV to HTML; SQL)
SB Converter	Tuesday, 26 April 2022
Started as a whim but then got seriously curious about a possibility of converting
aged SB screens to an HTML front (for the hell of it)
Idea first conceptualised circa Dec 2020 but only started doing some work on it
during redundancy period of TSC in January 2022.
We should identify that it’s NOT SB+ screens but the good old fashioned System
Builder (5.1) “green screens” – I will use SB as indicator here.
The extract code is written in D3 (10.4x) with as many modular functions as I thought
necessary.
This suite effectively writes a Python Dict which is then picked up (by Python
functions) to write HTML pages and routines to mimic a Web page.
The DB used (converted data) is MS SQL – but could be any SQL.
It was fun ??

<1> Create file (table) in D3
<2> Create screen(s) in D3

Control files are DictControl which holds values (rank) of fields from dictionary
definitions.

Python interface (HTML) will show tables available
This will then show screen available
