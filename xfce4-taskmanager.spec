Summary:	xfce4-taskmanager - simple task manager for Xfce
Summary(pl.UTF-8):	xfce4-taskmanager - prosty zarządca procesów dla Xfce
Name:		xfce4-taskmanager
Version:	0.3.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-taskmanager/%{name}-%{version}.tar.bz2
# Source0-md5:	f3f25dd5fe3e9a07291ff46fd578af26
URL:		http://goodies.xfce.org/projects/applications/xfce4-taskmanager/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= 4.4.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-taskmanager is a simple task manager for Xfce.

%description -l pl.UTF-8
xfce4-taskmanager jest prostym zarządcą procesów dla Xfce.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/xfce4-taskmanager
