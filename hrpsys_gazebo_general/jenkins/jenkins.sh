#!/bin/bash

trap 'exit 1' ERR

set -x

DISTRO=${1:-groovy}
source /opt/ros/${DISTRO}/setup.bash
#
mkdir -p catkin_ws/src
cd catkin_ws/src
catkin_init_workspace
wstool init
wstool merge https://rtm-ros-robotics.googlecode.com/svn-history/trunk/rtmros_gazebo/hrpsys_gazebo_atlas/dot.rosinstall
wstool update
find -name manifest.xml -exec  mv {} {}.bak \; ##
cd ..

#
sudo apt-get update
sudo apt-get -y install drcsim
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro ${DISTRO} -y -r
sudo apt-get install -y ros-${DISTRO}-hrpsys-ros-bridge ## this should installed as rosdep install command
catkin_make

##


