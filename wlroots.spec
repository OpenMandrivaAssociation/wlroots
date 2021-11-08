%define major 10
%define libname %mklibname wlroots %{major}
%define devname %mklibname -d wlroots
%define snapshot 20211107

Name:		wlroots
Version:	0.15.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	A modular Wayland compositor library
License:	MIT
URL:		https://gitlab.freedesktop.org/wlroots/wlroots/
Source0:	https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/master/wlroots-master.tar.bz2

BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xwayland)
BuildRequires:	pkgconfig(libseat)
BuildRequires:	meson
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(freerdp2)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
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
BuildRequires:  glslang-devel

%description
%{summary}.

%package -n %{libname}
Summary:	Library files for %{name}

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
%autosetup -p1 %{?snapshot:-n %{name}-master}

%build
%meson -Dlogind-provider=systemd -Dxcb-errors=disabled -Dexamples=false
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
