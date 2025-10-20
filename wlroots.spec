%define major 19
%define libname %mklibname wlroots
%define oldlibname %mklibname wlroots 12
%define devname %mklibname -d wlroots
#define snapshot 20211107

Name:		wlroots
Version:	0.19.1
Release:	2
Summary:	A modular Wayland compositor library
License:	MIT
URL:		https://gitlab.freedesktop.org/wlroots/wlroots/
Source0:	https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/%{version}/wlroots-%{version}.tar.bz2

BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libpng)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xwayland)
BuildRequires:	pkgconfig(libseat)
BuildRequires:	meson
BuildRequires:	hwdata
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(freerdp2)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xcb-errors)
BuildRequires:	pkgconfig(libglvnd)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  glslang

%description
%{summary}.

%package -n %{libname}
Summary:	Library files for %{name}
%rename %{oldlibname}

%description -n %{libname}
A modular Wayland compositor library.

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(libinput)
Requires:	pkgconfig(xcb)
Requires:	pkgconfig(xkbcommon)
Requires:	pkgconfig(pixman-1)
Requires:	pkgconfig(wayland-protocols)
Requires:	pkgconfig(xcb-icccm)

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -n wlroots-%{version} -p1

%build
%meson  \
        -Dxcb-errors=enabled \
        -Dexamples=false
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libwlroots-0.%{major}.so

%files -n %{devname}
%{_includedir}/wlroots-0.%{major}/wlr/
%{_libdir}/pkgconfig/wlroots-0.%{major}.pc
