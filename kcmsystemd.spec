Summary:	Systemd control module for KDE
Name:		kcmsystemd
Version:	0.6.0
Release:	4
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		https://github.com/rthomsen/kcmsystemd
Source0:	https://github.com/rthomsen/kcmsystemd/archive/%{name}-%{version}.tar.gz
Patch0:		kcmsystemd-0.5.0-kdesu-path.patch
Patch1:		kcmsystemd-0.6.0-locale.patch
Patch2:		kcmsystemd-0.6.0-fix_crash.patch
BuildRequires:	boost-devel
BuildRequires:	kdebase4-devel
BuildRequires:	qt4-devel
Requires:	kdebase4-runtime

%description
Systemd control module for KDE.
- Provides a graphical frontend for modifying the systemd
  configuration files: system.conf, journald.conf and login.conf.
- Integrates in the KDE System Settings.
- The module looks for the files in /etc/systemd and /usr/etc/systemd.

%files
%doc LICENSE NEWS README.md
%{_kde_libdir}/kde4/kcm_systemd.so
%{_kde_libdir}/kde4/libexec/kcmsystemdhelper
%{_kde_services}/kcm_systemd.desktop
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsystemd.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsystemd.policy
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsystemd.conf

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake_kde4

%install
%makeinstall_std -C build

