%define name	ocaml-ounit
%define version	1.0.2
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Unit test framework for OCaml
Group:      Development/Other
License:    MIT
URL:        http://www.xs4all.nl/~mmzeeman/ocaml/
Source0:    http://www.xs4all.nl/~mmzeeman/ocaml/ounit-%{version}.tar.gz
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
OUnit is a unit test framework for OCaml. It allows one to easily
create unit-tests for OCaml code. It is based on HUnit, a unit testing
framework for Haskell. It is similar to JUnit, and other xUnit testing
frameworks.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ounit-%{version}

%build
make all
make allopt
make doc

%check
make test

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{ocaml_sitelib}
install -d -m 755 %{buildroot}%{ocaml_sitelib}/stublibs
make install DESTDIR=%{buildroot} OCAMLFIND_DESTDIR=%{buildroot}%{ocaml_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENCE
%dir %{ocaml_sitelib}/oUnit
%{ocaml_sitelib}/oUnit/*.cmi

%files devel
%defattr(-,root,root)
%doc LICENCE README doc
%dir %{ocaml_sitelib}/oUnit/*
%exclude %{ocaml_sitelib}/oUnit/*.cmi

