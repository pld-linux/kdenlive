Summary:	KDE movie editor
Summary(pl.UTF-8):	Edytor filmów dla KDE
Name:		kdenlive
Version:	16.08.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	https://github.com/KDE/kdenlive/archive/v%{version}.tar.gz
# Source0-md5:	f8f457bedaadbe603911893b6d7a1a62
URL:		http://kdenlive.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake
BuildRequires:	gettext-tools
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kfilemetadata-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kplotting-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	libv4l-devel
BuildRequires:	mlt-devel >= 6.0.0
BuildRequires:	pkgconfig
BuildRequires:	qjson-devel >= 0.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel
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

%build
mkdir build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}*
%attr(755,root,root) %{_libdir}/plugins/mltpreview.so
%{_datadir}/appdata/kdenlive.appdata.xml
%{_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_datadir}/knotifications5/kdenlive.notifyrc
%{_datadir}/kservices5/mltpreview.desktop
%{_datadir}/kxmlgui5/kdenlive/kdenliveui.rc
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}
%{_desktopdir}/org.kde.kdenlive.desktop
%{_docdir}/HTML/en/kdenlive
/etc/xdg/%{name}*.knsrc
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svg
%{_iconsdir}/*/*/*/*.svgz
%{_mandir}/man1/kdenlive*
%{_pixmapsdir}/*
