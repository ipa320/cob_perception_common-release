Name:           ros-indigo-cob-object-detection-visualizer
Version:        0.6.6
Release:        0%{?dist}
Summary:        ROS cob_object_detection_visualizer package

Group:          Development/Libraries
License:        LGPL
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-object-detection-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-cob-object-detection-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-visualization-msgs

%description
The cob_object_detection_visualizer package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jun 17 2015 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.6-0
- Autogenerated by Bloom

* Wed Jun 17 2015 rbormann <richard.bormann@ipa.fraunhofer.de> - 0.6.5-0
- Autogenerated by Bloom

