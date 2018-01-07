Name:           ros-kinetic-cob-object-detection-visualizer
Version:        0.6.11
Release:        0%{?dist}
Summary:        ROS cob_object_detection_visualizer package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       opencv-devel
Requires:       pcl-devel
Requires:       ros-kinetic-cob-object-detection-msgs
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-eigen-conversions
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-pcl-ros
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  boost-devel
BuildRequires:  opencv-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cob-object-detection-msgs
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-eigen-conversions
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-pcl-ros
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-visualization-msgs

%description
The cob_object_detection_visualizer package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Jan 07 2018 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.11-0
- Autogenerated by Bloom

* Thu Jul 20 2017 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.10-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.9-0
- Autogenerated by Bloom

