#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.2
%define		qtver		5.15.2
%define		kaname		kdenlive
Summary:	KDE movie editor
Summary(pl.UTF-8):	Edytor filmów dla KDE
Name:		kdenlive
Version:	25.04.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	286db7d2eb235398168f1e385a654e5d
URL:		http://kdenlive.org/
BuildRequires:	Imath-devel >= 3.1.12
BuildRequires:	OpenTimelineIO-devel >= 0.17.0
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Multimedia-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6NetworkAuth-devel
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	kf6-attica-devel
BuildRequires:	kf6-karchive-devel
BuildRequires:	kf6-kbookmarks-devel
BuildRequires:	kf6-kconfig-devel
BuildRequires:	kf6-kconfigwidgets-devel
BuildRequires:	kf6-kcoreaddons-devel
BuildRequires:	kf6-kcrash-devel
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-kdeclarative-devel
BuildRequires:	kf6-kdoctools-devel
BuildRequires:	kf6-kfilemetadata-devel
BuildRequires:	kf6-kguiaddons-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kiconthemes-devel
BuildRequires:	kf6-kio-devel
BuildRequires:	kf6-knewstuff-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-knotifyconfig-devel
BuildRequires:	kf6-kplotting-devel
BuildRequires:	kf6-ktextwidgets-devel
BuildRequires:	kf6-kwidgetsaddons-devel
BuildRequires:	kf6-kxmlgui-devel
BuildRequires:	kf6-purpose-devel
BuildRequires:	kf6-sonnet-devel
BuildRequires:	libv4l-devel
BuildRequires:	mlt-devel >= 7.24.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qjson-devel >= 0.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	rttr-devel
BuildRequires:	shared-desktop-ontologies-devel
BuildConflicts:	gstreamer0.10
Requires:	%{name}-data = %{version}-%{release}
Requires:	Qt6Quick
Suggests:	dvdauthor
Suggests:	dvgrab
Suggests:	ffmpeg-ffplay
Suggests:	frei0r-plugins
Suggests:	mlt >= 7.12.0
Suggests:	recordmydesktop
Obsoletes:	ka5-%{kaname} < %{version}
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

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications/Multimedia
Obsoletes:	ka5-%{kaname}-data < %{version}
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%prep
%setup -q

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DPLUGIN_INSTALL_DIR=%{_libdir}/qt6/plugins \
	-DFETCH_OTIO=OFF

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/mltpreview.so

%files data  -f %{kaname}.lang
%defattr(644,root,root,755)
%{_datadir}/metainfo/org.kde.kdenlive.appdata.xml
%{_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_datadir}/knotifications6/kdenlive.notifyrc
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}
%{_desktopdir}/org.kde.kdenlive.desktop
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svg*
%{_mandir}/man1/kdenlive*
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/qlogging-categories6/kdenlive.categories
