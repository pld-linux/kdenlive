Summary:	KDE movie editor
Summary(pl):	Edytor film�w dla KDE
Name:		kdenlive
Version:	0.3.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kdenlive/%{name}-%{version}.tar.gz
# Source0-md5:	190efd0b823d8d5e10f72034c27667ee
URL:		http://kdenlive.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	kdelibs-devel
BuildRequires:	mlt++-devel >= 0.2.2
BuildRequires:	mlt-devel >= 0.2.2
BuildRequires:	rpmbuild(macros) >= 1.129
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

%description -l pl
Kdenlive to nieliniowy edytor film�w dla KDE. Dostarcza narz�dzia do
zarz�dzania projektem i edycji polegaj�ce na oddzielnym programie
renderuj�cym (aktualnie PIAVE) do wykonywania operacji edycji.
Planowana jest obs�uga przej��, efekt�w, wielu format�w plik�w oraz
pe�nego zarz�dzania projektem i kapita�em. Aktualna wersja beta mo�e
modyfikowa� pliki w formacie surowego DV oraz AVI DV przy u�yciu
narz�dzi takich jak przemieszczanie, ci�cia, zmiana rozmiaru,
wybieranie cz�ci klatek przy u�yciu punkt�w wej�ciowych/wyj�ciowych
oraz eksportowanie wyniku do innego pliku w formacie surowego DV.
Mo�na odtwarza�/podgl�da� zawarto�� w dowolnej chwili edycji.
Obs�ugiwany jest zapis/odczyt pe�nego projektu.

%prep
%setup -q -n %{name}-0.3

%build
cp -f /usr/share/automake/config.* admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%{__make} -f Makefile.cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_desktopdir}/kde/%{name}.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/config.kcfg/kdenlive.kcfg
%{_iconsdir}/*/*/apps/*.png
