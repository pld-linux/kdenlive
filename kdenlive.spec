# TODO:
# - Still fails with Failed to load plugin: /usr/share/mlt/modules/libmltavformat.so: undefined symbol: img_convert
Summary:	KDE movie editor
Summary(pl.UTF-8):	Edytor filmów dla KDE
Name:		kdenlive
Version:	0.7.8
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kdenlive/%{name}-%{version}.tar.gz
# Source0-md5:	7011d0c6b26f7f2350065defef3d9a76
URL:		http://kdenlive.org/
BuildRequires:	automake
BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:  kde4-kdebase-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:  shared-desktop-ontologies-devel
BuildRequires:  soprano-devel
BuildRequires:	mlt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Suggests:	dvdauthor
Suggests:	ffmpeg-ffplay 
Suggests:	recordmydesktop
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
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd ..
mv $RPM_BUILD_ROOT%{_datadir}/locale/zh  $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN
%find_lang %{name} --with-kde

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
%{_datadir}/pixmaps/*
%{_iconsdir}/*/*/*/*.png
%{_iconsdir}/*/*/*/*.svgz
%{_datadir}/mime/packages/*.xml
