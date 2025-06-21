@echo off
setlocal enabledelayedexpansion

echo Baixando FFmpeg...

set "URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
set "ZIP=ffmpeg.zip"
curl -L -o %ZIP% %URL%

mkdir ffmpeg
tar -xf %ZIP% -C ffmpeg --strip-components=1

del %ZIP%

set "FFMPEG_PATH=%cd%\ffmpeg\bin"
echo Adicionando FFmpeg ao PATH do sistema (usuário)...
setx PATH "%PATH%;%FFMPEG_PATH%"

echo.
echo ✅ FFmpeg instalado com sucesso!
echo.
ffmpeg -version

pause