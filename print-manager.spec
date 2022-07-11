#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : print-manager
Version  : 22.04.3
Release  : 41
URL      : https://download.kde.org/stable/release-service/22.04.3/src/print-manager-22.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.3/src/print-manager-22.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.3/src/print-manager-22.04.3.tar.xz.sig
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

%description
This project aims to be a full replacement for the
current printing management of KDE.

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


%package dev
Summary: dev components for the print-manager package.
Group: Development
Requires: print-manager-lib = %{version}-%{release}
Requires: print-manager-bin = %{version}-%{release}
Requires: print-manager-data = %{version}-%{release}
Provides: print-manager-devel = %{version}-%{release}
Requires: print-manager = %{version}-%{release}

%description dev
dev components for the print-manager package.


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
%setup -q -n print-manager-22.04.3
cd %{_builddir}/print-manager-22.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657553411
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657553411
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/print-manager
cp %{_builddir}/print-manager-22.04.3/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/print-manager/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/print-manager-22.04.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/print-manager/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/print-manager-22.04.3/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/print-manager/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/print-manager-22.04.3/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/print-manager/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/print-manager-22.04.3/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/print-manager/19d98e1b6f8ef12849ea4012a052d3907f336c91
cp %{_builddir}/print-manager-22.04.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/print-manager/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/print-manager-22.04.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/print-manager/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang plasma_applet_org.kde.plasma.printmanager
%find_lang print-manager

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/configure-printer
/usr/bin/kde-add-printer
/usr/bin/kde-print-queue

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_printer_manager.desktop
/usr/share/applications/org.kde.ConfigurePrinter.desktop
/usr/share/applications/org.kde.PrintQueue.desktop
/usr/share/applications/org.kde.kde-add-printer.desktop
/usr/share/knotifications5/printmanager.notifyrc
/usr/share/metainfo/org.kde.plasma.printmanager.appdata.xml
/usr/share/metainfo/org.kde.print-manager.metainfo.xml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/PopupDialog.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/PrinterItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/printmanager.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/metadata.json

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkcupslib.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/kded/printmanager.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_printer_manager.so
/usr/lib64/qt5/qml/org/kde/plasma/printmanager/libprintmanager.so
/usr/lib64/qt5/qml/org/kde/plasma/printmanager/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/print-manager/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/print-manager/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/print-manager/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/print-manager/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/print-manager/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/print-manager/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f plasma_applet_org.kde.plasma.printmanager.lang -f print-manager.lang
%defattr(-,root,root,-)

