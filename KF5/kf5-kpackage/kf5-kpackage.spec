%undefine __cmake_in_source_build
%global framework kpackage

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:           kf5-%{framework}
Version: 5.81.0
Release: 1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 library to load and install packages as plugins

License:        LGPLv2+
URL:            https://cgit.kde.org/%{framework}.git

%global majmin %(echo %{version} | cut -d. -f1,2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
# optional
BuildRequires:  kf5-kdoctools-devel >= %{majmin}

BuildRequires:  qt5-qtbase-devel

%description
KDE Frameworks 5 Tier 2 library to load and install non-binary packages as
if they were plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       extra-cmake-modules >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-man

# create/own dirs
mkdir -p %{buildroot}%{_kf5_qtplugindir}/kpackage/packagestructure/
mkdir -p %{buildroot}%{_kf5_datadir}/kpackage/


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5Package.so.*
%{_kf5_qtplugindir}/kpackage/
%{_kf5_datadir}/kpackage/
%{_kf5_datadir}/kservicetypes5/kpackage-*.desktop
%{_kf5_bindir}/kpackagetool5
%{_mandir}/man1/kpackagetool5.1*
%{_kf5_datadir}/qlogging-categories5/kpackage.categories
%{_kf5_datadir}/qlogging-categories5/kpackage.renamecategories

%files devel
%{_kf5_includedir}/kpackage_version.h
%{_kf5_includedir}/KPackage/
%{_kf5_libdir}/libKF5Package.so
%{_kf5_libdir}/cmake/KF5Package/


%changelog
* Sun Apr 11 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.81.0-1
- 5.81.0

* Sat Mar 13 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.80.0-1
- 5.80.0

* Sat Feb 13 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.79.0-1
- 5.79.0

* Sat Jan  9 16:30:27 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.78.0-1
- 5.78.0

* Mon Dec 14 16:50:20 MSK 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.77.0-1
- 5.77.0

* Sun Nov 15 22:13:49 MSK 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.76.0-1
- 5.76.0

* Sat Oct 10 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.75.0-1
- 5.75.0

* Thu Sep 17 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.74.0-1
- 5.74.0

* Mon Aug 10 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.73.0-1
- 5.73.0

* Mon Jul 13 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.72.0-1
- 5.72.0

* Sun Jun 14 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.71.0-1
- 5.71.0

* Sun May 10 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.70.0-1
- 5.70.0

* Sat Apr 11 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.69.0-1
- 5.69.0

* Mon Mar 16 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.68.0-1
- 5.68.0

* Thu Feb 27 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.67.0-2
- rebuild

* Sun Feb 09 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.67.0-1
- 5.67.0

* Sat Jan 11 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.66.0-1
- 5.66.0

* Sat Dec 14 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.65.0-1
- 5.65.0

* Mon Nov 11 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.64.0-1
- 5.64.0

* Sun Oct 13 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.63.0-1
- 5.63.0

* Sun Sep 15 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.62.0-1
- 5.62.0

* Mon Aug 12 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.61.0-1
- 5.61.0

* Sat Jul 13 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.60.0-1
- 5.60.0

* Sat Jun 08 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.59.0-1
- 5.59.0

* Tue May 14 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.58.0-1
- 5.58.0

* Sat Apr 27 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.57.0-1
- 5.57.0

* Mon Feb 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.55.0-1
- 5.55.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.54.0-1
- 5.54.0

* Sun Dec 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.53.0-1
- 5.53.0

* Wed Nov 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.52.0-2
- respin

* Sun Nov 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.52.0-1
- 5.52.0

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.51.0-1
- 5.51.0

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.50.0-1
- 5.50.0

* Tue Aug 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.49.0-1
- 5.49.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.48.0-1
- 5.48.0

* Thu Jun 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.47.0-2
- cleanup, use %%majmin %%make_build %%ldconfig_scriptlets

* Sat Jun 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.47.0-1
- 5.47.0

* Sat May 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.46.0-1
- 5.46.0

* Sun Apr 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.45.0-1
- 5.45.0

* Sat Mar 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.44.0-1
- 5.44.0

* Wed Feb 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.43.0-1
- 5.43.0

* Mon Jan 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.0-1
- 5.42.0

* Mon Dec 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.41.0-1
- 5.41.0

* Wed Nov 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-2
- -devel: Requires: +ECM,-KCoreAddons
- drop kf5-filesystem dep (only needed in Tier 1 frameworks)

* Fri Nov 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-1
- 5.40.0

* Sun Oct 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.39.0-1
- 5.39.0

* Mon Sep 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-1
- 5.38.0

* Fri Aug 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.37.0-1
- 5.37.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.36.0-1
- 5.36.0

* Sun Jun 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.35.0-1
- 5.35.0

* Mon May 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.34.0-1
- 5.34.0

* Wed Apr 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.33.0-2
- pull in upstream fix

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.33.0-1
- 5.33.0

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.32.0-1
- 5.32.0

* Mon Feb 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.31.0-1
- 5.31.0

* Sun Dec 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.29.1-3
- fix kf5-filesystem runtime versioned dep

* Sun Dec 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.29.1-2
- fix -devel versioned deps

* Fri Dec 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.29.1-1
- 5.29.1

* Tue Oct 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Wed Sep 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.26.0-1
- KDE Frameworks 5.26.0

* Thu Aug 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.25.0-3
- %%check: drop extraneous X/dbus deps

* Thu Aug 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.25.0-2
- patch to give details about kpackagetool5 --appstream-metainfo calls

* Mon Aug 08 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.25.0-1
- KDE Frameworks 5.25.0

* Wed Jul 06 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.24.0-1
- KDE Frameworks 5.24.0

* Tue Jun 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.23.0-1
- KDE Frameworks 5.23.0

* Mon May 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.22.0-1
- KDE Frameworks 5.22.0

* Sat Apr 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-2
- update URL
- own %%_kf5_datadir/kpackage/
- support bootstrap, add %%check

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-1
- KDE Frameworks 5.21.0

* Mon Mar 14 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.20.0-1
- KDE Frameworks 5.20.0

* Thu Feb 11 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.19.0-1
- KDE Frameworks 5.19.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Rex Dieter <rdieter@fedoraproject.org> 5.18.0-2
- cosmetics, update URL, use %%license

* Sun Jan 03 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.18.0-1
- KDE Frameworks 5.18.0

* Tue Dec 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.17.0-1
- KDE Frameworks 5.17.0

* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.16.0-1
- KDE Frameworks 5.16.0

* Thu Oct 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.15.0-1
- KDE Frameworks 5.15.0

* Wed Sep 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.14.0-1
- KDE Frameworks 5.14.0

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Tue Aug 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-0.1
- KDE Frameworks 5.13

* Fri Jul 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.12.0-1
- 5.12.0

* Thu Jul 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.11.0-3
- own %%{_kf5_qtplugindir}/kpackage/{packagestructure/}
- .spec cosmetics

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Daniel Vrátil <dvratil@redhat.com> - 5.11.0-1
- KDE Frameworks 5.11.0

* Mon May 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.10.0-1
- KDE Frameworks 5.10.0

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.9.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Apr 07 2015 Daniel Vrátil <dvratil@redhat.com> - 5.9.0-1
- KDE Frameworks 5.9.0

* Mon Mar 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.8.0-1
- KDE Frameworks 5.8.0

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-2
- Rebuild (GCC 5)

* Mon Feb 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-1
- KDE Frameworks 5.7.0

* Tue Jan 06 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-1
- KDE Frameworks 5.6.0
