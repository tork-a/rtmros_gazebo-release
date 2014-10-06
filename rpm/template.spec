Name:           ros-hydro-hrpsys-gazebo-general
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS hrpsys_gazebo_general package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hrpsys_gazebo_general
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-gazebo-msgs
Requires:       ros-hydro-gazebo-plugins
Requires:       ros-hydro-gazebo-ros
Requires:       ros-hydro-hrpsys-gazebo-msgs
Requires:       ros-hydro-hrpsys-ros-bridge
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-gazebo-msgs
BuildRequires:  ros-hydro-gazebo-plugins
BuildRequires:  ros-hydro-gazebo-ros
BuildRequires:  ros-hydro-hrpsys-gazebo-msgs
BuildRequires:  ros-hydro-hrpsys-ros-bridge

%description
hrpsys_gazebo_general

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Oct 06 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.2-0
- Autogenerated by Bloom

* Fri Sep 26 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.1-0
- Autogenerated by Bloom

