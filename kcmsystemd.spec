Summary:	Systemd control module for KDE
Name:		kcmsystemd
Version:	1.1.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		https://github.com/rthomsen/kcmsystemd
Source0:	https://github.com/rthomsen/kcmsystemd/archive/refs/tags/%{version}.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)

%description
Systemd control module for KDE.
- Provides a graphical frontend for modifying the systemd
  configuration files: system.conf, journald.conf and login.conf.
- Integrates in the KDE System Settings.
- The module looks for the files in /etc/systemd and /usr/etc/systemd.

%files -f %{name}.lang
%doc LICENSE NEWS README.md
%{_datadir}/dbus-1/system-services/*
%{_datadir}/dbus-1/system.d/*
%{_datadir}/polkit-1/actions/*
%{_datadir}/kservices5/*.desktop
%{_libdir}/qt5/plugins/kcm_systemd.so
%{_libdir}/libexec/kauth/kcmsystemdhelper

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}
