Summary:	DevHelp book: gdk-pixbuf
Summary(pl):	Ksi±¿ka do DevHelp'a o gdk-pixbuf
Name:		devhelp-book-gdk-pixbuf2
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gdk-pixbuf-2.0.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gdk-pixbuf 1.2

%description -l pl
Ksi±¿ka do DevHelp o gdk-pixbuf 1.2

%prep
%setup -q -c gdk-pixbuf-%{version} -n gdk-pixbuf-%{version}

%build
mv -f book gdk-pixbuf-%{version}
mv -f book.devhelp gdk-pixbuf-%{version}.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gdk-pixbuf-%{version}
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gdk-pixbuf-%{version}.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gdk-pixbuf-%{version}/* $RPM_BUILD_ROOT%{_prefix}/books/gdk-pixbuf-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
