%define		kdeappsver	19.04.0
%define		qtver		5.9.0
%define		kaname		kdenlive
Summary:	KDE movie editor
Summary(pl.UTF-8):	Edytor filmów dla KDE
Name:		kdenlive
Version:	19.04.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1386b04b1aef5832ae21525aaf4fc8b7
Patch0:		c11.patch
Patch1:		qt-5.15.patch
URL:		http://kdenlive.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake
BuildRequires:	gettext-tools
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kfilemetadata-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kplotting-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-purpose-devel
BuildRequires:	kf5-sonnet-devel
BuildRequires:	libv4l-devel
BuildRequires:	mlt-devel >= 6.12.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qjson-devel >= 0.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	rttr-devel
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel
Requires:	Qt5Gui-platform-xcb-egl
Requires:	Qt5Gui-platform-xcb-glx
Requires:	Qt5Quick-controls
Suggests:	dvdauthor
Suggests:	dvgrab
Suggests:	ffmpeg-ffplay
Suggests:	frei0r-plugins
Suggests:	mlt >= 6.0.0
Suggests:	recordmydesktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kdenlive is a non-linear video editor for KDE. It provides all project
management and editing tools while relying on a separate rendering
program (currently PIAVE) to perform the editing operations. Support
is planned for transitions, effects, multiple file formats, and full
project and asset management support. The current beta is capable of
editing raw DV or AVI DV files, with tools such as move, razor, and
resize, selecting parts of clips using in/outpoints, and exporting the
result to another raw DV file. You may playback/preview the contents
of the timeline at any point during the edit. Full project save/load
is supported.

%description -l pl.UTF-8
Kdenlive to nieliniowy edytor filmów dla KDE. Dostarcza narzędzia do
zarządzania projektem i edycji polegające na oddzielnym programie
renderującym (aktualnie PIAVE) do wykonywania operacji edycji.
Planowana jest obsługa przejść, efektów, wielu formatów plików oraz
pełnego zarządzania projektem i kapitałem. Aktualna wersja beta może
modyfikować pliki w formacie surowego DV oraz AVI DV przy użyciu
narzędzi takich jak przemieszczanie, cięcia, zmiana rozmiaru,
wybieranie części klatek przy użyciu punktów wejściowych/wyjściowych
oraz eksportowanie wyniku do innego pliku w formacie surowego DV.
Można odtwarzać/podglądać zawartość w dowolnej chwili edycji.
Obsługiwany jest zapis/odczyt pełnego projektu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mkdir -p build
cd build
%cmake .. \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DPLUGIN_INSTALL_DIR=%{_libdir}/qt5/plugins

%ninja_build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}*
%attr(755,root,root) %{_libdir}/qt5/plugins/mltpreview.so
%{_datadir}/metainfo/org.kde.kdenlive.appdata.xml
%{_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_datadir}/knotifications5/kdenlive.notifyrc
%{_datadir}/kservices5/mltpreview.desktop
%dir %{_datadir}/kxmlgui5/kdenlive
%{_datadir}/kxmlgui5/kdenlive/kdenliveui.rc
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}
%{_desktopdir}/org.kde.kdenlive.desktop
%{_docdir}/HTML/en/kdenlive
/etc/xdg/%{name}*.knsrc
/etc/xdg/kdenlive.categories
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svg
%{_iconsdir}/*/*/*/*.svgz
%{_mandir}/man1/kdenlive*
