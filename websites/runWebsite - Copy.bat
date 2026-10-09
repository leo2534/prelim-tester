@echo off
echo Starting local server...

REM Open home.html through the server (NOT file://)
start http://localhost:3000/home.html

REM Start Python HTTP server on port 3000
"C:/Users/PughL14/OneDrive - Hutchesons' Grammar School/ICT/Co-curricular programming/visual studio/python/python.exe" -m http.server 3000

REM Wait a moment for the server to start
timeout /t 2 >nul

