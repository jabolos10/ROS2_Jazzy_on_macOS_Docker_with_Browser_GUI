#!/bin/bash
Xvfb :1 -screen 0 1600x900x24 &
sleep 1
fluxbox &
x11vnc -display :1 -nopw -forever -shared -bg -quiet
websockify --web /usr/share/novnc 6080 localhost:5900 &
echo "Desktop ready: http://localhost:6080/vnc.html"
exec bash