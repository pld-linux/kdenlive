Summary:	KDE movie editor
Summary(pl):	Edytor filmów dla KDE
Name:		kdenlive
Version:	0.2.4
Release:	0.3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kdenlive/%{name}-%{version}.tar.gz
# Source0-md5:	2c78f21f00c761fd3c6631d68d0159b3
Patch0:		%{name}-piave.patch
Patch1:		%{name}-desktop.patch
URL:		http://kdenlive.sourceforge.net/
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	piave
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
Kdenlive to nieliniowy edytor filmów dla KDE. Dostarcza narzêdzia do
zarz±dzania projektem i edycji polegaj±ce na oddzielnym programie
renderuj±cym (aktualnie PIAVE) do wykonywania operacji edycji.
Planowana jest obs³uga przej¶æ, efektów, wielu formatów plików oraz
pe³nego zarz±dzania projektem i kapita³em. Aktualna wersja beta mo¿e
modyfikowaæ pliki w formacie surowego DV oraz AVI DV przy u¿yciu
narzêdzi takich jak przemieszczanie, ciêcia, zmiana rozmiaru,
wybieranie czê¶ci klatek przy u¿yciu punktów wej¶ciowych/wyj¶ciowych
oraz eksportowanie wyniku do innego pliku w formacie surowego DV.
Mo¿na odtwarzaæ/podgl±daæ zawarto¶æ w dowolnej chwili edycji.
Obs³ugiwany jest zapis/odczyt pe³nego projektu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Multimedia/*.desktop,%{_desktopdir}/kde}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_desktopdir}/kde/%{name}.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_iconsdir}/*/*/apps/*.png
%{_iconsdir}/piave.png
