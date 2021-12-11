if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin
call D:\Users\user1\anaconda3\Scripts\activate.bat
call activate autologin
E:
cd E:\code\autologin_school_network
call python autologin.py