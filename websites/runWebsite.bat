@echo off
echo Starting local server...

REM Start Python HTTP server on port 3000
start python -m http.server 3000

REM Wait a moment for the server to start
timeout /t 2 >nul

REM Open home.html through the server (NOT file://)
start http://localhost:3000/home.html
