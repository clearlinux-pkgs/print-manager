#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : print-manager
Version  : 20.08.0
Release  : 21
URL      : https://download.kde.org/stable/release-service/20.08.0/src/print-manager-20.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.0/src/print-manager-20.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.0/src/print-manager-20.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: print-manager-bin = %{version}-%{release}
Requires: print-manager-data = %{version}-%{release}
Requires: print-manager-lib = %{version}-%{release}
Requires: print-manager-license = %{version}-%{release}
Requires: print-manager-locales = %{version}-%{release}
Requires: cups
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cups
BuildRequires : cups-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : plasma-framework-dev

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
%setup -q -n print-manager-20.08.0
cd %{_builddir}/print-manager-20.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597800397
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1597800397
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/print-manager
cp %{_builddir}/print-manager-20.08.0/COPYING %{buildroot}/usr/share/package-licenses/print-manager/4cc77b90af91e615a64ae04893fdffa7939db84c
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
/usr/share/applications/org.kde.ConfigurePrinter.desktop
/usr/share/applications/org.kde.PrintQueue.desktop
/usr/share/applications/org.kde.kde-add-printer.desktop
/usr/share/knotifications5/printmanager.notifyrc
/usr/share/kservices5/kcm_printer_manager.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.printmanager.desktop
/usr/share/metainfo/org.kde.plasma.printmanager.appdata.xml
/usr/share/metainfo/org.kde.print-manager.metainfo.xml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/PopupDialog.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/PrinterItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/config.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/printmanager.qml
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.printmanager/metadata.json

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkcupslib.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_printer_manager.so
/usr/lib64/qt5/plugins/kf5/kded/printmanager.so
/usr/lib64/qt5/qml/org/kde/plasma/printmanager/libprintmanager.so
/usr/lib64/qt5/qml/org/kde/plasma/printmanager/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/print-manager/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f plasma_applet_org.kde.plasma.printmanager.lang -f print-manager.lang
%defattr(-,root,root,-)

