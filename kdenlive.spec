Summary:	KDE movie editor
Summary(pl.UTF-8):	Edytor filmów dla KDE
Name:		kdenlive
Version:	0.9.10
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.kde.org/stable/kdenlive/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	40d7ee8e388cb084f5eb1ad1596a14b2
URL:		http://kdenlive.org/
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libv4l-devel
BuildRequires:	mlt-devel >= 0.9.2
BuildRequires:	pkgconfig
BuildRequires:	qjson-devel >= 0.5
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	soprano-devel
Suggests:	dvdauthor
Suggests:	dvgrab
Suggests:	ffmpeg-ffplay
Suggests:	frei0r-plugins
Suggests:	mlt >= 0.9.2
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

cd ..
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/zh
%find_lang %{name} --with-kde

rm -rf $RPM_BUILD_ROOT%{_datadir}/menu

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}*
%{_libdir}/kde4/*
%{_datadir}/apps/%{name}
%{_datadir}/config/kdenlive*
%{_desktopdir}/kde4/%{name}.desktop
%{_datadir}/kde4/services/*.desktop
%{_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_mandir}/man1/kdenlive*
%{_pixmapsdir}/*
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svgz
%{_datadir}/mime/packages/*.xml
