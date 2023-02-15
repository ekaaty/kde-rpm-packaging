Name:          flatpak-kcm
Version:       5.27.0
Release:       2%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later
Summary:       Flatpak Permissions Management KCM
Url:           https://invent.kde.org/plasma/flatpak-kcm

Source0:       http://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:       http://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Source2:       https://jriddell.org/esk-riddell.gpg

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Svg)
BuildRequires: pkgconfig(flatpak)

%description
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang kcm_flatpak

%files -f kcm_flatpak.lang
%doc README.md
%license LICENSES/*
%{_kf5_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/main.qml
%{_kf5_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/permissions.qml
%{_kf5_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_flatpak.so
%{_kf5_datadir}/applications/kcm_flatpak.desktop

%changelog
* Tue Feb 14 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-2
- Rebuild against new sources

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Sun Jan 22 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- Initial Package
