#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : print-manager
Version  : 6.0.2
Release  : 66
URL      : https://download.kde.org/stable/plasma/6.0.2/print-manager-6.0.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.2/print-manager-6.0.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.2/print-manager-6.0.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: print-manager-bin = %{version}-%{release}
Requires: print-manager-data = %{version}-%{release}
Requires: print-manager-lib = %{version}-%{release}
Requires: print-manager-license = %{version}-%{release}
Requires: print-manager-locales = %{version}-%{release}
Requires: cups
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cups-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kirigami-dev
BuildRequires : knotifications-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Print Manager
Print Manager is a small, relatively self-contained set of components integrated with Plasma System Settings for managing CUPS printer configurations.

%package bin
Summary: bin components for the print-manager package.
Group: Binaries
Requires: print-manager-data = %{version}-%{release}
Requires: print-manager-license = %{version}-%{release}

%description bin
bin components for the print-manager package.


%package data
Summary: data components for the print-manager package.
Group: Data

%description data
data components for the print-manager package.


%package lib
Summary: lib components for the print-manager package.
Group: Libraries
Requires: print-manager-data = %{version}-%{release}
Requires: print-manager-license = %{version}-%{release}

%description lib
lib components for the print-manager package.


%package license
Summary: license components for the print-manager package.
Group: Default

%description license
license components for the print-manager package.


%package locales
Summary: locales components for the print-manager package.
Group: Default

%description locales
locales components for the print-manager package.


%prep
%setup -q -n print-manager-6.0.2
cd %{_builddir}/print-manager-6.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711158351
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711158351
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/print-manager
cp %{_builddir}/print-manager-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/print-manager/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/print-manager-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/print-manager/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/print-manager-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/print-manager/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/print-manager-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/print-manager/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/print-manager-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/print-manager/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/print-manager-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/print-manager/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/print-manager-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/print-manager/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang plasma_applet_org.kde.plasma.printmanager
%find_lang print-manager
%find_lang kcm_printer_manager
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/configure-printer
/V3/usr/bin/kde-add-printer
/V3/usr/bin/kde-print-queue
/usr/bin/configure-printer
/usr/bin/kde-add-printer
/usr/bin/kde-print-queue

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_printer_manager.desktop
/usr/share/applications/org.kde.ConfigurePrinter.desktop
/usr/share/applications/org.kde.PrintQueue.desktop
/usr/share/applications/org.kde.kde-add-printer.desktop
/usr/share/knotifications6/printmanager.notifyrc
/usr/share/metainfo/org.kde.plasma.printmanager.appdata.xml
/usr/share/metainfo/org.kde.print-manager.metainfo.xml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/FullRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/PrinterDelegate.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/metadata.json
/usr/share/qlogging-categories6/pmlogs.categories

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkcupslib.so.6.0.2
/V3/usr/lib64/qt6/plugins/kf6/kded/printmanager.so
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_printer_manager.so
/V3/usr/lib64/qt6/qml/org/kde/plasma/printmanager/libkcupslibplugin.so
/usr/lib64/libkcupslib.so.6.0.2
/usr/lib64/qt6/plugins/kf6/kded/printmanager.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_printer_manager.so
/usr/lib64/qt6/qml/org/kde/plasma/printmanager/kcupslib.qmltypes
/usr/lib64/qt6/qml/org/kde/plasma/printmanager/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/plasma/printmanager/libkcupslibplugin.so
/usr/lib64/qt6/qml/org/kde/plasma/printmanager/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/print-manager/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/print-manager/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/print-manager/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/print-manager/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/print-manager/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/print-manager/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f plasma_applet_org.kde.plasma.printmanager.lang -f print-manager.lang -f kcm_printer_manager.lang
%defattr(-,root,root,-)

