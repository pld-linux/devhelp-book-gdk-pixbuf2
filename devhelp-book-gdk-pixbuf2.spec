Summary:	DevHelp book: gdk-pixbuf 1.2
Summary(pl):	Ksi��ka do DevHelpa o gdk-pixbuf 1.2
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


%description
DevHelp book about gdk-pixbuf 1.2.

%description -l pl
Ksi��ka do DevHelpa o gdk-pixbuf 1.2.

%prep
%setup -q -c -n gdk-pixbuf-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gdk-pixbuf-%{version},specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gdk-pixbuf-%{version}.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gdk-pixbuf-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
