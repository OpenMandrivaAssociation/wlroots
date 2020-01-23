%define major	5
%define libname	%mklibname wlroots %{major}
%define devname	%mklibname -d wlroots


Name:           wlroots
Version:	0.10.0
Release:	1
Summary:        A modular Wayland compositor library
License:        MIT
URL:            https://github.com/swaywm/%{name}
Source0:	https://github.com/swaywm/wlroots/archive/%{version}.tar.gz

BuildRequires:  libcap-devel
BuildRequires:  libinput-devel
BuildRequires:  png-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  meson
BuildRequires:  pixman-devel
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(egl)
BuildRequires:  egl-devel
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(libglvnd)

BuildRequires:  wayland-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel

%description
%{summary}.

%package -n     %{libname}
Summary:        Library files for %{name}

%description -n %{libname}
A modular Wayland compositor library

%package -n     %{devname}
Summary:        Development files for %{name}

Requires:       %{libname} = %{EVRD}
Requires:       libinput-devel
Requires:       xcb-devel
Requires:       libxkbcommon-devel
Requires:       pixman-devel
Requires:       wayland-devel
Requires:       xcb-util-wm-devel

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
