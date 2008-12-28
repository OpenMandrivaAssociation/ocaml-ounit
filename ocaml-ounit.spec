%define name	ocaml-ounit
%define version	1.0.3
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Unit test framework for OCaml
Group:      Development/Other
License:    MIT
URL:        http://www.xs4all.nl/~mmzeeman/ocaml/
Source0:    http://www.xs4all.nl/~mmzeeman/ocaml/ounit-%{version}.tar.gz
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
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
install -d -m 755 %{buildroot}%{_libdir}/ocaml/stublibs
make install DESTDIR=%{buildroot} OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENCE
%dir %{_libdir}/ocaml/oUnit
%{_libdir}/ocaml/oUnit/*.cmi
%{_libdir}/ocaml/oUnit/*.cma
%{_libdir}/ocaml/oUnit/META

%files devel
%defattr(-,root,root)
%doc LICENCE README doc
%{_libdir}/ocaml/oUnit/*.a
%{_libdir}/ocaml/oUnit/*.cmxa
%{_libdir}/ocaml/oUnit/*.mli

