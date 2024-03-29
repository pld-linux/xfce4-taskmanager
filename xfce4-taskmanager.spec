Summary:	xfce4-taskmanager - simple task manager for Xfce
Summary(pl.UTF-8):	xfce4-taskmanager - prosty zarządca procesów dla Xfce
Name:		xfce4-taskmanager
Version:	1.5.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-taskmanager/1.5/%{name}-%{version}.tar.bz2
# Source0-md5:	5c5b4838a73f9ee355c1df629da2cbfb
Patch0:		%{name}-desktop.patch
URL:		http://goodies.xfce.org/projects/applications/xfce4-taskmanager/
BuildRequires:	autoconf
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	intltool
BuildRequires:	libxfce4ui-devel >= 4.14.0
BuildRequires:	xorg-lib-libXmu-devel >= 1.1.2
BuildRequires:	libwnck-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-taskmanager is a simple task manager for Xfce.

%description -l pl.UTF-8
xfce4-taskmanager jest prostym zarządcą procesów dla Xfce.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ur_PK,hy_AM,hye,ie,fa_IR}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS THANKS
%attr(755,root,root) %{_bindir}/xfce4-taskmanager
%{_desktopdir}/xfce4-taskmanager.desktop
%{_iconsdir}/hicolor/*/*/*
