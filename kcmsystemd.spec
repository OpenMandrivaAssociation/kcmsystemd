%define	debug_package	%nil

Name:		kcmsystemd
Version:	0.1.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/KDE
Summary:	https://github.com/rthomsen/kcmsystemd
Source0:	https://github.com/rthomsen/kcmsystemd/archive/%{name}-%{version}.tar.gz
BuildRequires:	kdebase4-devel
BuildRequires:	qt4-devel
BuildRequires:	boost-devel

%description
Systemd control module for KDE.
Provides a graphical frontend for modifying the systemd
configuration files: system.conf, journald.conf and login.conf.
Integrates in the System Settings dialogue.
The module looks for the files in /etc/systemd and /usr/etc/systemd.

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build 

%files
%{_kde_libdir}/kde4/kcm_systemd.so
%{_libdir}/kde4/libexec/kcmsystemdhelper
%{_datadir}/kde4/services/kcm_systemd.desktop
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsystemd.policy
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsystemd.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsystemd.service
