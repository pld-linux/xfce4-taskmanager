Summary:	xfce4-taskmanager - simple task manager for Xfce
Summary(pl.UTF-8):	xfce4-taskmanager - prosty zarządca procesów dla Xfce
Name:		xfce4-taskmanager
Version:	1.5.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfce4-taskmanager/1.5/%{name}-%{version}.tar.bz2
# Source0-md5:	b9b802c9b789f1c4d7a90a9113ba5f35
Patch0:		%{name}-desktop.patch
URL:		https://goodies.xfce.org/projects/applications/xfce4-taskmanager/
BuildRequires:	autoconf
BuildRequires:	cairo-devel >= 1.5.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libwnck-devel >= 3.2
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
BuildRequires:	xorg-lib-libX11-devel >= 1.6.7
BuildRequires:	xorg-lib-libXmu-devel >= 1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-taskmanager is a simple task manager for Xfce.

%description -l pl.UTF-8
xfce4-taskmanager jest prostym zarządcą procesów dla Xfce.

%prep
%setup -q
%patch -P 0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ur_PK,hy_AM,hye,ie,fa_IR}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS THANKS
%attr(755,root,root) %{_bindir}/xfce4-taskmanager
%{_desktopdir}/xfce4-taskmanager.desktop
%{_iconsdir}/hicolor/*/*/*
