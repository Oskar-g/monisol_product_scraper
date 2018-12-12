@echo off

echo "###################################################################"
echo "###      ___  __             __                                 ###"
echo "###    /___\/ _\  /\ /\    / _\ ___ _ __ __ _ _ __   ___ _ __   ###"
echo "###   //  //\ \  / //_/____\ \ / __| '__/ _` | '_ \ / _ \ '__|  ###"
echo "###  / \_// _\ \/ __ \_____|\ \ (__| | | (_| | |_) |  __/ |     ###"
echo "###  \___/  \__/\/  \/     \__/\___|_|  \__,_| .__/ \___|_|     ###"
echo "###                                          |_|                ###"  
echo "###                                                             ###"
echo "###                             contact: oscarg@programmer.net  ###"
echo "###################################################################"

echo.
echo instalando librerias
echo.
pip install lxml
pip install beautifulsoup4
pip install XlsxWriter
echo.
python main.py
echo.
echo Scrapeo finalizado
pause