#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : garcon
Version  : 0.6.4
Release  : 21
URL      : http://archive.xfce.org/src/xfce/garcon/0.6/garcon-0.6.4.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/garcon/0.6/garcon-0.6.4.tar.bz2
Summary  : Freedesktop.org compliant menu library
Group    : Development/Tools
License  : LGPL-2.0
Requires: garcon-data = %{version}-%{release}
Requires: garcon-lib = %{version}-%{release}
Requires: garcon-license = %{version}-%{release}
Requires: garcon-locales = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(sm)

%description
What is it?
===========
This is garcon, a freedesktop.org compliant menu implementation based
on GLib and GIO. It was started as a complete rewrite of the former
Xfce menu library called libxfce4menu, which, in contrast to garcon,
was lacking menu merging features essential for loading menus modified
with menu editors.

%package data
Summary: data components for the garcon package.
Group: Data

%description data
data components for the garcon package.


%package dev
Summary: dev components for the garcon package.
Group: Development
Requires: garcon-lib = %{version}-%{release}
Requires: garcon-data = %{version}-%{release}
Provides: garcon-devel = %{version}-%{release}
Requires: garcon = %{version}-%{release}

%description dev
dev components for the garcon package.


%package doc
Summary: doc components for the garcon package.
Group: Documentation

%description doc
doc components for the garcon package.


%package lib
Summary: lib components for the garcon package.
Group: Libraries
Requires: garcon-data = %{version}-%{release}
Requires: garcon-license = %{version}-%{release}

%description lib
lib components for the garcon package.


%package license
Summary: license components for the garcon package.
Group: Default

%description license
license components for the garcon package.


%package locales
Summary: locales components for the garcon package.
Group: Default

%description locales
locales components for the garcon package.


%prep
%setup -q -n garcon-0.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564972280
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1564972280
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/garcon
cp COPYING %{buildroot}/usr/share/package-licenses/garcon/COPYING
%make_install
%find_lang garcon
## install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/. && rmdir %{buildroot}%{_sysconfdir}
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/desktop-directories/xfce-accessories.directory
/usr/share/desktop-directories/xfce-development.directory
/usr/share/desktop-directories/xfce-education.directory
/usr/share/desktop-directories/xfce-games.directory
/usr/share/desktop-directories/xfce-graphics.directory
/usr/share/desktop-directories/xfce-hardware.directory
/usr/share/desktop-directories/xfce-multimedia.directory
/usr/share/desktop-directories/xfce-network.directory
/usr/share/desktop-directories/xfce-office.directory
/usr/share/desktop-directories/xfce-other.directory
/usr/share/desktop-directories/xfce-personal.directory
/usr/share/desktop-directories/xfce-screensavers.directory
/usr/share/desktop-directories/xfce-settings.directory
/usr/share/desktop-directories/xfce-system.directory
/usr/share/xdg/menus/xfce-applications.menu

%files dev
%defattr(-,root,root,-)
/usr/include/garcon-1/garcon/garcon-config.h
/usr/include/garcon-1/garcon/garcon-environment.h
/usr/include/garcon-1/garcon/garcon-marshal.h
/usr/include/garcon-1/garcon/garcon-menu-directory.h
/usr/include/garcon-1/garcon/garcon-menu-element.h
/usr/include/garcon-1/garcon/garcon-menu-item-action.h
/usr/include/garcon-1/garcon/garcon-menu-item-cache.h
/usr/include/garcon-1/garcon/garcon-menu-item-pool.h
/usr/include/garcon-1/garcon/garcon-menu-item.h
/usr/include/garcon-1/garcon/garcon-menu-merger.h
/usr/include/garcon-1/garcon/garcon-menu-node.h
/usr/include/garcon-1/garcon/garcon-menu-parser.h
/usr/include/garcon-1/garcon/garcon-menu-separator.h
/usr/include/garcon-1/garcon/garcon-menu-tree-provider.h
/usr/include/garcon-1/garcon/garcon-menu.h
/usr/include/garcon-1/garcon/garcon.h
/usr/include/garcon-gtk2-1/garcon-gtk/garcon-gtk-menu.h
/usr/include/garcon-gtk2-1/garcon-gtk/garcon-gtk.h
/usr/include/garcon-gtk3-1/garcon-gtk/garcon-gtk-menu.h
/usr/include/garcon-gtk3-1/garcon-gtk/garcon-gtk.h
/usr/lib64/libgarcon-1.so
/usr/lib64/libgarcon-gtk2-1.so
/usr/lib64/libgarcon-gtk3-1.so
/usr/lib64/pkgconfig/garcon-1.pc
/usr/lib64/pkgconfig/garcon-gtk2-1.pc
/usr/lib64/pkgconfig/garcon-gtk3-1.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/garcon/GarconMenu.html
/usr/share/gtk-doc/html/garcon/GarconMenuDirectory.html
/usr/share/gtk-doc/html/garcon/GarconMenuElement.html
/usr/share/gtk-doc/html/garcon/GarconMenuItem.html
/usr/share/gtk-doc/html/garcon/GarconMenuItemCache.html
/usr/share/gtk-doc/html/garcon/GarconMenuMerger.html
/usr/share/gtk-doc/html/garcon/GarconMenuParser.html
/usr/share/gtk-doc/html/garcon/GarconMenuSeparator.html
/usr/share/gtk-doc/html/garcon/GarconMenuTreeProvider.html
/usr/share/gtk-doc/html/garcon/api-index-full.html
/usr/share/gtk-doc/html/garcon/garcon-Desktop-Environment-Configuration.html
/usr/share/gtk-doc/html/garcon/garcon-GarconGtkMenu.html
/usr/share/gtk-doc/html/garcon/garcon-GarconMenuItemAction.html
/usr/share/gtk-doc/html/garcon/garcon-Version-Information.html
/usr/share/gtk-doc/html/garcon/garcon-garcon-gtk.html
/usr/share/gtk-doc/html/garcon/garcon-garcon-menu-item-pool.html
/usr/share/gtk-doc/html/garcon/garcon-garcon-menu-node.html
/usr/share/gtk-doc/html/garcon/garcon-garcon.html
/usr/share/gtk-doc/html/garcon/garcon-gtk-menu.html
/usr/share/gtk-doc/html/garcon/garcon-menus.html
/usr/share/gtk-doc/html/garcon/garcon-miscellaneous.html
/usr/share/gtk-doc/html/garcon/garcon-parsing.html
/usr/share/gtk-doc/html/garcon/garcon.devhelp2
/usr/share/gtk-doc/html/garcon/home.png
/usr/share/gtk-doc/html/garcon/index.html
/usr/share/gtk-doc/html/garcon/left-insensitive.png
/usr/share/gtk-doc/html/garcon/left.png
/usr/share/gtk-doc/html/garcon/object-tree.html
/usr/share/gtk-doc/html/garcon/pt01.html
/usr/share/gtk-doc/html/garcon/right-insensitive.png
/usr/share/gtk-doc/html/garcon/right.png
/usr/share/gtk-doc/html/garcon/style.css
/usr/share/gtk-doc/html/garcon/up-insensitive.png
/usr/share/gtk-doc/html/garcon/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgarcon-1.so.0
/usr/lib64/libgarcon-1.so.0.0.0
/usr/lib64/libgarcon-gtk2-1.so.0
/usr/lib64/libgarcon-gtk2-1.so.0.0.0
/usr/lib64/libgarcon-gtk3-1.so.0
/usr/lib64/libgarcon-gtk3-1.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/garcon/COPYING

%files locales -f garcon.lang
%defattr(-,root,root,-)

