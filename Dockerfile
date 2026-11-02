FROM ros:jazzy

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    ros-jazzy-turtlesim \
    ros-jazzy-rqt-graph \
    ros-jazzy-teleop-twist-keyboard \
    xvfb x11vnc fluxbox novnc websockify \
    && rm -rf /var/lib/apt/lists/*

COPY start-desktop.sh /start-desktop.sh
RUN chmod +x /start-desktop.sh && \
    echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc

ENV DISPLAY=:1
EXPOSE 6080
CMD ["/start-desktop.sh"]