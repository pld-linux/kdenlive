Summary:	KDE movie editor
Summary(pl):	Edytor filmTODO 
Name:		kdenlive
Version:	0.2.4
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	2c78f21f00c761fd3c6631d68d0159b3
URL:		http://www.uchian.pwp.blueyonder.co.uk/kdenlive.html
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel 
Requires:	piave
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Kdenlive is a non-linear video editor for KDE. It provides all project management and editing tools while relying on a separate rendering program (currently PIAVE) to perform the editing operations. Support is planned for transitions, effects, multiple file formats, and full project and asset management support. The current beta is capable of editing raw DV or AVI DV files, with tools such as move, razor, and resize, selecting parts of clips using in/outpoints, and exporting the result to another raw DV file. You may playback/preview the contents of the timeline at any point during the edit. Full project save/load is supported.

%description -l pl
TODO

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/apps/%{name}

%{_applnkdir}/Multimedia/%{name}.desktop
%{_pixmapsdir}/*/*/apps/*.png
#%%{_pixmapsdir}/*/*/apps/*.rc
#%%{_libdir}/kde3/libkplayerpart.la
#%%{_libdir}/kde3/libkplayerpart.so
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/pixmaps/*/*/*/*.png
TODO:
   /usr/share/apps/kdenlive/icons/hicolor/32x32/actions/spacer.png
   /usr/share/apps/kdenlive/kdenlive-splash.png
   /usr/share/apps/kdenlive/kdenliveui.rc
   /usr/share/pixmaps/piave.png
