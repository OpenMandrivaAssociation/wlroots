%define major 7
%define libname %mklibname wlroots %{major}
%define devname %mklibname -d wlroots

Name:		wlroots
Version:	0.12.0
Release:	2
Summary:	A modular Wayland compositor library
License:	MIT
URL:		https://github.com/swaywm/%{name}
Source0:	https://github.com/swaywm/wlroots/archive/%{version}.tar.gz

BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xkbcommon)
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
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb-icccm)

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
%autosetup -p1

%build
%meson -Dlogind-provider=systemd -Dlibseat=disabled -Dxcb-errors=disabled -Dexamples=false
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
